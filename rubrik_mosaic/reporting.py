# Copyright 2018 Rubrik, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License prop
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This module contains the Rubrik SDK Connect class.
"""

import requests
import os
import logging
import datetime
from copy import deepcopy

from .api import Api
from .exceptions import RubrikConnectionException, InvalidAPIEndPointException, MissingCredentialException


class Reporting(Api):
    #get a list of all the store stats from rdio
    def get_store_stats(self):
        stores = []
        for store in self.get("/liststore")['data']:
            stores.append(store['store_name'])
        for store in stores:
            self.log('get_store_stats - Found the following store: {}'.format(store))
        storestatslist = []
        for store in stores:
            self.log('get_store_stats - Getting store stats for store: {}'.format(store))
            storestats = self.get("/getstorestats/{}".format(store))['data']
            storestatslist.append(deepcopy(storestats))
        return storestatslist

    #get a list of all the source stats from rdio
    def get_source_stats(self):
        sources = []
        for source in self.get("/listsource")['data']:
            sources.append(source['source_name'])
        for source in sources:
            self.log('get_source_stats - Found the following source: {}'.format(source))
        sourcestatslist = []
        for source in sources:
            self.log('get_source_stats - Getting store stats for source: {}'.format(source))
            sourcestats = self.get("/getsourcestats/{}".format(source))['data']
            sourcestatslist.append(deepcopy(sourcestats))
        return sourcestatslist

    #get a list of all backup policy documents from rdio
    def get_policies(self):
        policylist = []
        for policy in self.get("/listpolicy")['data']:
            policylist.append(policy)
            self.log('get_policies - Found the following policy: {} - {}'.format(policy['sys_p_doc']['policy_group_name'], policy['sys_p_doc']['source_mgmt_obj']))
        return policylist

    def get_jobs(self):
        joblist = []
        scheduled = 0
        failed = 0
        successful = 0
        aborted = 0
        for job in self.get("/listjobs")['data']:
            joblist.append(job)
            if job['current_state'] == "job_scheduled":
                scheduled+=1
            elif job['current_state'] == "job_failed":
                failed+=1
            elif job['current_state'] == "job_successful":
                successful+=1
            elif job['current_state'] == "job_aborted":
                aborted+=1
        self.log('get_jobs - Found {} jobs. Job Summary - Scheduled: {} | Failed: {} | Successful: {} | Aborted: {}'.format(len(joblist), scheduled, failed, successful, aborted))
        return joblist

    #get a list of jobs with the specified state and end_time within num_hours
    def get_job_summary(self, job_state, num_hours):
        jobs = self.get_jobs()
        self.log('get_job_summary - Attepting to find \'{}\' jobs within the last {} hours'.format(job_state, num_hours))
        joblist = []
        hourdiff = datetime.timedelta(hours=num_hours)
        currenttime = datetime.datetime.now()
        for job in jobs:
            endtime = datetime.datetime.fromtimestamp(job['end_time'])
            if job['current_state'] in job_state and ((currenttime-endtime)<=hourdiff):
                joblist.append(job)
                starttime = datetime.datetime.fromtimestamp(job['start_time'])
                self.log('get_job_summary - Found match! job id: {} | start time: {} | end time: {} | status: {}'.format(job['_id'], starttime.strftime("%m-%d-%Y %H:%M:%S"), endtime.strftime("%m-%d-%Y %H:%M:%S"), job['current_state']))
        return joblist

    #calculate the number of objects currently under protection by the specified rdio cluster
    def get_protected_object_count(self):
        policies = self.get_policies()
        objectcount = 0
        for policy in policies:
            #verify we only have on object in our policy and not a list of objects, if so increment
            #this should always be the case currently, trying to futureproof this module
            if isinstance(policy['sys_p_doc']['source_mgmt_obj'], str) and policy['sys_p_doc']['policy_disabled'] == False:
                objectcount+=1
            #if we have a list of objects in our policy, increment the object count by the number of protected objects
            #this should not be the case currently, trying to futureproof this module
            elif isinstance(policy['sys_p_doc']['source_mgmt_obj'], list) and policy['sys_p_doc']['policy_disabled'] == False:
                objectcount+=len(policy['sys_p_doc']['source_mgmt_obj'])
            #skip disabled policies
            elif (isinstance(policy['sys_p_doc']['source_mgmt_obj'], str) or isinstance(policy['sys_p_doc']['source_mgmt_obj'], list)) and policy['sys_p_doc']['policy_disabled'] == True:
                pass
            #something went wrong, raise an error
            else:
                raise ValueError("get_protected_object_count - invalid source_mgmt_obj value in policy document {}".format(policy['sys_p_doc']['policy_group_name']))
        return objectcount

    #calculate the total capacity of data currently under protection by the specified rdio cluster
    def get_size_under_protection(self):
        sources = self.get_source_stats()
        sizeunderprotection = 0
        self.log('get_size_under_protection - Calculating capacity under protection')
        for source in sources:
            if source['db_stats']['status'] == True:
                self.log('get_size_under_protection - source {} has {} MB under protection'.format(source['source_name'], source['db_stats']['licensed_size']))
                sizeunderprotection+=int(source['db_stats']['licensed_size'])
            #skip disabled policies
            elif source['db_stats']['status'] != True:
                self.log('get_size_under_protection - source {} has a status of {}, skipping it'.format(source['source_name'], source['db_stats']['status']))
                pass
        return sizeunderprotection

    #calculate total secondary storage consumed 
    def get_secondary_storage_consumed(self):
        policies = self.get_policies()
        secondarystorageconsumed = 0
        for policy in policies:
            self.log('get_secondary_storage_consumed - {} - {} is storing {} MB of data'.format(policy['sys_p_doc']['policy_group_name'], policy['sys_p_doc']['source_mgmt_obj'], policy['physical_size']))
            secondarystorageconsumed+=int(policy['physical_size'])
        return secondarystorageconsumed

    #calculate total number of backups stored by rdio
    def get_backup_count(self):
        policies = self.get_policies()
        backupcount = 0
        for policy in policies:
            self.log('get_backup_count - {} - {} has {} versions'.format(policy['sys_p_doc']['policy_group_name'], policy['sys_p_doc']['source_mgmt_obj'], policy['version_count']))
            backupcount+=int(policy['version_count'])
        return backupcount