# get_protected_object_count

Get the number of objects currently under protection by the Rubrik Mosaic cluster
```py
def get_protected_object_count()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| int  | The total number of objects currently under protection by the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_protected_object_count()
```