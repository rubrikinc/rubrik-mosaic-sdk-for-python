# _common_api

Internal method that consolidates the base API functions.
```py
def _common_api(call_type, api_endpoint, config=None, timeout=15, params=None)
```

## Arguments
| Name        | Type | Description                                                                 | Choices |
|-------------|------|-----------------------------------------------------------------------------|---------|
| call_type  | str  | The HTTP Method for the type of RESTful API call being made.  |    'GET', 'POST', 'TOKEN_GENERATE'.     |
| api_endpoint  | str  | The endpoint of the Rubrik Mosaic API to call (ex. /login). |         |
## Keyword Arguments
| Name        | Type | Description                                                                 | Choices | Default |
|-------------|------|-----------------------------------------------------------------------------|---------|---------|
| params  | dict  | An optional dict containing variables in a key:value format to send with `GET` & `POST` API calls  |         |    None     |
| timeout  | int  | The number of seconds to wait to establish a connection the Rubrik cluster before returning a timeout error.  |         |    15     |

## Returns
| Type | Return Value                                                                                   |
|------|-----------------------------------------------------------------------------------------------|
| dict  | The full API call response for the provided endpoint. |
