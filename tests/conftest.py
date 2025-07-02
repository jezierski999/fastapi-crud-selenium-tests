import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

@pytest.fixture(scope="module")
def driver():
    """
    Provides a Firefox WebDriver instance for the test module.
    - Uses the geckodriver path for Termux/Linux
    - Opens the test web application before tests
    - Closes the browser after all tests in the module
    """
    service = Service(executable_path="/data/data/com.termux/files/usr/bin/geckodriver")
    options = webdriver.FirefoxOptions()
    # Uncomment the next line to run tests without opening the browser window
    # options.add_argument('--headless')
    
    driver = webdriver.Firefox(service=service)  # GUI mode
    # driver = webdriver.Firefox(service=service, options=options)  # headless mode

    driver.get("http://192.168.1.254:8080/")
    yield driver
    driver.quit()
