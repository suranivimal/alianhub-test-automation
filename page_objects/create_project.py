import time
import uuid

import pyautogui
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from page_objects.login_page import LoginPage
from utils.common_utils import *
from utils.read_properties import ReadConfig


class CreateProject:
    """
    Page Object Model for the Create Project page in the application.
    Contains locators and methods to interact with the Create Project page.
    """
    timeout = ReadConfig.get_global_timeout()

    # Locators

    btn_new_project = "(//button[normalize-space()='+ New Project'])[1]"

    # Step 1
    btn_blank_project = "//div[@id='createblankproject_driver']//button[@type='button']"
    btn_use_a_template = "(//button[@type='button'])[2]"

    # Step 2
    txt_project_name = "//input[@placeholder='Enter Project Name']"
    txt_project_key = "//div[@id='createprojectkey_driver']//input[@id='inputId']"
    sidebar_category_list = "//div[@id='createprojectcategory_driver']//input[@id='inputId']"
    sidebar_category_list_title = "//div[@class='assignee-headtitle d-block text-ellipsis text-nowrap'][normalize-space()='Category List']"
    sidebar_category_list_option_hourly_price = "(//div[@id='item0'])[1]"
    date_picker_due_date = "// input[ @ placeholder = 'Select Project Due Date']"
    btn_lead_assignee = "//ul[@class='d-flex']"
    sidebar_list_user_one = "(//div[@id='item0'])[1]"
    sidebar_list_user_close_btn = "//img[@alt='closeButton']"

    # Step 3
    btn_upload = "//label[normalize-space()='Upload']"

    # Step 4
    project_type_private = "//p[text()='Private']"

    # Step 5
    task_type_new_template_btn = "(//button[normalize-space()='+ New Template'])[1]"
    task_type_template_name = "(//input[@placeholder='Enter Template'])[1]"
    task_type_template_save_icon = "//span[@class='position-ab edit-rightinput save__closeimg-wrapper']//img[@class='cursor-pointer']"
    task_type_template_add_task_type_btn = "(//button[normalize-space()='+ Add Task Type'])[1]"
    task_type_template_bug = "(//span[contains(text(),'Bug')])[1]"
    task_type_template_subtask = "(//span[normalize-space()='Sub Task'])[1]"
    task_type_template_close_icon = "//div[@class='cursor-pointer d-flex align-items-center text-nowrap']//img"
    template_save_btn = "(//button[normalize-space()='Save Template'])[1]"
    templates_save_btn = "(//button[normalize-space()='Save Templates'])[1]"

    # Step 6
    project_status_template_new_template_btn = "(//button[normalize-space()='+ New Template'])[1]"
    project_status_template_name = "(//input[@placeholder='Enter Template'])[1]"
    project_status_template_save_icon = "//span[@class='position-ab edit-rightinput save__closeimg-wrapper']//img[@class='cursor-pointer']"
    project_status_template_add_status_btn = "(//button[normalize-space()='+ Add Status'])[1]"
    project_status_template_done = "(//div[@class='bg-white sidebar_item_main hover-bg-blue hover-white cursor-pointer d-flex align-items-center justify-content-between mobile-listuser'])[2]"
    project_status_template_on_hold = "(//div[@class='bg-white sidebar_item_main hover-bg-blue hover-white cursor-pointer d-flex align-items-center justify-content-between mobile-listuser'])[1]"
    project_status_template_completed = "(//span[normalize-space()='Completed'])[1]"
    project_status_template_close_icon = "//div[@class='cursor-pointer d-flex align-items-center text-nowrap']//img"
    project_status_templates_save_btn = "(//button[normalize-space()='Save Templates'])[1]"

    # Step 7
    task_status_template_new_template_btn = "(//button[normalize-space()='+ New Template'])[1]"
    task_status_template_name = "(//input[@placeholder='Enter Template'])[1]"
    task_status_template_save_icon = "//span[@class='position-ab edit-rightinput save__closeimg-wrapper']//img[@class='cursor-pointer']"
    task_status_template_add_status_btn = "(//button[normalize-space()='+ Add Status'])[1]"

    task_status_template_in_progress = "(//div[@class='bg-white sidebar_item_main hover-bg-blue hover-white cursor-pointer d-flex align-items-center justify-content-between mobile-listuser'])[1]"
    task_status_template_in_review = "(//div[@class='bg-white sidebar_item_main hover-bg-blue hover-white cursor-pointer d-flex align-items-center justify-content-between mobile-listuser'])[2]"
    task_status_template_backlog = "(//div[@class='bg-white sidebar_item_main hover-bg-blue hover-white cursor-pointer d-flex align-items-center justify-content-between mobile-listuser'])[3]"
    task_status_template_close_icon = "//div[@class='cursor-pointer d-flex align-items-center text-nowrap']//img"
    task_status_templates_save_btn = "(//button[normalize-space()='Save Template'])[1]"

    # Step 8
    btn_enable_apps = "(//div[@class='toggle bg-lowlight-gray mr-10px'])[1]"
    apps_title = "(//h3[normalize-space()='Choose Apps'])[1]"
    custom_field_title = "(//button[normalize-space()='+ Add Custom Field'])[1]"

    # Step 9

    btn_add_custom_field = "(//button[normalize-space()='+ Add Custom Field'])[1]"
    btn_number = "(//h5[normalize-space()='Number'])[1]"
    txt_box_field_label = "(//input[@placeholder='Enter Field Label'])[1]"
    txt_box_placeholder = "//input[@placeholder='Enter Placeholder']"
    txt_box_text_area = "(//textarea[@id='text'])[1]"
    btn_save = "(//button[normalize-space()='Save'])[1]"

    # Step 10

    view_title = "(//h3[normalize-space()='Required views'])[1]"

    btn_board_view = "(//div[@class='toggle bg-lowlight-gray ml-5px'])[1]"
    board_view_label = "(//span[normalize-space()='Board'])[1]"

    btn_project_details_view = "(//div[@class='toggle bg-lowlight-gray ml-5px'])[1]"
    project_details_label = "(//span[@class='changesFont margin-left-value ml-5px enableapp-list-desktop'][normalize-space()='Project Details'])[1]"

    btn_comments_view = "(//div[@class='toggle bg-lowlight-gray ml-5px'])[1]"
    comments_view_label = "(//span[normalize-space()='Comments'])[1]"

    btn_calendar_view = "(//div[@class='toggle bg-lowlight-gray ml-5px'])[1]"
    calendar_view_label = "(//span[normalize-space()='Calendar'])[1]"

    btn_activity_view = "(//div[@class='toggle bg-lowlight-gray ml-5px'])[1]"
    activity_view_label = "(//span[normalize-space()='Activity'])[1]"

    btn_workload_view = "(//div[@class='toggle bg-lowlight-gray ml-5px'])[1]"
    workload_view_label = "(//span[normalize-space()='Workload'])[1]"

    btn_table_view = "(//div[@class='toggle bg-lowlight-gray ml-5px'])[1]"
    table_view_label = "(//span[normalize-space()='Table'])[1]"

    # btn_board_view = "(//div)[575]"
    # btn_project_details_view = "(//div)[582]"
    # btn_comments_view = "(//div)[589]"
    # btn_calendar_view = "(//div)[596]"
    # btn_activity_view = "(//div)[603]"
    # btn_workload_view = "(//div)[610]"
    # btn_table_view = "(//div)[617]"

    txt_project_template = "(//p[@class='privatespace-desc-desktop'])[1]"
    btn_next = "(//button[normalize-space()='Next'])[1]"
    toggle_view_project_details = "//div[@id='my-sidebar']//div[3]//div[2]//div[2]"
    btn_create_project = "(//button[normalize-space()='Create Project'])[1]"
    project_list_fav = "//img[@id='projestleftlistfilter_driver']"
    project_name = "//span[@class='text-ellipsis project-sb-ptitle font-size-13 font-weight-500 mw-80']"
    option_template = "//div[@class='template_project_img']//img[@class='cursor-pointer']"
    btn_use_template = "//button[normalize-space()='Use Template']"
    toast_message_project = "//div[contains(@class, 'v-toast__item') and contains(@class, 'v-toast__item--success')]"

    def click_on_add_custom_field(self):

        btn_add_custom_field_locator = (By.XPATH, self.btn_add_custom_field)
        btn_number_locator = (By.XPATH, self.btn_number)
        txt_box_field_label_locator = (By.XPATH, self.txt_box_field_label)
        txt_box_placeholder_locator = (By.XPATH, self.txt_box_placeholder)
        txt_box_text_area_locator = (By.XPATH, self.txt_box_text_area)
        btn_save_locator = (By.XPATH, self.btn_save)

        try:

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_add_custom_field_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*btn_add_custom_field_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_number_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*btn_number_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=txt_box_field_label_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*txt_box_field_label_locator).send_keys("Number")

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=txt_box_placeholder_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*txt_box_placeholder_locator).send_keys("Enter Number")

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=txt_box_text_area_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*txt_box_text_area_locator).send_keys("Number Description ....sdsds")

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_save_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*btn_save_locator).click()

        except NoSuchElementException as e:
            print(f"Error clicking on 'Add Custom Field' button: {e}")

    def __init__(self, driver):
        """
        Initializes the CreateProject page object.

        :param driver: WebDriver instance to interact with the browser.
        """
        self.driver = driver

    def wait_for_project_list_fav(self):
        """
        Waits for the 'favorite' icon to be visible on the project list sidebar.
        """
        locator = (By.XPATH, self.project_list_fav)
        try:
            webdriver_for_presence_of_element_located(driver=self.driver, locator=locator, timeout=self.timeout)
        except TimeoutException as e:
            print(f"Timeout waiting for 'Fav' icon on project list sidebar: {e}")

    def click_on_new_project_button(self):
        """
        Clicks on the 'New Project' button to start creating a new project.
        """
        try:
            self.driver.find_element(By.XPATH, self.btn_new_project).click()
        except NoSuchElementException as e:
            print(f"Error clicking on 'New Project' button: {e}")

    def click_on_blank_project_button(self):
        """
        Clicks on the 'Blank Project' button to create a new project from scratch.
        """
        locator = (By.XPATH, self.btn_blank_project)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Blank Project' button: {e}")

    def click_on_use_a_template_button(self):
        """
        Clicks on the 'Use a Template' button to use a predefined template for the project.
        """
        locator = (By.XPATH, self.btn_use_a_template)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Use a Template' button: {e}")

    def set_project_name(self, project_name):
        """
        Sets the name of the project in the project name input field.

        :param project_name: The name to be entered into the project name field.
        """
        try:
            element = self.driver.find_element(By.XPATH, self.txt_project_name)
            element.clear()
            element.send_keys(project_name)
        except NoSuchElementException as e:
            print(f"Error setting project name: {e}")

    def set_project_key(self, project_key):
        """
        Sets the project key in the project key input field.

        :param project_key: The key to be entered into the project key field.
        """
        locator = (By.XPATH, self.txt_project_key)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            element = self.driver.find_element(*locator)
            element.clear()
            element.send_keys(project_key)
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error setting project key: {e}")

    def click_on_category_dropdown(self):
        """
        Clicks on the category dropdown to select a category for the project.
        """
        locator = (By.XPATH, self.sidebar_category_list)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on category dropdown: {e}")

    def select_category(self):
        """
        Selects a category from the category dropdown.
        """
        locator = (By.XPATH, self.sidebar_category_list_title)
        try:
            webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Category List",
                                               timeout=self.timeout)
            self.driver.find_element(By.XPATH, self.sidebar_category_list_option_hourly_price).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting category: {e}")

    def verify_project_template_text(self):
        txt_locator = (By.XPATH, self.txt_project_template)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=txt_locator,
                                                             timeout=90)
            txt_element = self.driver.find_element(*txt_locator)
            return txt_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying project template title: {e}")
            return None

    def click_on_lead_dropdown(self):
        """
        Clicks on the 'lead assignee' to select an assignee for the project.
        """
        locator = (By.XPATH, self.btn_lead_assignee)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'lead assignee' button: {e}")

    def select_assignee(self):

        locator = (By.XPATH, self.sidebar_list_user_one)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting assignee: {e}")

    def close_assignee_sidebar(self):
        locator = (By.XPATH, self.sidebar_list_user_close_btn)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on  close button of assignee sidebar: {e}")

    def project_image_upload(self):

        upload_button = self.driver.find_element(By.XPATH, self.btn_upload)  # Adjust XPath
        upload_button.click()

        # Wait for the file picker to open
        time.sleep(2)

        # Automate the file picker using PyAutoGUI
        file_path = "C:\\Users\\Alian Testing\\Downloads\\test.png"  # Replace with the correct file path
        pyautogui.write(file_path)  # Type the file path
        pyautogui.press('enter')

    def select_project_type(self):

        locator = (By.XPATH, self.project_type_private)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'project type': {e}")

    @staticmethod
    def generate_task_template_name():
        unique_id = uuid.uuid4().hex[:6].capitalize()  # Generate a unique identifier
        return f"{unique_id}"

    def select_task_type_template(self):

        new_template_btn_locator = (By.XPATH, self.task_type_new_template_btn)
        template_name_locator = (By.XPATH, self.task_type_template_name)
        template_save_locator = (By.XPATH, self.task_type_template_save_icon)
        template_add_task_type_locator = (By.XPATH, self.task_type_template_add_task_type_btn)
        template_bug_locator = (By.XPATH, self.task_type_template_bug)
        template_subtask_locator = (By.XPATH, self.task_type_template_subtask)
        template_close_locator = (By.XPATH, self.task_type_template_close_icon)
        template_save_btn_locator = (By.XPATH, self.template_save_btn)
        template_name = self.generate_task_template_name()
        login_page = LoginPage(self.driver)

        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=new_template_btn_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*new_template_btn_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_name_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*template_name_locator).send_keys(template_name)

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_save_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*template_save_locator).click()

            login_page.retrieve_warning_message()

            expected_warning_message = "Template has been created Successfully."
            actual_warning_message = login_page.retrieve_warning_message()

            assert actual_warning_message == expected_warning_message, (
                f"Expected warning message '{expected_warning_message}' but got '{actual_warning_message}'"
            )

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_add_task_type_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*template_add_task_type_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_bug_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*template_bug_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_subtask_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*template_subtask_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_close_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*template_close_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=template_save_btn_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*template_save_btn_locator).click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting on 'task type template': {e}")

    def select_project_status_template(self):

        project_status_template_new_template_locator = (By.XPATH, self.project_status_template_new_template_btn)
        project_status_template_name_locator = (By.XPATH, self.project_status_template_name)
        project_status_template_save_locator = (By.XPATH, self.project_status_template_save_icon)
        project_status_template_add_status_locator = (By.XPATH, self.project_status_template_add_status_btn)
        project_status_template_done_locator = (By.XPATH, self.project_status_template_done)
        project_status_template_on_hold_locator = (By.XPATH, self.project_status_template_on_hold)
        project_status_template_completed_locator = (By.XPATH, self.project_status_template_completed)
        project_status_template_close_btn_locator = (By.XPATH, self.project_status_template_close_icon)
        project_status_templates_save_btn_locator = (By.XPATH, self.project_status_templates_save_btn)
        login_page = LoginPage(self.driver)

        template_name = self.generate_task_template_name()

        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=project_status_template_new_template_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_new_template_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=project_status_template_name_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_name_locator).send_keys(template_name)

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=project_status_template_save_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_save_locator).click()

            login_page.retrieve_warning_message()

            expected_warning_message = "Template has been created Successfully."
            actual_warning_message = login_page.retrieve_warning_message()

            assert actual_warning_message == expected_warning_message, (
                f"Expected warning message '{expected_warning_message}' but got '{actual_warning_message}'"
            )

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=project_status_template_add_status_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_add_status_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=project_status_template_done_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_done_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=project_status_template_on_hold_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_on_hold_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=project_status_template_completed_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_completed_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=project_status_template_close_btn_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_template_close_btn_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=project_status_templates_save_btn_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*project_status_templates_save_btn_locator).click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting on 'project status template': {e}")

    def select_task_status_template(self):

        task_status_new_template_locator = (By.XPATH, self.task_status_template_new_template_btn)
        task_status_template_name_locator = (By.XPATH, self.task_status_template_name)
        task_status_template_save_locator = (By.XPATH, self.task_status_template_save_icon)
        task_status_template_add_status_locator = (By.XPATH, self.task_status_template_add_status_btn)

        task_status_template_in_progress_locator = (By.XPATH, self.task_status_template_in_progress)
        task_status_template_in_review_locator = (By.XPATH, self.task_status_template_in_review)
        task_status_template_backlog_locator = (By.XPATH, self.task_status_template_backlog)

        task_status_template_close_locator = (By.XPATH, self.task_status_template_close_icon)
        task_status_template_save_btn_locator = (By.XPATH, self.task_status_templates_save_btn)
        login_page = LoginPage(self.driver)

        template_name = self.generate_task_template_name()

        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=task_status_new_template_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_new_template_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=task_status_template_name_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_name_locator).send_keys(template_name)

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=task_status_template_save_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_save_locator).click()

            login_page.retrieve_warning_message()

            expected_warning_message = "Template has been created Successfully."
            actual_warning_message = login_page.retrieve_warning_message()

            assert actual_warning_message == expected_warning_message, (
                f"Expected warning message '{expected_warning_message}' but got '{actual_warning_message}'"
            )

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=task_status_template_add_status_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_add_status_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=task_status_template_in_progress_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_in_progress_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=task_status_template_in_review_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_in_review_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=task_status_template_backlog_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_backlog_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=task_status_template_close_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_close_locator).click()

            webdriver_wait_for_element_to_be_clickable(driver=self.driver,
                                                       locator=task_status_template_save_btn_locator,
                                                       timeout=self.timeout)
            self.driver.find_element(*task_status_template_save_btn_locator).click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting on 'task status template': {e}")

    def click_on_enable_apps(self):
        locator = (By.XPATH, self.btn_enable_apps)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'enable apps' button:{e}")

    def click_on_next_button(self):
        """
        Clicks on the 'Next' button to proceed to the next step in the project creation process.
        """
        locator = (By.XPATH, self.btn_next)
        try:
            webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Next", timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Next' button: {e}")

    def click_on_board_view(self):
        """
        Clicks on the 'Board View' radio button in the project details section.
        """
        try:
            board_view_label_locator = (By.XPATH, self.board_view_label)
            btn_board_view_element = WebDriverWait(self.driver, 60).until(
                lambda driver: driver.find_element(
                    locate_with(By.XPATH, self.btn_board_view).to_right_of(
                        driver.find_element(*board_view_label_locator)
                    )
                )
            )

            # Click the located radio button
            btn_board_view_element.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Board View' radio button: {e}")

    def click_on_project_details_view(self):
        """
        Clicks on the 'Project Details View' radio button in the project details section.
        """
        try:

            project_details_label_locator = (By.XPATH, self.project_details_label)
            btn_project_details_view_element = WebDriverWait(self.driver, 60).until(
                lambda driver: driver.find_element(
                    locate_with(By.XPATH, self.btn_project_details_view).to_right_of(
                        driver.find_element(*project_details_label_locator)
                    )
                )
            )
            btn_project_details_view_element.click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Project Details View' radio button: {e}")

    def click_on_comments_view(self):
        """
        Clicks on the 'Comments View' radio button in the project details section.
        """
        try:
            comments_view_label_locator = (By.XPATH, self.comments_view_label)
            btn_comments_view_element = WebDriverWait(self.driver, 60).until(
                lambda driver: driver.find_element(
                    locate_with(By.XPATH, self.btn_comments_view).to_right_of(
                        driver.find_element(*comments_view_label_locator)
                    )
                )
            )

            btn_comments_view_element.click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Comments View' radio button: {e}")

    def click_on_calendar_view(self):
        """
        Clicks on the 'Calendar View' radio button in the project details section.
        """

        try:
            calendar_view_label_locator = (By.XPATH, self.calendar_view_label)
            btn_calendar_view_element = WebDriverWait(self.driver, 60).until(
                lambda driver: driver.find_element(
                    locate_with(By.XPATH, self.btn_calendar_view).to_right_of(
                        driver.find_element(*calendar_view_label_locator)
                    )
                )
            )
            btn_calendar_view_element.click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Calendar View' radio button: {e}")

    def click_on_activity_view(self):
        """
        Clicks on the 'Activity View' radio button in the project details section.
        """
        try:
            activity_view_label_locator = (By.XPATH, self.activity_view_label)

            btn_activity_view_element = WebDriverWait(self.driver, 60).until(
                lambda driver: driver.find_element(
                    locate_with(By.XPATH, self.btn_activity_view).to_right_of(
                        driver.find_element(*activity_view_label_locator)
                    )
                )
            )

            btn_activity_view_element.click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Activity View' radio button: {e}")

    def click_on_workload_view(self):
        """
        Clicks on the 'Workload iew' radio button in the project details section.
        """

        try:

            workload_view_label_locator = (By.XPATH, self.workload_view_label)
            btn_workload_view_element = WebDriverWait(self.driver, 60).until(
                lambda driver: driver.find_element(
                    locate_with(By.XPATH, self.btn_workload_view).to_right_of(
                        driver.find_element(*workload_view_label_locator)
                    )
                )
            )

            btn_workload_view_element.click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Workload View' radio button: {e}")

    def click_on_table_view(self):
        """
        Clicks on the 'Table View' radio button in the project details section.
        """

        try:
            table_view_label_locator = (By.XPATH, self.table_view_label)
            btn_table__view_element = WebDriverWait(self.driver, 60).until(
                lambda driver: driver.find_element(
                    locate_with(By.XPATH, self.btn_table_view).to_right_of(
                        driver.find_element(*table_view_label_locator)
                    )
                )
            )
            btn_table__view_element.click()

        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Table View' radio button: {e}")

    # def click_on_view(self):
    #     """
    #     Clicks on the 'View' radio button in the project details section.
    #     """
    #     btn_board_view_locator = (By.XPATH, self.btn_board_view)
    #     btn_project_details_view_locator = (By.XPATH, self.btn_project_details_view)
    #     btn_comments_view_locator = (By.XPATH, self.btn_comments_view)
    #     btn_calendar_view_locator = (By.XPATH, self.btn_calendar_view)
    #     btn_activity_view_locator = (By.XPATH, self.btn_activity_view)
    #     btn_workload_view_locator = (By.XPATH, self.btn_workload_view)
    #     btn_table_view_locator = (By.XPATH, self.btn_table_view)
    #     try:
    #         webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_board_view_locator,
    #                                                    timeout=self.timeout)
    #         self.driver.find_element(*btn_board_view_locator).click()
    #
    #         webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_project_details_view_locator,
    #                                                    timeout=self.timeout)
    #         self.driver.find_element(*btn_project_details_view_locator).click()
    #
    #         webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_comments_view_locator,
    #                                                    timeout=self.timeout)
    #         self.driver.find_element(*btn_comments_view_locator).click()
    #
    #         webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_calendar_view_locator,
    #                                                    timeout=self.timeout)
    #         self.driver.find_element(*btn_calendar_view_locator).click()
    #
    #         webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_activity_view_locator,
    #                                                    timeout=self.timeout)
    #         self.driver.find_element(*btn_activity_view_locator).click()
    #
    #         webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_workload_view_locator,
    #                                                    timeout=self.timeout)
    #         self.driver.find_element(*btn_workload_view_locator).click()
    #
    #         webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=btn_table_view_locator,
    #                                                    timeout=self.timeout)
    #         self.driver.find_element(*btn_table_view_locator).click()
    #
    #     except (NoSuchElementException, TimeoutException) as e:
    #         print(f"Error clicking on 'View' radio button: {e}")

    def select_templates(self):
        """
        Selects a template from the available templates.
        """
        locator = (By.XPATH, self.option_template)
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
        self.driver.find_element(*locator).click()

    def click_on_use_template_button(self):
        """
        Clicks on the 'Use Template' button to proceed to the next step in the project creation process.
        """
        locator = (By.XPATH, self.btn_use_template)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Use Template' button: {e}")

    def click_on_create_project(self):
        """
        Clicks on the 'Create Project' button to finalize and create the new project.
        """
        locator = (By.XPATH, self.btn_create_project)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=locator,
                                                             timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Create Project' button: {e}")

    def verify_project_toast_message(self):
        """
        Verifies that the success toast message is displayed after project creation.

        :return: The text of the toast message.
        """
        toast_locator = (By.XPATH, self.toast_message_project)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator,
                                                             timeout=90)
            toast_element = self.driver.find_element(*toast_locator)
            return toast_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying project toast message: {e}")
            return None

    def verify_view_title(self):
        toast_locator = (By.XPATH, self.view_title)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator,
                                                             timeout=90)
            toast_element = self.driver.find_element(*toast_locator)
            return toast_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying project view title: {e}")
            return None

    def verify_apps_title(self):
        toast_locator = (By.XPATH, self.apps_title)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator,
                                                             timeout=90)
            toast_element = self.driver.find_element(*toast_locator)
            return toast_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying project apps title: {e}")
            return None

    def verify_custom_field_title(self):
        toast_locator = (By.XPATH, self.custom_field_title)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=toast_locator,
                                                             timeout=90)
            toast_element = self.driver.find_element(*toast_locator)
            return toast_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error verifying custom field title: {e}")
            return None

    def get_created_project_name(self):
        """
        Retrieves the name of the newly created project from the project list.

        :return: The name of the created project.
        """
        project_name_locator = (By.XPATH, self.project_name)
        try:
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=project_name_locator,
                                                             timeout=self.timeout)
            project_name_element = self.driver.find_element(*project_name_locator)
            return project_name_element.text
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error getting created project name: {e}")
            return None

    def select_created_project(self):
        """
        Clicks on the created project from the project list to open it.

        :return: The WebElement of the created project.
        """
        locator = (By.XPATH, self.project_name)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            project_element = self.driver.find_element(*locator)
            project_element.click()
            return project_element
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error selecting created project: {e}")
            return None

    def click_on_due_date(self):
        locator = (By.XPATH, self.date_picker_due_date)
        try:
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
            self.driver.find_element(*locator).click()
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Error clicking on 'Use Template' button: {e}")

    def calendar_component(self):

        locator = (By.XPATH, self.date_picker_due_date)
        webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=self.timeout)
        self.driver.find_element(*locator).click()

        cel_locator = (By.CLASS_NAME, "dp__instance_calendar")
        webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=cel_locator,
                                                         timeout=self.timeout)

        # Interact with the calendar

        next_button = self.driver.find_element(By.XPATH, "//button[@aria-label='Next month']")
        next_button.click()

        # Example: Select a specific date (30th)
        date_button = self.driver.find_element(By.XPATH,
                                               "//div[contains(@class, 'dp__calendar_item') and .//div[text()='30']]")
        date_button.click()
