import uuid

import allure
import pytest
from page_objects.create_project import CreateProject
from page_objects.create_task import CreateTask
from page_objects.dashboard import Dashboard
from utils.custom_logger import LogGen
from utils.read_properties import ReadConfig
from utils.login_manager import LoginManager


class TestCreateTask:
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    projectname = ReadConfig.get_project_name()
    logger = LogGen.loggen()

    @allure.epic("Alian Hub Create Task Test")
    @allure.feature("TC#01 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_create_task(self, setup):
        self.logger.info("***** Testing Create Task *****")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        try:

            # Login
            login_manager = LoginManager(self.driver, self.username, self.password)
            login_manager.login()
            self.logger.info("Logged in successfully.")

            # Dashboard
            dashboard = Dashboard(self.driver)
            dashboard.click_on_projects_nav()

            # Navigate to Project and Task sections
            create_project = CreateProject(self.driver)
            create_project.wait_for_project_list_fav()

            self.logger.info("Navigated to the Projects section.")

            create_project.select_created_project()
            self.logger.info(f"Selected project: {self.projectname}")

            # Verify navigation
            assert self.driver.title == "Alian Hub | Projects", f"Unexpected title: {self.driver.title}"
            self.logger.info("Project page title verified.")

            # Create Task
            create_task = CreateTask(self.driver)
            create_task.click_on_new_task_button()

            task_name = f"Task_{uuid.uuid4().hex[:6]}"  # Dynamic task name
            create_task.set_task_name(task_name)

            create_task.click_on_task_save_button()
            create_task.verify_task_toast_message()
            self.logger.info(f"Task '{task_name}' created successfully.")

            self.driver.refresh()

            # Verify task creation
            verified_task_name = create_task.verify_task_name(task_name)
            self.logger.info(f"Verified task name: {verified_task_name}")
            assert verified_task_name == task_name, f"Expected task name '{task_name}' but got '{verified_task_name}'"

        except Exception as e:
            self.logger.error(f"Test failed: {str(e)}")
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot",
                          attachment_type=allure.attachment_type.PNG)
            raise e
