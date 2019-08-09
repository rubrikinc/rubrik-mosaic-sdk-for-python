# Quick Start Guide: Rubrik Mosaic SDK for Python

## Introduction to the Rubrik Mosaic SDK for Python

Rubrik Mosaic’s API first architecture enables organizations to embrace and integrate Rubrik Mosaic functionality into their existing automation processes. While Rubrik Mosaic APIs can be consumed natively, companies are at various stages in their automation journey with different levels of automation knowledge on staff. The Rubrik Mosaic Software Development Kit (SDK) for Python extends upon Python’s easy to understand programming language, transforming Rubrik Mosaic functionality into easy to consume functions. This eliminates the need to understand how to consume raw Rubrik Mosaic APIs with Python and extends upon one of Rubrik Mosaic’s main design centers - simplicity.

## Authentication Mechanisms

The Rubrik Mosaic SDK for Python provides two mechanisms for supplying credentials to the `rubrik_mosaic.Connect()` function. Credentials may be accessed through the use of environment variables or manually passed into the function as parameters.

### Authenticating with Environment Variables

Storing credentials in environment variables is a more secure process than directly hard coding them into scripts and ensures that your credentials are not accidentally shared if your code is uploaded to an internal or public version control system such as GitHub. If no arguments are passed to the `rubrik_mosaic.Connect()` function, it will attempt to read the Rubrik Cluster credentials from the following environment variables:

* **`rubrik_mosaic_node_ip`** (Contains the IP/FQDN of a Rubrik Mosaic node)
* **`rubrik_mosaic_username`** (Contains a username with configured access to the Rubrik Mosaic cluster)
* **`rubrik_mosaic_password`** (Contains the password for the above user)

The way in which to populate these environment variables differs depending on the operating system running Python. Below are examples for Windows, Linux, and Mac OS.

#### Setting Environment Variables in Microsoft Windows

For Microsoft Windows-based operating systems the environment variables can be set utilizing the `setx` command as follows:

```batch
setx rubrik_mosaic_node_ip "192.168.0.100"
setx rubrik_mosaic_username "user@domain.com"
setx rubrik_mosaic_password "SecretPassword"
```

#### Setting Environment Variables in macOS and \*nix

For macOS and \*nix based operating systems the environment variables can be set utilizing the export command as follows:

```shell
export rubrik_mosaic_node_ip=192.168.0.100
export rubrik_mosaic_username=user@domain.com
export rubrik_mosaic_password=SecretPassword
```

In order for the environment variables to persist across terminal sessions, add the above three export commands to the ~\.bash_profile or ~\.profile file.

Once set, the `rubrik_mosaic.Connect()` function will automatically utilize the data within the environment variables to perform its connection unless credentials are specifically passed in the arguments of the function.

### Authenticate by Providing Username and Password

Although the use of environment variables are recommended, there may be scenarios where directly sending credentials to the `rubrik_mosaic.Connect()` function as parameters makes sense. When arguments are provided, any environment variable information, populated or unpopulated, is ignored. To pass connection and credential information, simply call the `rubrik_mosaic.connect()` function, passing the node IP, username, and password as follows:

```py
node_ip = "192.168.0.100"
username = "user@domain.com"
password = "SecretPassword"

mosaic = rubrik_mosaic.Connect(node_ip, username, password)
```

Mixing the usage of both environment and hard coded variables is supported. The below example is run under the pretense that the `rubrik_mosaic_node_ip` and `rubrik_mosaic_password` environment variables have been set, providing only the password to the connect function.

`mosaic = rubrik_mosaic.Connect(password="SecretPassword")`

## Connecting to a Rubrik Mosaic Cluster

The Rubrik Mosaic SDK for Python utilizes the `rubrik_mosaic.Connect()`function as a mechanism to provide credentials to Rubrik Mosaic. `rubrik_mosaic.Connect()` only needs to be called once, assigning the response to a variable to be used for subsequent calls throughout the remainder of the Python session. To initiate the function, first import the `rubrik_mosaic` package and assign the response of `rubrik_mosaic.Connect()` to a variable as follows:

```py
import rubrik_mosaic
mosaic = rubrik_mosaic.Connect()
```

| Note: You may use any variable name to connect to the Rubrik cluster. |
| --- |

