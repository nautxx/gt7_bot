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
    if args.debug:
        print(f"{key} pressed.")


def hold_key(key, duration):
    """Holds a key (str) for some duration (int/float)."""

    with pyautogui.hold(key):
        time.sleep(duration)


def delay(duration):
    if args.debug:
        print(f"{duration} second delay.")
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


def open_extra_menu_item():
    """Helper function to open the extra menu."""

    press_key("enter")  # open extra menu
    press_key("enter")  # watch movie
    delay(3)
    press_key("escape") # skip movie
    print("Extra menu item has been opened.")


def open_ticket():
    """Helper function to open a ticket. Goes through an RNG roll."""

    press_key("enter")  # open_ticket
    press_key("enter")  # confirm to start the RNG roll.
    print("RNGing.")
    delay(16)


def accept_gift():
    """Helper function to accept a ticket using screen detection, but default 
    to normal acceptance if it fails."""

    if detect_on_screen("car_text.png"):
        print("Car screen detected.")
        press_key("enter")
        delay(10)
        press_key("enter")  # speed up point tally
        delay(4)
        press_key("enter")
        press_key("enter")
    
    elif detect_on_screen("credits_text.png"):
        print("Credits screen detected.")
        press_key("enter")
        delay(5)
        press_key("enter")
    
    elif detect_on_screen("tuning_text.png"):
        print("Tuning part screen detected.")
    
    elif detect_on_screen("invitation_text.png"):
        print("Invitation screen detected.")
    
    else:
        # use default ticket acceptance otherwise.
        press_key("enter")
        delay(10)
        press_key("enter")
        delay(4)
        press_key("enter")
        press_key("enter")

    press_key("enter")  # accept the ticket
    print("Ticket gift received.")


def get_tickets():
    """Gets all of the free tickets and goes back to home."""

    # start at home (Cafe)
    print("Entering Cafe.")
    press_key("enter")
    delay(3)
    
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
    open_extra_menu_item()

    # navigate to extra menu no. 3
    press_key("right")
    press_key("right")

    # open extra menu no. 3
    print("Opening extra menu no. 3.")
    open_extra_menu_item()

    # navigate back to home (Cafe)
    press_key("escape")
    press_key("escape")
    delay(4)


def open_tickets():
    """Opens both roulette tickets."""
    
    # navigate to Garage
    press_key("right")
    press_key("enter")
    delay(4)

    # navigate to Gifts
    press_key("right")
    press_key("right")
    press_key("right")
    press_key("enter")

    # select and open 4-Star roulette ticket
    print("Opening 4-Star roulette ticket.")
    open_ticket()

    # accept 4-Star ticket
    accept_gift()

    # navigate to 6-Star rotary ticket
    press_key("right")

    # select and open 6-Star rotary roulette ticket
    print("Opening 6-Star roulette rotary ticket.")
    open_ticket()

    # accept 6-Star ticket
    accept_gift()

    # navigate back to map
    print("Heading back to map.")
    press_key("escape")
    press_key("escape")
    delay(3)

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
    parser.add_argument("--version", "-v", action="version", version="%(prog)s v1.0.0")
    parser.add_argument("--cycles", "-c", type=int, default=True, help="Indicate how many cyles to run. Default is set to infiniti.")
    parser.add_argument("--debug", "-db", action="store_true", help="Toggle debug mode.")

    args = parser.parse_args()
    
    cycles = 0
    time_initial = time.time()
    while args.cycles:
        execute_bot()
        cycles += 1
        time_elapsed_s = time.time() - time_initial
        time_elapsed_m = time_elapsed_s / 60
        print(f"{str(cycles)} cycle{'s'[:cycles^1]} completed over {time_elapsed_m} min.")

        if args.cycles == cycles:
            args.cycles = False
            print(f"Bot operations complete.")