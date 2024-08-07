from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import random
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the username and passwords for OrangeHRM
USERNAME = 'Admin'
INCORRECT_PASSWORDS = ['wrong_password1']  # Add more incorrect passwords if needed
VALID_PASSWORD = 'admin123'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
chrome_options.add_argument("--disable-extensions")  # Disable extensions

# Use webdriver_manager to manage ChromeDriver installation
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

def human_like_typing(element, text):
    """Simulate human-like typing by adding random delays between keystrokes."""
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))

def login_orangehrm(username, incorrect_passwords, valid_password):
    try:
        # Open OrangeHRM login page
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        for password in incorrect_passwords + [valid_password]:
            # Wait for the username field to be present
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )

            # Enter username
            username_input = driver.find_element(By.NAME, "username")
            username_input.clear()
            human_like_typing(username_input, username)

            # Enter password
            password_input = driver.find_element(By.NAME, "password")
            password_input.clear()
            human_like_typing(password_input, password)
            time.sleep(random.uniform(1, 3))  # Random delay before submitting password
            
            # Find and click the login button
            login_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
            login_button.click()

            # Wait for the result
            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".oxd-alert-content"))
                )
                logging.info(f"Login failed with password: '{password}'")
            except TimeoutException:
                try:
                    WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "oxd-topbar-header-breadcrumb"))
                    )
                    logging.info(f"Login successful with password: '{password}'")
                    check_buttons()
                    break
                except TimeoutException:
                    logging.warning(f"Unknown issue with login for password: '{password}'")
            time.sleep(2)

        logging.info("Login attempts have been processed.")
        
        # Keep the browser open until user input
        input("Press Enter to close the browser...")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        driver.quit()

def check_buttons():
    """Check and interact with all buttons on the page after successful login."""
    try:
        buttons = driver.find_elements(By.TAG_NAME, "button")
        
        for button in buttons:
            button_text = button.text
            button.click()
            time.sleep(2)  # Adjust the time gap as needed
            logging.info(f"Clicked button: {button_text}")
            time.sleep(2)
    except Exception as e:
        logging.error(f"An error occurred while checking buttons: {e}")

def main():
    login_orangehrm(USERNAME, INCORRECT_PASSWORDS, VALID_PASSWORD)

if __name__ == "__main__":
    main()

