# get_secondary_storage_consumed

Get the total secondary storage consumption of the Rubrik Mosaic cluster
```py
def get_secondary_storage_consumed()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| int  | The total secondary storage consumption in MB of the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_secondary_storage_consumed()```