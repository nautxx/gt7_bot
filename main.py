import sys
import time
import argparse

import pyautogui


def press_key(key: str) -> None:
    """Press a key. Gran Turismo requires you hold a keypress for a small duration."""
    
    with pyautogui.hold(key):
        time.sleep(0.2)
    time.sleep(0.2)


def hold_key(key: str, duration: float) -> None:
    """Hold a key for some duration."""

    with pyautogui.hold(key):
        time.sleep(duration)


def focus_window():
    """Focus the window by clicking on the center of the primary screen."""

    x, y = pyautogui.size()
    center = x / 2, y / 2
    pyautogui.moveTo(center)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)


def detect_screen(screen):

    width, height = pyautogui.size()
    halfwidth = int(width / 2)
    halfheight = int(height / 2)

    CONFIDENCE = 0.5
    GRAYSCALE = True
    REGION = (halfwidth, 0, halfwidth, halfheight)

    filename = screen + ".png"
    print(" [-] Analyzing " + filename + " screen.")
    detected_screen = pyautogui.locateOnScreen(
        filename, region=REGION, grayscale=GRAYSCALE, confidence=CONFIDENCE
    )
    if detected_screen is not None:
        return True
    else:
        return False


def execute_bot():
    """Main bot script."""
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="gt7_bot by naut 2022"
    )
    subparser = parser.add_subparsers(dest='command')

    parser.add_argument("--version", "-v", action="version", version="%(prog)s v0.0.1")

    args = parser.parse_args()

    
    execute_bot()