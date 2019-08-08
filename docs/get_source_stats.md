# get_source_stats

Get a list of all the data source stats from Rubrik Mosaic.
```py
def get_source_stats()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| list  | A list that contains the statistics for each data source in the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_source_stats()
```