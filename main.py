import pyautogui
import pyperclip
from pynput import mouse
import logging

# Basic configuration for the logging
logging.basicConfig(level=logging.INFO)

# Define a mapping for special characters
special_char_mapping = {
    '~': ['shift', '`'],
    '!': ['shift', '1'],
    '@': ['shift', '2'],
    '#': ['shift', '3'],
    '$': ['shift', '4'],
    '%': ['shift', '5'],
    '^': ['shift', '6'],
    '&': ['shift', '7'],
    '*': ['shift', '8'],
    '(': ['shift', '9'],
    ')': ['shift', '0'],
    '_': ['shift', '-'],
    '+': ['shift', '='],
    'Q': ['shift', 'q'],
    'W': ['shift', 'w'],
    'E': ['shift', 'e'],
    'R': ['shift', 'r'],
    'T': ['shift', 't'],
    'Y': ['shift', 'y'],
    'U': ['shift', 'u'],
    'I': ['shift', 'i'],
    'O': ['shift', 'o'],
    'P': ['shift', 'p'],
    '{': ['shift', '['],
    '}': ['shift', ']'],
    '|': ['shift', '\\'],
    'A': ['shift', 'a'],
    'S': ['shift', 's'],
    'D': ['shift', 'd'],
    'F': ['shift', 'f'],
    'G': ['shift', 'g'],
    'H': ['shift', 'h'],
    'J': ['shift', 'j'],
    'K': ['shift', 'k'],
    'L': ['shift', 'l'],
    ':': ['shift', ';'],
    '"': ['shift', '\''],
    'Z': ['shift', 'z'],
    'X': ['shift', 'x'],
    'C': ['shift', 'c'],
    'V': ['shift', 'v'],
    'B': ['shift', 'b'],
    'N': ['shift', 'n'],
    'M': ['shift', 'm'],
    '<': ['shift', ','],
    '>': ['shift', '.'],
    '?': ['shift', '/']
}


def on_click(x, y, button, pressed):
    try:
        if pressed:
            if button.name == 'button9':
                text_to_type = pyperclip.paste()  # Read from clipboard
                logging.info('button9 pressed! typing: {}'.format(text_to_type[0:32]))
                type_text(text_to_type)

    except Exception as err:
        logging.error('{}'.format(err))


def type_special_char(char):
    """
    This is a workaround for the VMWARE Horizon Client that for some reason has a sticky shift key with pyautogui
    So we're double-checking that the shift is pressed and released and this seems to resolve it
    """
    pyautogui.keyDown('shift')
    keys = special_char_mapping[char]
    pyautogui.hotkey(*keys)
    pyautogui.keyUp('shift')


def type_text(text):
    """
    Types the given text using the keyboard, handling special characters.
    """
    for char in text:
        if char in special_char_mapping:
            type_special_char(char)
        else:
            pyautogui.typewrite(char)


def main():
    # Set up the listener for mouse clicks
    with mouse.Listener(on_click=on_click) as listener:
        logging.info('type2rdp started!')
        listener.join()

    logging.info('type2rdp closed!')


if __name__ == "__main__":
    main()
