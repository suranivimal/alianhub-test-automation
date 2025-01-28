import pytest
import tempfile
from _pytest.config import hookimpl
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configure Chrome options globally
chrome_options = Options()
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--disable-extensions")
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
def setup(browser):
    if browser == 'chrome':
        # Create a temporary directory for user data to avoid session conflicts
        user_data_dir = tempfile.mkdtemp()  # Generates a unique temp directory
        chrome_options.add_argument(f'--user-data-dir={user_data_dir}')

        # Initialize Chrome WebDriver with the options
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching chrome browser.........")

    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")

    else:
        driver = webdriver.Chrome(options=chrome_options)
        print("Launching default browser (chrome).........")

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
