# get

Send a GET request to the provided Rubrik Mosaic API endpoint.
```py
def get(api_endpoint, timeout=15, params=None)
```

## Arguments
| Name        | Type | Description                                                                 | Choices |
|-------------|------|-----------------------------------------------------------------------------|---------|
| api_endpoint  | str  | The endpoint of the Rubrik Mosaic API to call (ex. /listjobs). |         |
## Keyword Arguments
| Name        | Type | Description                                                                 | Choices | Default |
|-------------|------|-----------------------------------------------------------------------------|---------|---------|
| params  | dict  | An optional dict containing variables in a key:value format to send with `GET` & `DELETE` API calls  |         |    None     |
| timeout  | int  | The number of seconds to wait to establish a connection the Rubrik Mosaic cluster before returning a timeout error.  |         |    15     |

## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| dict  | The response body of the API call. |
## Example
```py
import rubrik_mosaic

mosaic = rubrik_mosaic.Connect()

mosaic.get('/getall')
```