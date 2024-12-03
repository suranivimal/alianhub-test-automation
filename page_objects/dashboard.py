from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from utils.common_utils import *
from utils.read_properties import ReadConfig


class Dashboard:
    timeout = ReadConfig.get_global_timeout()

    """
    This class represents the dashboard of the application.

    It provides methods to interact with elements on the dashboard, such as the profile button
    and the logout button.
    """
    # Locators
    nav_projects = "//a[normalize-space()='Projects']"
    btn_profile_xpath = "//*[@class='profile-image asignee-profile']"
    btn_logout_xpath = "//span[@class='project-mobile-desc']"

    def __init__(self, driver):
        """
        Initializes the Dashboard page object.

        :param driver: WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def click_on_projects_nav(self):
        """
        Clicks on the 'Projects' tab to navigate to the projects.
        """
        locator = (By.XPATH, self.nav_projects)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Projects' tab: {e}")

    def click_on_profile(self):
        """
        Clicks on the profile button on the dashboard.

        This method locates the profile button using its XPath and performs a click action.
        """
        self.driver.find_element(By.XPATH, self.btn_profile_xpath).click()

    def click_on_logout(self):
        """
        Clicks on the logout button on the dashboard.

        This method locates the logout button using its XPath and performs a click action.
        """
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()
