# EAuth

The "Authentication Exploit Toolkit" is a Python-based project designed to simplify the exploration and exploitation of authentication vulnerabilities in web applications. This toolkit comprises two main modules: eauth.py and exploit.py, along with a utility module callback.py.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [License](#license)

## Introduction

This project includes a Python module for handling authentication exploits (`eauth.py`) and an exploit module (`exploit.py`) providing a command-line interface for exploiting authentication vulnerabilities. Additionally, there's a callback module (`callback.py`) containing functions for validating URL, parsing data, validating injectable parameters, and parsing proxy and cookie information.

## Installation

To use this project, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/aliabdullahnasiri/EAuth.git

```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### `eauth.py`

The eauth.py module provides the EAuth class for handling authentication exploits. It includes various parameters such as target, payload, data, parameter, method, proxies, cookies, csrf, and timeout. The module also defines an exploit method to perform the authentication exploit.

Example:

```python
from eauth import EAuth

# Create an instance of EAuth
eauth = EAuth(target="http://example.com", payload="exploit_payload", data={"user": "admin"}, parameter="username")

# Perform the exploit
response = eauth.exploit()

# Access the response attributes
print(response.status_code)
print(response.text)
```

### `exploit.py`

The exploit.py module provides a command-line interface for exploiting authentication vulnerabilities. It utilizes the EAuth class from eauth.py to perform the exploits.

Example:

```bash
python exploit.py -T http://example.com -d "user=admin&password=pass123" -m POST -p username
```

### `callback.py`

The `callback.py` module contains callback functions used for input validation in the command-line interface. It includes functions for validating URLs, parsing data, validating injectable parameters, parsing proxy information, and parsing cookie information.

## Features

1. _EAuth Class:_ A class for handling authentication exploits with customizable parameters.
2. _Exploit Module:_ Command-line interface for exploiting authentication vulnerabilities.
3. _Callback Functions:_ Functions for validating inputs in the command-line interface.

## License

This project is licensed under the [GPL v3](./LICENSE) - see the LICENSE file
