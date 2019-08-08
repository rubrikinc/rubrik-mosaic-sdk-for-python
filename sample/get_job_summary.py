import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

'''
job_state should be one of:
  job_scheduled
  job_failed
  job_successful
  job_aborted
'''

mosaic.get_job_summary('job_successful',12)
