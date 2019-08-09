# Rubrik SDK for Python

## Installation

The SDK has been tested against Python 2.7.6 and Python 3.6.4.

Install from source:

```bash
git clone https://github.com/rubrik-devops/rubrik-mosaic-sdk-for-python
cd rubrik-mosaic-sdk-for-python
python setup.py install
```

## Configuration

Before you begin to use the Rubrik Mosaic Python SDK, you should first setup your authentication credentials. By default, the SDK will attempt to read the the Rubrik Mosaic Cluster credentials from the following environment variables:

* `rubrik_mosaic_node_ip`
* `rubrik_mosaic_username`
* `rubrik_mosaic_password`

## Usage

To use the SDK, you must first instantiate a new variable, in thise case `mosaic`, to connect to the Rubrik Mosaic Cluster.

```py
import rubrik_mosaic
mosaic = rubrik_mosaic.Connect()
```

{% hint style="info" %}
Note: You may use any variable name to connect to the Rubrik Mosaic Cluster.
{% endhint %}

If you have not configured the correct environment variables you may also manually pass in the required authentication credentials.

```py
import rubrik_cdm

node_ip = "172.21.8.90"
username = "sdk@rangers.lab"
password = "RubrikMosaicPythonSDK"

mosaic = rubrik_mosaic.Connect(node_ip, username, password)
```

## Debug

To enable debuging set the `Connect()` `enable_logging` keyword argument to `True`.

### Example

Script:

```py
import rubrik_mosaic
mosaic = rubrik_mosaic.Connect(enable_logging=True)

store_stats = mosaic.get_store_stats()
print(store_stats)
```

Output:

```shell
[2019-08-08 14:42:21,175] [DEBUG] -- Node IP: 172.21.8.53
[2019-08-08 14:42:21,175] [DEBUG] -- Node Port: 9090
[2019-08-08 14:42:21,175] [DEBUG] -- Username: demo
[2019-08-08 14:42:21,175] [DEBUG] -- Password: *******

[2019-08-08 14:43:11,846] [DEBUG] -- Generating API Token
[2019-08-08 14:43:14,377] [DEBUG] -- API Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsInByaW50LXByZXR0eSI6Im5vIiwiaWF0IjoxNTY1MjcxNzk0LCJleHAiOjE1Njc4NjM3OTR9.s2N71RFONZhQ1m0WvJTnGn_STBFSQP_ggxhooWpYGZ4
[2019-08-08 14:43:14,377] [DEBUG] -- GET https://172.21.8.53:9090/datos/liststore

```

## Certificate Verification

When connecting to a Rubrik Mosaic cluster without certificate verification enabled you will receive the following warning message:

```shell
/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning:
Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warningsInsecureRequestWarning)
```

To supress this warning add the following code to your script:

```py
import urllib3
urllib3.disable_warnings()
```
