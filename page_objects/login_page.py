from selenium.webdriver.common.by import By
from utils.custom_logger import LogGen
from utils.common_utils import *

logger = LogGen.loggen()


class LoginPage:
    """
    This class represents the login page of the application.

    It provides methods to interact with elements on the login page, such as setting username and password,
    clicking the login button, and retrieving warning messages. It also includes methods to wait for specific
    conditions on the page.
    """

    # Locators
    txt_email_id = "email"
    txt_password_id = "password"
    btn_login_xpath = "//button[normalize-space()='Login']"
    toast_message_xpath = "//div[contains(@class, 'v-toast--top')]"

    def __init__(self, driver):
        """
        Initializes the CreateProject page object.

        :param driver: WebDriver instance to interact with the browser.
        """

        self.driver = driver

    def set_email_id(self, username):
        """
        Sets the username in the email input field.

        :param username: The username to be entered in the email field.
        """
        try:
            email_field = self.driver.find_element(By.ID, self.txt_email_id)
            email_field.clear()
            email_field.send_keys(username)
            logger.info(f"Entered username: {username}.")
        except Exception as e:
            logger.error(f"Failed to set username: {e}")
            raise

    def set_password(self, password):
        """
        Sets the password in the password input field.

        :param password: The password to be entered in the password field.
        """
        try:
            password_field = self.driver.find_element(By.ID, self.txt_password_id)
            password_field.clear()
            password_field.send_keys(password)
            logger.info(f"Entered password.")
        except Exception as e:
            logger.error(f"Failed to set password: {e}")
            raise

    def set_invalid_email_id(self, email):
        """
        Sets an invalid username in the email input field.

        :param email: The invalid email to be entered.
        """
        try:
            email_field = self.driver.find_element(By.ID, self.txt_email_id)
            email_field.clear()
            email_field.send_keys(email)
            logger.info(f"Entered invalid username: {email}.")
        except Exception as e:
            logger.error(f"Failed to set invalid username: {e}")
            raise

    def set_invalid_password(self, userpassword):
        """
        Sets an invalid password in the password input field.

        :param userpassword: The invalid password to be entered.
        """
        try:
            password_field = self.driver.find_element(By.ID, self.txt_password_id)
            password_field.clear()
            password_field.send_keys(userpassword)
            logger.info(f"Entered invalid password.")
        except Exception as e:
            logger.error(f"Failed to set invalid password: {e}")
            raise

    def click_on_login_button(self):
        """
        Clicks the login button to submit the login form.
        """
        try:
            login_button = self.driver.find_element(By.XPATH, self.btn_login_xpath)
            login_button.click()
            logger.info("Clicked on Login button.")
        except Exception as e:
            logger.error(f"Failed to click Login button: {e}")
            raise

    def wait_for_home_page(self):
        """
        Waits for the home page to load by checking that the page title contains 'Alian Hub | Home'.
        """
        try:
            webdriver_wait_for_title_contains(driver=self.driver, element_title="Alian Hub | Home", timeout=60)
            logger.info("Home page title verified.")
        except Exception as e:
            logger.error(f"Failed to wait for home page: {e}")
            raise

    def retrieve_warning_message(self):
        """
        Waits for the warning message to be visible and retrieves its text.

        :return: The text of the warning message.
        """
        try:
            warning_message_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.toast_message_xpath))
            )
            warning_message_text = warning_message_element.text
            logger.info(f"Retrieved warning message: {warning_message_text}")
            return warning_message_text
        except Exception as e:
            logger.error(f"Failed to retrieve warning message: {e}")
            raise
