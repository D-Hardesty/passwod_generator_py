# Password Manager

This is a simple password manager application built with Python and Tkinter.

## Overview

The Password Manager allows users to:

- Save and manage website credentials (website, email, password)
- Generate random passwords
- Retrieve saved passwords
- Copy passwords to the clipboard

## File Structure

- `password_manager.py`: The main Python script containing the application logic.
- `data.json`: A JSON file to store saved credentials.
- `logo.png`: Image file used for the application's logo.

## Dependencies

- Python 3.x
- Tkinter (Python's standard GUI library)
- pyperclip (for copying passwords to the clipboard)

## How to Run

1. Make sure you have Python installed on your system.
2. Run the `password_manager.py` script.
3. The graphical user interface (GUI) will appear, allowing you to interact with the password manager.

## Usage

### Save Password
- Enter the website, email, and password in the respective fields.
- Click the "Save" button to save the credentials.

### Generate Password
- Click the "Generate Password" button to generate a random password.
- The generated password will be copied to the clipboard.

### Find Password
- Enter the website for which you want to retrieve the password.
- Click the "Search" button to find and display the saved credentials.
- The password will be copied to the clipboard.

## Screenshots

Insert screenshots or GIFs of the application in action.

## Notes

- Make sure to handle the `DATA_FILE` (default: `data.json`) securely.
- The application relies on the `pyperclip` library for clipboard operations.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
