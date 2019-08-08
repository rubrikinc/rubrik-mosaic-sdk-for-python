# get_policies

Get a list of all the backup policy documents from Rubrik Mosaic.
```py
def get_policies()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| list  | A list that contains the details of each backup policy in the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_policies()
```