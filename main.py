import argparse

import pyautogui


def execute_bot():
    """Main bot script."""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="gt7_bot by naut 2022"
    )
    subparser = parser.add_subparsers(dest='command')

    parser.add_argument("--version", "-v", action="version", version="%(prog)s v0.0.1")

    args = parser.parse_args()

    
    execute_bot()