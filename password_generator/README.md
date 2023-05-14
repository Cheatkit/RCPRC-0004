# Password Generator

This script generates strong, random passwords and provides options to save them to a file or copy them to the clipboard for easy use.

## Prerequisites

- Python 3.x
- Pyperclip (for clipboard functionality)

## How to Run

1. Make sure you have Python 3.x installed on your system.
2. Install the required `pyperclip` module by running the following command:
   ```
   pip install pyperclip
   ```
3. Download the script and save it with a `.py` extension (e.g., `password_generator.py`).
4. Open a terminal or command prompt and navigate to the directory where you saved the script.
5. Run the script using the following command:
   ```
   python password_generator.py
   ```

## Usage

1. The script will prompt you to enter the desired length of the password.
2. After generating a random password, it will be displayed on the console.
3. You will be asked if you want to save the password to a file. Respond with 'y' or 'n'.
   - If you choose to save the password, it will be appended to a file named "passwords.txt" in the current directory.
4. You will be asked if you want to copy the password to the clipboard. Respond with 'y' or 'n'.
   - If you choose to copy the password, it will be copied to your clipboard, allowing you to paste it conveniently.

## Customization

- You can modify the default length of the password by changing the value of the `length` variable in the script.
- The script uses a combination of uppercase letters, lowercase letters, digits, and punctuation symbols to generate passwords. If you want to modify the set of characters used, you can update the `characters` variable in the `generate_password()` function.

## License

This script inherits the liscence of the RCPRC organization [LISCENCE](https://github.com/RCPRC/.github/blob/main/LICENSE).