# get_size_under_protection

Get the total capacity of data currently under protection by the Rubrik Mosaic cluster
```py
def get_size_under_protection()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| int  | The total capacity of data currently under protection in MB of the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_size_under_protection()
```