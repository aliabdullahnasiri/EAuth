#!/usr/bin/env python
"""the eauth module"""

import sys
from typing import Literal, Union

import urllib3
from bs4 import BeautifulSoup
from requests import Session
from rich.console import Console
from rich.panel import Panel
from rich.traceback import install

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class EAuth:
    """the EAuth class"""

    def __init__(
        self,
        *,
        target: str,
        payload: str,
        data: str,
        method: Literal["POST", "GET"] = "POST",
        **kwargs,
    ):
        pass


if __name__ == "__main__":
    install()
    eauth = EAuth(
        target="https://nexa.gov.af/login",
        payload="",
        timeout=10,
        method="POST",
        data="username=aliabdullah&password=passwd",
        proxy="127.0.0.1:8080",
        cookies="security=low; PHPSESSID=iv09panmg7ld7qjq9gcsdccvg1",
        parameter="username",
    )
