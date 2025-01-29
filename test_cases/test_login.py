import pytest
import allure
from page_objects.login_page import LoginPage
from utils.login_manager import LoginManager
from utils.read_properties import ReadConfig
from utils.custom_logger import LogGen
from utils.common_utils import capture_screenshot


class TestLoginPage:
    """
    This class contains test cases for the LoginPage of the application.

    It includes tests for:
       - Logging in with valid credentials
       - Logging in with invalid credentials
       - Verifying the home page title after a successful login
    """
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    invalid_email = ReadConfig.get_invalid_user_email()
    invalid_password = ReadConfig.get_invalid_password()
    logger = LogGen.loggen()

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#01 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_login_with_valid_credentials(self, setup):
        """
        Test case for logging in with valid credentials.

        It verifies that the user can log in successfully and the home page title is correct.
        """
        self.logger.info("Testing Login with Valid Credentials")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        try:

            # Login
            login_manager = LoginManager(self.driver, self.username, self.password)
            login_manager.login()
            self.logger.info("Logged in successfully.")

            actual_title = self.driver.title

            assert actual_title == 'Alian Hub | Home', f"Expected title 'Alian Hub | Home' but got '{actual_title}'"
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_valid_credentials_passed')
            self.logger.info("Login with valid credentials passed.")

        except Exception as e:
            self.logger.error(f"An error occurred during login with valid credentials: {str(e)}")
            capture_screenshot(self.driver, "test_login_with_valid_credentials_failed")
            assert False, f"Test failed due to {str(e)}"

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#02 - Alian Hub Negative Test")
    @pytest.mark.negative
    def test_login_with_invalid_credentials(self, setup):
        """
        Test case for logging in with invalid credentials.

        It verifies that an appropriate warning message is displayed for invalid credentials.
        """
        self.logger.info("Testing Login with Invalid Credentials")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        try:

            login_page = LoginPage(self.driver)
            login_page.set_email_id(self.invalid_email)
            login_page.set_password(self.invalid_password)
            login_page.click_on_login_button()

            expected_warning_message = "Your email is invalid. Please check and try again"
            actual_warning_message = login_page.retrieve_warning_message()

            assert actual_warning_message == expected_warning_message, (
                f"Expected warning message '{expected_warning_message}' but got '{actual_warning_message}'"
            )
            allure.attach(self.driver.get_screenshot_as_png(), name='test_login_with_invalid_credentials_passed')
            self.logger.info("Login with invalid credentials passed.")

        except Exception as e:
            self.logger.error(f"An error occurred during login with invalid credentials: {str(e)}")
            capture_screenshot(self.driver, "test_login_with_invalid_credentials_failed")
            assert False, f"Test failed due to {str(e)}"

    @allure.epic("Alian Hub Login Test")
    @allure.feature("TC#03 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_home_page_title(self, setup):
        """
        Test case for verifying the home page title before login.

        It ensures that the title of the login page is correct when initially loading the page.
        """
        self.logger.info("Testing Homepage Title")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        try:
            actual_title = self.driver.title

            assert actual_title == 'Alian Hub | Login', f"Expected title 'Alian Hub | QA | Login' but got '{actual_title}'"
            allure.attach(self.driver.get_screenshot_as_png(), name='test_home_page_title_passed')
            self.logger.info("Homepage title verification passed.")
        except Exception as e:
            self.logger.error(f"An error occurred during homepage title verification: {str(e)}")
            capture_screenshot(self.driver, "test_home_page_title_failed")
            assert False, f"Test failed due to {str(e)}"
