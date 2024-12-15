# type2rdp

**type2rdp** is a Python script designed for environments where typing certain characters directly into a remote desktop (such as VMware Horizon Client) causes issues. This script listens for a specific mouse button event and, when triggered, types out the contents of your clipboard into the active window, handling special characters in a way that avoids sticky modifier issues.

## Features

- **Clipboard Integration**: Automatically reads the current system clipboard and types its contents.
- **Special Character Handling**: Works around issues that may arise with certain symbols and uppercase letters in remote desktop sessions.
- **Configurable Trigger**: By default, pressing mouse button 9 (a common extra button on some mice) triggers the typing action.
- **Logging**: Provides informative logging to help troubleshoot or confirm that the script is functioning as intended.

## Dependencies

Before running the script, ensure the following Python packages are installed:

- [pyautogui](https://pypi.org/project/PyAutoGUI/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [pynput](https://pypi.org/project/pynput/)

You can install these dependencies with:
```bash
pip3 install pyautogui pyperclip pynput
