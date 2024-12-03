from selenium.webdriver.common.by import By
from utils.common_utils import *
from selenium.webdriver.support.wait import WebDriverWait
import time


class TestVerifyGmailAccount:

    def test_login_with_valid_credentials(self, setup):

        self.driver = setup
        self.driver.get(
            "https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=Ab5oB3pupTMhWiu10mKVmBgJWDdMbzXRYQAqoRtLpVWVuqgTIdlfn03N7F8JxbWPbUsjmiNP0Ux_&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-1154018585%3A1725791482059509&ddm=0")
        self.driver.maximize_window()

        try:

            # Step 1: Navigate to Gmail login page
            locator = (By.XPATH, "//span[normalize-space()='Sign in']")
            webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=locator, timeout=60)

            # Enter email
            email_input = self.driver.find_element(By.XPATH, '//*[@id="identifierId"]')
            email_input.send_keys('vimalpatel888999@gmail.com')

            next_button_locator = self.driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=locator, timeout=60)
            next_button_locator.click()

            locator = (By.XPATH, "//span[normalize-space()='Welcome']")
            webdriver_wait_for_text_in_element(driver=self.driver, locator=locator, text="Welcome", timeout=60)

            password_input = self.driver.find_element(By.XPATH, '//*[@name="Passwd"]')
            password_input.send_keys('Abc@223133')  # Replace with your password

            time.sleep(20)

            next_locator = self.driver.find_element(By.XPATH, "//span[normalize-space()='Next']")
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=next_locator, timeout=60)
            next_locator.click()

            # Step 2: Wait for the page to load and the search box to be visible
            search_box = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Search mail']"))
            )

            # Step 3: Enter the search query for a specific subject
            subject = "Alian Hub have sent you an invitation"  # Replace with the subject you want to search for
            search_box.send_keys(f'subject:"{subject}"')

            # Step 4: Click the search button (or press Enter)
            search_box.send_keys(u'\ue007')  # Press Enter to trigger the search

            # Step 5: Wait for the results to load
            WebDriverWait(self.driver, 60).until(
                EC.presence_of_element_located((By.XPATH, "//tr[@role='row']"))
            )

            # Step 6: Interact with the search results (e.g., click on the first email)
            first_email = self.driver.find_element(By.XPATH, "//tr[@role='row'][1]")
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=first_email, timeout=60)
            first_email.click()

            # email_row = self.driver.find_element(By.XPATH,
            #                                      "//tr[td//span[text()='noreply'] and td//span[contains(text(), 'Alian Hub have sent you an invitation')]]")
            # webdriver_wait_for_visibility_of_element_located(driver=self.driver, element_tuple=email_row, timeout=60)
            # email_row.click()
            #
            # time.sleep(40)
            #
            # join_button = self.driver.find_element(By.XPATH, "//a[normalize-space()='Click here to Join']")
            # webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=join_button, timeout=60)
            # join_button.click()

            time.sleep(25)

            main_window = self.driver.current_window_handle

            # Get all window handles (tabs)
            WebDriverWait(self.driver, 20).until(lambda d: len(self.driver.window_handles) > 1)
            all_windows = self.driver.window_handles

            # Switch to the new tab (which is the last in the list)
            for window in all_windows:
                if window != main_window:
                    self.driver.switch_to.window(window)
                    break

            # Now you are in the new tab, wait for the content to load (if needed)
            WebDriverWait(self.driver, 60).until(EC.title_contains("Alian Hub | Register"))
            print("New tab title: ", self.driver.title)

            first_name = self.driver.find_element(By.XPATH, "//input[@id='firstName']")
            first_name.send_keys("Vimal")

            last_name = self.driver.find_element(By.XPATH, "//input[@id='lastName']")
            last_name.send_keys("Patel")

            password = self.driver.find_element(By.XPATH, "//input[@id='password']")
            password.send_keys("Abc123456*")

            confirm_password = self.driver.find_element(By.XPATH, "//input[@id='confirmPassword']")
            confirm_password.send_keys("Abc123456*")

            checkbox = WebDriverWait(self.driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'I agree to the')]"))
            )
            checkbox.click()

            register_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Register']")
            webdriver_wait_for_element_to_be_clickable(driver=self.driver, locator=register_button, timeout=60)
            register_button.click()

            time.sleep(60)

            # Step 6: After interacting with the new tab, you can close it or switch back
            self.driver.close()  # Close the new tab

            # Switch back to the original tab
            self.driver.switch_to.window(main_window)
            print("Switched back to the original tab.")

        finally:
            # Close the browser window after done
            self.driver.quit()
