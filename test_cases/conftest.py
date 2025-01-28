import pytest
import tempfile
import shutil
from _pytest.config import hookimpl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options globally for regular (non-headless) mode
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")  # Ensure the browser window is maximized
chrome_options.add_argument("--disable-extensions")
# Remove --headless argument for UI visibility
# chrome_options.add_argument("--headless")  # Commented out to show UI
chrome_options.add_argument("--no-sandbox")  # Disable sandbox (required for some environments like Docker)
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
chrome_options.add_argument("--remote-debugging-port=9222")  # Remote debugging port
chrome_options.add_argument("--disable-dev-shm-usage")  # Helps to avoid "DevToolsActivePort file doesn't exist" error
chrome_options.add_argument("--disable-software-rasterizer")  # Avoid issues related to software rasterizer

# Handle Chrome prefs for notifications and media
chrome_options.add_experimental_option(
    "prefs", {
        "profile.default_content_setting_values.notifications": 1,
        "profile.default_content_setting_values.media_stream_mic": 1,
        "profile.default_content_setting_values.media_stream_camera": 1,
        "profile.default_content_setting_values.geolocation": 1
    }
)


# Fixture to set up and configure browser (chrome or firefox)
@pytest.fixture(scope="function")
def setup(browser, request):
    if browser == 'chrome':
        # Create a temporary directory for user data to avoid session conflicts
        user_data_dir = tempfile.mkdtemp()  # Generates a unique temp directory
        chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

        # Initialize Chrome WebDriver with the options
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching chrome browser with UI.........")

        # Cleanup temporary user data directory after test run
        def cleanup():
            shutil.rmtree(user_data_dir)
            print(f"Cleaned up temp directory {user_data_dir}")

        # Ensure cleanup is done after test completes
        request.addfinalizer(cleanup)

    elif browser == 'firefox':
        driver = webdriver.Firefox(options=chrome_options)  # Add regular (non-headless) options for Firefox if needed
        print("Launching firefox browser with UI.........")

    else:
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching default browser (chrome) with UI.........")

    yield driver
    driver.quit()


# Function to add browser option to the pytest command line
def pytest_addoption(parser):
    parser.addoption("--test-browser", action="store", default="chrome",
                     help="Type in browser name e.g. chrome OR firefox")


# Fixture to fetch the browser argument passed in the pytest command line
@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--test-browser")


# Pytest HTML Report
# Hook for adding environment info to HTML report
@hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
