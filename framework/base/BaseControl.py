from abc import ABC
from framework.common.form.controls.Control import ControlInterface
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from framework.utilities.common.elementUtils import *


class BaseControl(ControlInterface, ABC):
    """
    The BaseControl class provides a base implementation for controlling an input device.
    Any subclass extending this class can use these instance variables to interact with the input device.
    """

    def __init__(self, driver, locator):
        self.elements = get_elements_when_visible(locator)