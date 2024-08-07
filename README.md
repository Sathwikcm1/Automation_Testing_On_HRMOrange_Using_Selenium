# OrangeHRM Login Automation with Selenium

This project automates the login process for the OrangeHRM demo website using Selenium WebDriver and the Brave browser. It tests login with incorrect passwords followed by a valid one, and then interacts with all button elements post-login to ensure their functionality. The browser remains open after execution for further manual inspection.

## Features

- Automates login process for OrangeHRM demo website
- Tests login with multiple incorrect passwords before using the correct password
- Interacts with all button elements post-login to verify functionality
- Logs all actions and results for review
- Keeps browser open for manual inspection after automation script completes

## Requirements

- Python 3.x
- Selenium 4.4.0
- webdriver-manager 3.8.5
- Chrome browser installed via Snap on Linux Mint

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/orangehrm-login-automation.git
    cd orangehrm-login-automation
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Make sure Chrome browser is installed via Snap:
    ```sh
    sudo snap install brave
    ```

2. Run the script:
    ```sh
    python3 st1.py
    ```

3. The script will:
    - Attempt to log in with incorrect passwords and log the results
    - Attempt to log in with the correct password and log the results
    - Interact with all button elements on the page post-login
    - Keep the browser open for further manual inspection

## Script Overview

- **Human-like typing**: The script simulates human-like typing by adding random delays between keystrokes.
- **Login attempts**: The script first tries logging in with a series of incorrect passwords before using the valid password.
- **Button interaction**: Upon successful login, the script interacts with every button element on the page, clicking each one sequentially.
- **Logging**: All actions and results are logged for review.

## Logging

The script uses Python’s built-in logging module to log information at various levels (INFO, WARNING, ERROR). This helps in tracking the script’s progress and diagnosing any issues.

## Contribution

Feel free to fork this repository, submit issues, and send pull requests.

## License

This project is licensed under the MIT License.
