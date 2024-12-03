from page_objects.login_page import LoginPage


class LoginManager:
    def __init__(self, driver, username, password):
        self.driver = driver
        self.username = username
        self.password = password
        self.login_page = LoginPage(driver)

    def login(self):
        self.login_page.set_email_id(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_on_login_button()
        self.login_page.wait_for_home_page()
