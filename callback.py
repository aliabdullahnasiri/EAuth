#!/usr/bin/env python

import re
from typing import Union

import click


def validate_url(ctx: click.Context, param: click.Parameter, value: str) -> str:
    """
    Validate the format of a URL.

    Args:
        ctx (click.Context): The Click context.
        param (click.Parameter): The Click parameter.
        value (str): The URL to validate.

    Returns:
        str: The valid URL.

    Raises:
        click.exceptions.ClickException: If the URL format is invalid.
            Example: "Invalid URL format! Please provide a valid URL."

    """
    url_pattern = re.compile(
        r"^(http[s]?:\/\/(www\.)?|ftp:\/\/(www\.)?|www\.)"
        r"([0-9A-Za-z-.@:%_+~#=]+)+((\.[a-zA-Z]{2,3})+)(\/(.*))?(\?(.*))?"
    )
    if re.match(url_pattern, value):
        return value

    raise click.exceptions.ClickException(
        "Invalid URL format! Please provide a valid URL."
    )


def parse_data(ctx: click.Context, param: click.Parameter, value: str) -> dict:
    """
    Parse and validate data in the form of key-value pairs.

    Args:
        ctx (click.Context): The Click context.
        param (click.Parameter): The Click parameter.
        value (str): The data to parse.

    Returns:
        dict: A dictionary containing key-value pairs.

    Raises:
        click.exceptions.ClickException: If the data format is invalid.
            Example: "Invalid Data format! Please provide data in key=value format."

    """
    data_pattern = r"^([a-zA-Z0-9_]+=[a-zA-Z0-9_@.]+)(&[a-zA-Z0-9_]+=[a-zA-Z0-9_@.]+)*$"
    if re.match(data_pattern, value):
        return dict(data.strip().split("=") for data in value.split("&"))

    raise click.exceptions.ClickException(
        "Invalid Data format! Please provide data in key=value format."
    )


def validate_parameter(ctx: click.Context, _: click.Parameter, value: str) -> str:
    """
    Validate an injectable parameter.

    Args:
        ctx (click.Context): The Click context.
        _ (click.Parameter): Unused parameter.
        value (str): The parameter to validate.

    Returns:
        str: The valid parameter.

    Raises:
        click.exceptions.ClickException: If the parameter is invalid.
            Example: "Invalid injectable parameter: 'example'! Please provide a valid parameter."

    """
    if value and value in ctx.params.get("data").keys():
        return value

    raise click.exceptions.ClickException(
        f"Invalid injectable parameter: {value!r}! Please provide a valid parameter."
    )


def parse_proxy(ctx: click.Context, param: click.Parameter, value: str) -> dict:
    """
    Parse and validate proxy information.

    Args:
        ctx (click.Context): The Click context.
        param (click.Parameter): The Click parameter.
        value (str): The proxy information to parse.

    Returns:
        dict: A dictionary containing proxy information.

    Raises:
        click.exceptions.ClickException: If the proxy format is invalid.
            Example: "Invalid proxy format! Please provide a valid proxy in the form of host:port."

    """
    proxy_pattern = re.compile(r"^[a-zA-Z0-9_.-]+:\d+$")
    if re.match(proxy_pattern, value):
        return {"http": value, "https": value}

    raise click.exceptions.ClickException(
        "Invalid proxy format! Please provide a valid proxy in the form of host:port."
    )


def parse_cookies(
    ctx: click.Context, param: click.Parameter, value: Union[str, None]
) -> dict:
    """
    Parse and validate cookie information.

    Args:
        ctx (click.Context): The Click context.
        param (click.Parameter): The Click parameter.
        value (Union[str, Noun]): The cookie information to parse.

    Returns:
        dict: A dictionary containing cookie information.

    Raises:
        click.exceptions.ClickException: If the cookie format is invalid.
            Example: "Invalid cookies format 'example'! Please provide valid cookies."

    """
    if value:
        cookies_pattern = re.compile(r"^([a-zA-Z0-9_]+=[^;]+)(; [a-zA-Z0-9_]+=[^;]+)*$")
        if re.match(cookies_pattern, value):
            return dict(data.strip().split("=") for data in value.split(";"))

        raise click.exceptions.ClickException(
            f"Invalid cookies format {value!r}! Please provide valid cookies."
        )
    else:
        return {}
