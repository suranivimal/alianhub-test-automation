import pytest
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


@pytest.fixture(scope="function")
def setup(browser):
    if browser == 'chrome':
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


def pytest_addoption(parser):
    parser.addoption("--test-browser", action="store", default="chrome",
                     help="Type in browser name e.g. chrome OR firefox")


@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--test-browser")


# Pytest HTML Report
# Hook for adding environment info to HTML report
@hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugin", None)
