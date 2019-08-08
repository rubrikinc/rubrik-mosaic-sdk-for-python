# get_backup_count

Get the number of backups stored on a Rubrik Mosaic cluster.
```py
def get_backup_count()
```


## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| int  | The total number of backups stored on the Rubrik Mosaic cluster. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get_backup_count()```