# get_job_summary

Get a list of all the jobs from the Rubrik Mosaic cluster.
```py
def get_job_summary(job_state, num_hours)
```

## Arguments
| Name        | Type | Description                                                                 | Choices |
|-------------|------|-----------------------------------------------------------------------------|---------|
| job_state  | str  | The current state of the job as a string |         |
| num_hours  | int  | The number of hours to go back in the job history |         |

## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| list  | A list that contains the details of each job in the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

'''
job_state should be one of:
  job_scheduled
  job_failed
  job_successful
  job_aborted
'''

mosaic.get_job_summary('job_successful',12)```