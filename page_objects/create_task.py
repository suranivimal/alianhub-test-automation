from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from utils.common_utils import *
from utils.read_properties import ReadConfig


class CreateTask:

    timeout = ReadConfig.get_global_timeout()

    """
    Page Object Model for the Create Task page in the application.
    Contains locators and methods to interact with the Create Task page.
    """

    # Locators
    btn_task_id = "createtask_driver"
    txt_task_name = "//input[@id='inputId']"
    btn_task_save = "//button[normalize-space()='Save']"
    task_name_xpath = "//span[@class='text-ellipsis d-inline-block edit__taskname' and @title='Task 1025']"
    toast_message_task = "//div[contains(@class, 'v-toast__item') and contains(@class, 'v-toast__item--success')]"

    def __init__(self, driver):
        """
        Initializes the CreateTask page object.

        :param driver: WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def click_on_new_task_button(self):
        """
        Clicks on the 'New Task' button to create a new task.
        """
        locator = (By.ID, self.btn_task_id)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'New Task' button: {e}")

    def set_task_name(self, task_name):
        """
        Sets the name of the task in the task name input field.

        :param task_name: The name to be entered into the task name field.
        """
        try:
            element = self.driver.find_element(By.XPATH, self.txt_task_name)
            element.clear()
            element.send_keys(task_name)
        except NoSuchElementException as e:
            print(f"Error finding task name input field: {e}")
        except Exception as e:
            print(f"Error setting task name: {e}")

    def click_on_task_save_button(self):
        """
        Clicks on the 'Save' button to save the new task.
        """
        try:
            self.driver.find_element(By.XPATH, self.btn_task_save).click()
        except NoSuchElementException as e:
            print(f"Error finding 'Save' button: {e}")
        except Exception as e:
            print(f"Error clicking on 'Save' button: {e}")

    def verify_task_toast_message(self):
        """
        Verifies that the success toast message is displayed after task creation.

        :return: The text of the toast message.
        """
        toast_locator = (By.XPATH, self.toast_message_task)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator,
                                                             timeout=self.timeout)
            toast_element = self.driver.find_element(*toast_locator)
            return toast_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying task toast message: {e}")
            return None

    def verify_task_name(self, task_name):
        """
        Verifies that the task name is visible in the task list.

        :param task_name: The name of the task to verify.
        :return: The text of the task name element.
        """
        locator = (By.XPATH, f"//span[@class='text-ellipsis d-inline-block edit__taskname' and @title='{task_name}']")
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=locator, timeout=self.timeout)
            task_name_element = self.driver.find_element(*locator)
            return task_name_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying task name: {e}")
            return None
