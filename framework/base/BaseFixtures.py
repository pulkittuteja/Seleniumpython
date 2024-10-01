import allure
from allure_commons.types import AttachmentType
import pytest
from _pytest.reports import CollectReport
from _pytest.stash import StashKey
from typing import Dict
from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.edge.service import Service
from selenium.webdriver.ie.service import Service as IEService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.options import Options as edgeOptions
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as firefoxOptions
from selenium.webdriver.safari.options import Options as safariOptions


@pytest.fixture(autouse=False)
def setup_driver(request, browser, url):
    """
    Setup & teardown the web driver Fixture to be used in the test. This fixture is invoked automatically by pytest.
    :param request: Request object from the class or method using this fixture.
    :param browser: Browser to be used for testing
    :param url: URL of the application to be tested
    :return: driver : An object of web_driver to be used in the test
    """
    # Setup method
    global driver
    driver = ""

    match browser:
        case "chrome":
            chrome_options = chromeOptions()
            add_options(chrome_options)
            driver = webdriver.Chrome(options=chrome_options)
        case "firefox":
            firefox_options = firefoxOptions()
            add_options(firefox_options)
            driver = webdriver.Firefox(options=firefox_options)
        case "edge":
            edge_options = edgeOptions()
            add_options(edge_options)
            driver = webdriver.Edge(options=edge_options)
        case "ie":
            driver = webdriver.Ie()
        case "safari":
            safari_options = safariOptions()
            add_options(safari_options)
            driver = webdriver.Safari(options=safariOptions)
        case "chromium":
            driver = webdriver.Chrome(
                service=ChromiumService(
                    ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
                )
            )

    if url is not None:
        driver.get(url)
    pytest.driver = driver
    driver.maximize_window()
    request.cls.driver = driver

    # Teardown method
    yield
    driver.close()


def add_options(browserOption):
    # browserOption.add_argument("--headless")
    # browserOption.add_argument("--window-size=1920,1080")
    # browserOption.add_argument('--ignore-certificate-errors')
    browserOption.add_argument('--allow-running-insecure-content')
    browserOption.add_argument('--no-sandbox')
    browserOption.add_argument('--disable-dev-shm-usage')

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36  Edg/121.0.2277.113'
    browserOption.add_argument(f'user-agent={user_agent}')


def pytest_addoption(parser):
    """
    Pytest method to read custom commandline arguments
    :param parser: Parser object
    :return: void
    """
    parser.addoption(
        "--browser",
        action="store",
        default="edge",
        help="Chrome or Firefox or edge or Safari",
    )
    parser.addoption(
        "--url",
        action="store",
        default=None,
        help="Set URL to load",
    )


@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_screenshot", attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep