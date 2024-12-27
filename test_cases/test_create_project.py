import time
import uuid
import allure
import pytest
from page_objects.create_project import CreateProject
from page_objects.dashboard import Dashboard
from utils.login_manager import LoginManager
from utils.read_properties import ReadConfig
from utils.custom_logger import LogGen
from utils.common_utils import capture_screenshot


def generate_project_name(base_name="Project Test"):
    unique_id = uuid.uuid4().hex[:8].capitalize()  # Generate a unique identifier
    return f"{base_name} {unique_id}"


def generate_project_key(base_key="PROJ"):
    unique_id = uuid.uuid4().hex[:8].upper()  # Generate a unique identifier (uppercase)
    return f"{base_key}-{unique_id}"


class TestCreateProject:
    baseUrl = ReadConfig.get_application_url()
    username = ReadConfig.get_user_email()
    password = ReadConfig.get_user_password()
    logger = LogGen.loggen()

    # @allure.epic("Alian Hub Create Project Using Blank Project")
    # @allure.feature("TC#01 - Alian Hub Positive Test")
    # @pytest.mark.positive
    # def test_create_project_blank_project_with_required_field(self, setup):
    #     self.logger.info("***** Testing Create Project using blank project with required fields only *****")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.driver.maximize_window()
    #
    #     try:
    #
    #         # Login
    #         login_manager = LoginManager(self.driver, self.username, self.password)
    #         login_manager.login()
    #         self.logger.info("Logged in successfully.")
    #
    #         # Dashboard
    #         dashboard = Dashboard(self.driver)
    #         dashboard.click_on_projects_nav()
    #
    #         # Create Project
    #         create_project = CreateProject(self.driver)
    #         create_project.wait_for_project_list_fav()
    #         create_project.click_on_new_project_button()
    #
    #         self.logger.info("Step-1: Project Type - Blank Project or Use a Template")
    #         create_project.click_on_blank_project_button()
    #
    #         self.logger.info("Step-2: Project Detail")
    #         self.projectname = generate_project_name()
    #         self.projectkey = generate_project_key()
    #         self.logger.info(f"Generated project name: {self.projectname}, project key: {self.projectkey}")
    #
    #         create_project.set_project_name(self.projectname)
    #         create_project.set_project_key(self.projectkey)
    #         create_project.click_on_category_dropdown()
    #         create_project.select_category()
    #         create_project.click_on_next_button()
    #
    #         self.logger.info("Step-3: Project Avatar or Project Color")
    #         create_project.click_on_next_button()
    #
    #         self.logger.info("Step-4: Project Type - Public Project or Private Project")
    #         create_project.click_on_next_button()
    #
    #         self.logger.info("Step-5: Task Type - Add the type of tasks you need")
    #         create_project.click_on_next_button()
    #
    #         self.logger.info("Step-6: Project Status - Add the statuses for the project")
    #         create_project.click_on_next_button()
    #
    #         self.logger.info("Step-7: Task Status - Set up the statuses for tasks")
    #         create_project.click_on_next_button()
    #
    #         self.logger.info(
    #             "Step-8: Enable Apps - Priority, Multiple Assignees, Time Estimate, Milestones, Tags, Custom Fields, Time Tracking, and AI")
    #         create_project.click_on_next_button()
    #
    #         self.logger.info(
    #             "Step-9: Enable Views - List, Board, Project Details, Comments, Calendar, Activity, Workload, and Table")
    #         # create_project.click_on_view_radio_button()
    #         create_project.click_on_next_button()
    #
    #         self.logger.info("Step-10: Project Summary - Details of the Project setup")
    #         create_project.click_on_create_project()
    #         toast_message = create_project.verify_project_toast_message()
    #         self.logger.info(f"Toast message: {toast_message}")
    #         capture_screenshot(self.driver, "project_created_successfully")
    #         allure.attach(self.driver.get_screenshot_as_png(), name='Project Created Successfully')
    #
    #         self.driver.refresh()
    #
    #         # Verify the project name
    #         created_project_name = create_project.get_created_project_name()
    #         assert created_project_name == self.projectname, f"Project name mismatch. Expected: {self.projectname}, Found: {created_project_name}"
    #
    #     except Exception as e:
    #         self.logger.error(f"An error occurred: {str(e)}")
    #         capture_screenshot(self.driver, "test_create_project_name_verification_failed")
    #         allure.attach(self.driver.get_screenshot_as_png(), name='Create Project Error')
    #         assert False
    #
    # @allure.epic("Alian Hub Create Project Using a Template")
    # @allure.feature("TC#02- Alian Hub Positive Test")
    # @pytest.mark.positive
    # def test_create_project_using_template_with_required_field(self, setup):
    #     self.logger.info("***** Testing Create Project using template with required fields only *****")
    #     self.driver = setup
    #     self.driver.get(self.baseUrl)
    #     self.driver.maximize_window()
    #
    #     try:
    #
    #         # Login
    #         login_manager = LoginManager(self.driver, self.username, self.password)
    #         login_manager.login()
    #         self.logger.info("Logged in successfully.")
    #
    #         # Dashboard
    #         dashboard = Dashboard(self.driver)
    #         dashboard.click_on_projects_nav()
    #
    #         # Create Project using Template
    #         create_project = CreateProject(self.driver)
    #         create_project.wait_for_project_list_fav()
    #         create_project.click_on_new_project_button()
    #         create_project.click_on_use_a_template_button()
    #
    #         # Select Template and Set Project Details
    #         create_project.select_templates()
    #         create_project.click_on_use_template_button()
    #
    #         self.projectname = generate_project_name()
    #         self.projectkey = generate_project_key()
    #         self.logger.info(f"Generated project name: {self.projectname}, project key: {self.projectkey}")
    #
    #         create_project.set_project_name(self.projectname)
    #         create_project.set_project_key(self.projectkey)
    #
    #         create_project.click_on_category_dropdown()
    #         create_project.select_category()
    #
    #         time.sleep(25)
    #         create_project.click_on_create_project()
    #
    #         # Verify Toast Message and Refresh
    #         toast_message = create_project.verify_project_toast_message()
    #         self.logger.info(f"Toast message: {toast_message}")
    #         capture_screenshot(self.driver, "project_created_successfully")
    #         allure.attach(self.driver.get_screenshot_as_png(), name='Project Created Successfully')
    #
    #         self.driver.refresh()
    #
    #         # Verify the project name
    #         created_project_name = create_project.get_created_project_name()
    #         assert created_project_name == self.projectname, f"Project name mismatch. Expected: {self.projectname}, Found: {created_project_name}"
    #         self.logger.info("Project name verification testcase passed")
    #         allure.attach(self.driver.get_screenshot_as_png(), name='Test Create Project Name Verification Passed')
    #
    #     except Exception as e:
    #         self.logger.error(f"An error occurred: {str(e)}")
    #         capture_screenshot(self.driver, "test_create_project_name_verification_failed")
    #         allure.attach(self.driver.get_screenshot_as_png(), name='Create Project Error')
    #         assert False

    @allure.epic("Alian Hub Create Project Using Blank Project with all fields")
    @allure.feature("TC#03 - Alian Hub Positive Test")
    @pytest.mark.positive
    def test_create_project_blank_project_with_all_field(self, setup):
        self.logger.info("***** Testing Create Project using blank project with all fields *****")
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

            # Create Project
            create_project = CreateProject(self.driver)
            create_project.wait_for_project_list_fav()
            create_project.click_on_new_project_button()

            self.logger.info("Step-1: Project Type - Blank Project or Use a Template")
            create_project.click_on_blank_project_button()

            self.logger.info("Step-2: Project Detail")
            self.projectname = generate_project_name()
            self.projectkey = generate_project_key()
            self.logger.info(f"Generated project name: {self.projectname}, project key: {self.projectkey}")

            create_project.set_project_name(self.projectname)
            create_project.set_project_key(self.projectkey)
            create_project.click_on_category_dropdown()
            create_project.select_category()
            create_project.calendar_component()
            create_project.click_on_lead_dropdown()
            create_project.select_assignee()
            create_project.close_assignee_sidebar()
            create_project.click_on_next_button()

            self.logger.info("Step-3: Project Avatar or Project Color")
            create_project.project_image_upload()
            create_project.click_on_next_button()

            self.logger.info("Step-4: Project Type - Public Project or Private Project")
            create_project.select_project_type()
            create_project.click_on_next_button()

            self.logger.info("Step-5: Task Type - Add the type of tasks you need")
            create_project.select_task_type_template()
            create_project.click_on_next_button()

            self.logger.info("Step-6: Project Status - Add the statuses for the project")
            create_project.select_project_status_template()
            create_project.click_on_next_button()

            self.logger.info("Step-7: Task Status - Set up the statuses for tasks")
            create_project.select_task_status_template()
            create_project.click_on_next_button()

            self.logger.info(
                "Step-8: Enable Apps - Priority, Multiple Assignees, Time Estimate, Milestones, Tags, Custom Fields, Time Tracking, and AI")
            create_project.click_on_enable_apps()
            create_project.click_on_next_button()

            self.logger.info("Step-9: Custom Field")
            create_project.click_on_add_custom_field()
            create_project.click_on_next_button()

            self.logger.info(
                "Step-10: Enable Views - List, Board, Project Details, Comments, Calendar, Activity, Workload, and Table")
            create_project.verify_view_title()
            create_project.click_on_board_view()
            create_project.click_on_project_details_view()
            create_project.click_on_comments_view()
            create_project.click_on_calendar_view()
            create_project.click_on_activity_view()
            create_project.click_on_workload_view()
            create_project.click_on_table_view()
            create_project.click_on_next_button()

            self.logger.info("Step-10: Project Summary - Details of the Project setup")
            create_project.click_on_create_project()
            toast_message = create_project.verify_project_toast_message()
            self.logger.info(f"Toast message: {toast_message}")
            capture_screenshot(self.driver, "project_created_successfully")
            allure.attach(self.driver.get_screenshot_as_png(), name='Project Created Successfully')

            self.driver.refresh()

            # Verify the project name
            created_project_name = create_project.get_created_project_name()
            assert created_project_name == self.projectname, f"Project name mismatch. Expected: {self.projectname}, Found: {created_project_name}"

        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            capture_screenshot(self.driver, "test_create_project_name_verification_failed")
            allure.attach(self.driver.get_screenshot_as_png(), name='Create Project Error')
            assert False
