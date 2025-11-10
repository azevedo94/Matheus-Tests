#!/usr/bin/env python3
"""
Interactive prompt to collect Anaplan Basic Auth credentials and validate them
using the official Anaplan API client.
"""

from __future__ import annotations

import getpass
from typing import Optional

from anaplan.api import AnaplanAPI
from anaplan.api.exceptions import AnaplanAPIException


def prompt_for_credentials() -> tuple[str, str]:
    """Prompt the user for their Anaplan username and password."""
    print("🔒 Anaplan API Authentication (Basic Auth)")
    username = input("Enter your Anaplan username (email): ").strip()
    password = getpass.getpass("Enter your Anaplan password (input hidden): ")
    print("-" * 30)
    return username, password


def authenticate(username: str, password: str) -> Optional[AnaplanAPI]:
    """Attempt to authenticate with the Anaplan API using the provided credentials."""
    try:
        client = AnaplanAPI(username=username, password=password)

        # A lightweight call to verify the session; adjust as needed.
        client.models.get_models()

        print("✅ Successfully authenticated with Anaplan.")
        return client
    except AnaplanAPIException as err:
        print("❌ Authentication failed.")
        print(f"Reason: {err}")
        return None
    except Exception as err:
        print("🛑 Unexpected error during authentication.")
        print(f"Reason: {err}")
        return None


def main() -> None:
    username, password = prompt_for_credentials()
    authenticate(username, password)


if __name__ == "__main__":
    main()
