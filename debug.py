import sys
import time
import pyautogui


def cursor_location():
    """Use to determine cursor location on screen."""
    
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)

    except KeyboardInterrupt:
        print('\n')