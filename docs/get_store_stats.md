# get_store_stats

Get a list of all the backup store stats from Rubrik Mosaic.
```py
def get_store_stats()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| list  | A list that contains the statistics for each backup store in the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_store_stats()```