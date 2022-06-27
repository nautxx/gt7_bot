import sys
import time
import argparse

import pyautogui


def press_key(key):
    """Presses a key (str). Note: Gran Turismo requires you hold a keypress for a
    small duration to count as a button press."""
    
    duration = 0.2
    hold_key(key, duration)
    time.sleep(duration)


def hold_key(key, duration):
    """Holds a key (str) for some duration (int/float)."""

    with pyautogui.hold(key):
        time.sleep(duration)


def focus_window():
    """Focuses on the window by clicking on the center of the primary screen."""

    x, y = pyautogui.size()
    center = x / 2, y / 2
    delay = 1
    pyautogui.moveTo(center)
    time.sleep(delay)
    pyautogui.click()
    time.sleep(delay)


def detect_on_screen(file_name):
    """Returns True if inputted image is a screen element that has been
    detected. Returns False otherwise."""

    x, y = pyautogui.size()
    half_x = int(x / 2)
    half_y = int(y / 2)

    confidence = 0.5
    grayscale = True
    region = (half_x, 0, half_x, half_y) # left, top, width, height

    path = f"images/{file_name}"
    print("Analyzing " + file_name + " screen.")
    detected_screen = pyautogui.locateOnScreen(
        path, region=region, grayscale=grayscale, confidence=confidence
    )
    
    return detected_screen is not None

def open_extra_menu():
    """Helper function to open the extra menu item."""

    press_key("enter")
    press_key("enter")
    time.sleep(3)
    press_key("escape")
    print("Extra menu item has been opened.")


def open_ticket():
    """Helper function to open a ticket."""

    # open ticket
    press_key("enter")
    press_key("enter")
    time.sleep(15)
    # Accept ticket
    press_key("enter")
    print("Ticket has been accepted.")


def get_tickets():

    # start at Cafe
    press_key("enter")
    print("Entering Cafe.")
    time.sleep(3)
    
    # navigate and select My Collection
    press_key("left")
    press_key("enter")
    
    # navigate and select Extra Menus
    press_key("down")
    press_key("right")
    press_key("enter")
    
    # navigate to extra menu no. 1
    press_key("up")

    # open extra menu no. 1
    print("Opening extra menu no. 1.")
    open_extra_menu()

    # navigate to extra menu no. 3
    press_key("right")

    # open extra menu no. 3
    print("Opening extra menu no. 3.")
    open_extra_menu()

    # navigate back to Cafe
    press_key("escape")
    press_key("escape")
    time.sleep(4)


def open_tickets():
    
    # navigate to Garage
    press_key("right")
    press_key("enter")
    time.sleep(4)

    # navigate to Gifts
    press_key("right")
    press_key("right")
    press_key("right")
    press_key("enter")

    # select and open 4-Star ticket
    print("Opening 4-Star ticket.")
    open_ticket()

    # screen detection for 4-Star ticket
    if detect_on_screen("car_text.png"):
        print("Car screen detected.")
        press_key("enter")
        time.sleep(10)
        press_key("enter")
        time.sleep(4)
        press_key("enter")
        press_key("enter")
    
    elif detect_on_screen("credits_text.png"):
        print("Credits screen detected.")
        press_key("enter")
        time.sleep(5)
        press_key("enter")
    
    elif detect_on_screen("tuning_text.png"):
        print("Tuning part screen detected.")
    
    elif detect_on_screen("invitation_text.png"):
        print("Invitation screen detected.")
    
    else:
        print("No screen has been detected. Exiting.")
        exit()

    # navigate to 6-Star ticket
    press_key("right")

    # select and open 6-Star ticket
    print("Opening 6-Star ticket.")
    open_ticket()

    # navigate back to map
    print("Heading back to map.")
    press_key("escape")
    press_key("escape")
    time.sleep(3)

    # place cursor on Menu to start over
    press_key("left")  


def execute_bot():
    """Main bot script."""

    focus_window()
    get_tickets()
    open_tickets()



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="gt7_bot by naut 2022"
    )
    parser.add_argument("--version", "-v", action="version", version="%(prog)s v0.0.2")

    args = parser.parse_args()

    cycles = 0
    while True:
        execute_bot()
        cycles += 1
        print(f"{str(cycles)} cyles completed.")