Any subsequent calls to methods or functions within the rubrik_mosaic package are now executed through the context of the variable used to store the response from the Connect() method. For example, to retrieve statistics about configured data stores the following code is used:

```py
import rubrik_mosaic
mosaic = rubrik_mosaic.Connect()
print store_stats = mosaic.get_store_stats()
```

For a full list of functions, methods, and their associated arguments see the official [Rubrik Mosaic SDK for Python documentation](https://rubrik.gitbook.io/rubrik-mosaic-sdk-for-python).

### Certificate Validation

When connecting to a Rubrik Mosaic cluster without certificate validation enabled you will receive the following warning message:

```shell
/usr/local/lib/python3.6/site-packages/urllib3/connectionpool.py:857:
InsecureRequestWarning:
Unverified HTTPS request is being made. Adding certificate verification is strongly advised.
See:
https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warningsInsecureRequestWarning)
```

This warning may be suppressed utilizing the `urllib3` library and inserting the following code within your script:

```py
import rubrik_mosiac
import urllib3

urllib3.disable_warnings()

mosaic = rubrik_mosaic.Connect()
```

## Rubrik Mosaic SDK for Python Quick Start

The following section outlines how to get started using the Rubrik Mosaic SDK for Python, including installation, configuration, as well as sample code.

### Prerequisites

The following are the prerequisites in order to successfully install and run the sample code included in this quickstart guide:

* Python (Tested against v2.7.6 and v3.7.4)
* The [pip package management tool](https://pip.pypa.io/en/stable/)
* Rubrik Mosaic

### Installation

The Rubrik Mosaic SDK for Python can be installed into a Python environment either by utilizing the pip package manager or installing from source.

|Note: Installing from source should only be used when performing development work on the Rubrik Mosaic SDK for Python or if the environment does not allow for pip installations. The easiest and most common way to install the Rubrik Mosaic SDK for Python is through the pip package manager. |
| --- |

#### Install using the pip package manager

Due to the popular uptake of the pip package manager Rubrik also maintains a copy of the Rubrik Mosaic SDK for Python hosted within the Python Package Index. This allows for developers and operations to install the Rubrik Mosaic SDK for Python using pip as follows.

```bash
pip install rubrik-mosaic
```

The pip installation method will take care of downloading and installing all dependencies of the Rubrik Msoaic SDK for Python.

#### Install from Source

As the Rubrik Mosaic SDK for Python is hosted on GitHub, installing from source allows for the added benefit of being able to access newly created and “beta” type features as they are developed and pushed to the repository.

To install the Rubrik SDK for Python from source run the following commands.

```shell
git clone https://github.com/rubrik-devops/rubrik-mosaic-sdk-for-python
cd rubrik-mosaic-sdk-for-python
sudo python setup.py install
```

|Note: After executing `setup.py` install, all dependencies will be automatically downloaded and installed. |
| --- |

#### Accessing the Built-in Sample Code

To help accelerate development the Rubrik SDK for Python source contains many files containing common activities often performed against a Rubrik cluster. Sample files may be found on the [Rubrik SDK for Python GitHub page](https://github.com/rubrikinc/rubrik-sdk-for-python/tree/master/sample).

Sample code may be executed using the following syntax:

```bash
python samplefile.py
```

## Rubrik Mosaic SDK for Python Documentation

This guide acts only as a quick start to get up and running with the Rubrik Mosaic SDK for Python. For detailed information on all of the functions and features included see the complete [Rubrik Mosaic SDK for Python documentation](https://rubrik.gitbook.io/rubrik-mosaic-sdk-for-python).

## Troubleshooting

The Rubrik Mosaic SDK for Python contains built-in functions and configurations to help assist with troubleshooting any errors that may arise.

### Enabling Debug Mode

The `rubrik_mosaic.Connect()` function contains a built-in, verbose logging mechanism which is disabled by default. To enable the logging mechanism, set the `enable_logging` argument to true when connecting to the Rubrik cluster as follows:

```py
mosaic = rubrik_mosaic.Connect(enable_logging=True)
```

When doing so, more verbose debug messages will be displayed on the console when executing various commands and functions within the Rubrik Mosaic SDK for Python. For example, the `Connect()` function itself displays no information by default, however running the same function specifying enable_logging=True outputs the following:

```shell
[2019-08-08 14:42:21,175] [DEBUG] -- Node IP: 172.21.8.53
[2019-08-08 14:42:21,175] [DEBUG] -- Node Port: 9090
[2019-08-08 14:42:21,175] [DEBUG] -- Username: demo
[2019-08-08 14:42:21,175] [DEBUG] -- Password: *******

[2019-08-08 14:43:11,846] [DEBUG] -- Generating API Token
[2019-08-08 14:43:14,377] [DEBUG] -- API Token: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGFzc3dvcmQiOiJhZG1pbiIsInByaW50LXByZXR0eSI6Im5vIiwiaWF0IjoxNTY1MjcxNzk0LCJleHAiOjE1Njc4NjM3OTR9.s2N71RFONZhQ1m0WvJTnGn_STBFSQP_ggxhooWpYGZ4
[2019-08-08 14:43:14,377] [DEBUG] -- GET https://172.21.8.53:9090/datos/liststore

```

|Note: `enable_logging` only needs to be specified on the initial connection to Rubrik Mosaic when running the `Connect()` function. All subsequent calls to functions and methods within the Rubrik Mosaic SDK for Python will then display verbose logging to the console thereafter. |
| --- |

## Contributing to the Rubrik Mosaic SDK for Python

The Rubrik Mosaic SDK for Python is hosted on a public repository on GitHub. If you would like to get involved and contribute to the SDK please follow the below guidelines.

### Common Environment Setup

1. Clone the Rubrik Mosaic SDK for Python repository

```bash
git clone https://github.com/rubrikinc/rubrik-mosaic-sdk-for-python.git
```

2. Change to the repository root directory

```bash
cd rubrik-mosaic-sdk-for-python
```

3. Switch to the devel branch

```bash
git checkout devel
```

4. Create a virtual environment

For Python 3:

```bash
python3 -m venv venv
```

For Python 2:

```bash
virtualenv venv
```

5. Activate the virtual environment

```bash
. venv/bin/activate
```

6. Install the SDK from Source

```bash
python setup.py install
```

### New Function Development

The `/rubrik-mosaic-sdk-for-python/rubrik_mosaic` directory contains all functions for the SDK.

At a high level the directory contains the following:

* **`api.py`** - Base API Functions (get, post, etc.) that should only be touched for bug fixes.
* **`reporting.py`** - Reporting Functions
* **`rubrik_mosaic.py`** - Several internal functions as well as the Connect class which all other functions are accessed through. This should only be touched for bug fixes.

When adding a new function it ideally should be categorized to fit into one of the above files. Each function should meet the following requirements:

* Each function must be idempotent. Before making any configuration changes (post, patch, delete) you should first check to see if that change is necessary. If it's not you must return a message formatted as `No change required. {message}:`  For example, the assign_sla function first checks to see if the Rubrik object is already assigned to the provided SLA domain.
* A doc string using the docBlockr format. Visual Studio Code users can take advantage of the [autoDocstring](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) extension to simplify this process.
* Each API call made in the function should have a `self.log()` call made explaining what the API call is doing. The log message should be formatted as `function_name: message`.
* A corresponding example in the `/rubrik-sdk-for-python/sample` directory named the same as the function_name.
Each function also must have associated documentation which can be auto generated through `cd docs && python create_docs.py`

Once a new function has been added you will then submit a new Pull Request which will be reviewed before merging into the devel branch.

For more information around contributing to the Rubrik Mosaic SDK for Python see the [Rubrik MosaicSDK for Python Development Guide](https://github.com/rubrikinc/rubrik-mosaic-sdk-for-python/blob/devel/CONTRIBUTING.md) documentation on GitHub.

## Further Reading

* [Rubrik Mosaic SDK for Python GitHub Repository](https://github.com/rubrikinc/rubrik-mosaic-sdk-for-python)
* [Rubrik Mosaic SDK for Python Official Documentation](https://rubrik.gitbook.io/rubrik-mosaic-sdk-for-python)
* [Rubrik Mosaic API Documentation]
* [Rubrik Mosaic SDK for Python Development Guide (GitHub)](https://github.com/rubrikinc/rubrik-mosaic-sdk-for-python/blob/devel/CONTRIBUTING.md)
