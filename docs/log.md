# log

Create properly formatted debug log messages.
```py
def log(log_message)
```

## Arguments
| Name        | Type | Description                                                                 | Choices |
|-------------|------|-----------------------------------------------------------------------------|---------|
| log_message  | str  | The message to pass to the debug log. |         |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect(enable_logging=True)

mosaic.log('Python SDK')
```