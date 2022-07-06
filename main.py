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


def press_ps_button():
    """Press ps button. Note: Gran Turismo requires you hold a keypress for a
    small duration to count as a button press."""

    duration = 0.2
    pyautogui.moveTo(450, 524, duration = 0.2)
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()
    if args.debug:
        print("PS Button pressed.")


def restart_game():
    """Presses ps button and restarts game."""

    press_ps_button()
    delay(2)
    press_key("down")
    press_key("enter")
    press_key("enter")
    press_key("down")
    press_key("down")
    press_key("enter")  # close game
    delay(4)
    press_key("enter")  # reopen game
    delay(22)


def delay(duration):
    """Add delay for some duration(int/float)."""

    if args.debug:
        print(f"{duration} second delay.")
    time.sleep(duration)


def focus_window():
    """Focuses on the window by clicking on the center of the primary screen."""

    x, y = pyautogui.size()
    # center = x / 2, y / 2
    delay = 1
    pyautogui.moveTo(450, 15)
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


def open_ticket():
    """Helper function to open a ticket. Goes through an RNG roll."""

    press_key("enter")  # open_ticket
    press_key("enter")  # confirm to start the RNG roll.
    print("RNGing.")
    delay(16)


def accept_gift(option=4):
    """Helper function to accept a ticket using screen detection, but default 
    to normal acceptance if it fails."""

    if option == 4:
        press_key("enter")
        delay(10)
        press_key("enter")  # speeds up point tally
        delay(4)
        press_key("enter")
        press_key("enter")
    
    press_key("enter")  # accept the ticket


def get_tickets():
    """Gets all of the free tickets and goes back to home."""
    
    # enter world map
    press_key("enter")

    # enter cafe
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
    open_extra_menu_item()

    # navigate to extra menu no. 3
    press_key("right")
    press_key("right")

    # open extra menu no. 3
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
    accept_gift(4)

    # navigate to 6-Star rotary ticket
    press_key("right")

    # select and open 6-Star rotary roulette ticket
    print("Opening 6-Star roulette rotary ticket.")
    open_ticket()

    # accept 6-Star ticket
    accept_gift(6)

    # escape to world map
    press_key("escape")
    press_key("escape")


def execute_bot():
    """Main bot script."""

    focus_window()
    print("Getting tickets...")
    get_tickets()
    print("Opening tickets...")
    open_tickets()
    print("Restarting game...")
    restart_game()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="gt7_bot by naut 2022"
    )
    parser.add_argument("--version", "-v", action="version", version="%(prog)s v1.0.0")
    parser.add_argument("--cycles", "-c", type=int, default=True, help="indicate how many cyles to run. Default is set to infiniti.")
    parser.add_argument("--startup_delay", "-sd", type=int, default=5, help="startup delay in seconds.")
    parser.add_argument("--ps_button", "-ps", help="ps button coordinates.")
    parser.add_argument("--debug", "-db", action="store_true", help="toggle debug mode.")

    args = parser.parse_args()
    
    cycles = 0
    time_elapsed_m = 0
    total_completion_time = args.cycles * 2
    print(f"Estimated time to completion: {total_completion_time} minutes.")
    time_initial = time.time()
    while args.cycles:
        execute_bot()
        cycles += 1
        time_elapsed_s = time.time() - time_initial
        time_elapsed_m = time_elapsed_s / 60
        print(
            f"{str(cycles)} cycle{'s'[:cycles^1]} " + 
            f"completed over {time_elapsed_m} min."
        )
        print(
            "Estimated time to completion: " + 
            f"{total_completion_time - time_elapsed_m} min."
        )

        if args.cycles == cycles:
            args.cycles = False
            print("Bot operations complete.")