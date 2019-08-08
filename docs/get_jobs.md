# get_jobs

Get a list of all the jobs from the Rubrik Mosaic cluster.
```py
def get_jobs()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| list  | A list that contains the details of each job in the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_jobs()```