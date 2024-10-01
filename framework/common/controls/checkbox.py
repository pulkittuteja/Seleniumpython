from framework.base.BaseControl import BaseControl
from framework.utilities.common.elementUtils import *
from framework.utilities.common.pageUtils import *


class Checkbox(BaseControl):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def get_value(self) -> str:
        """
        get the current value of checkbox element
        :return: str: Value of element in a checkbox
        """

        try:
            return self.elements[0].get_attribute("value")
        except Exception as err:
            print(f"Error in get_value: {err}")
            return None

    def set_value(self):
        """
        select the checkbox element
        """

        try:
            if not self.elements[0].is_selected():
                self.elements[0].click()
        except Exception as err:
            print(f"Error in set_value: {err}")
            return None

    def deselect_value(self):
        """
        deselect the checkbox element
        """

        try:
            if self.elements[0].is_selected():
                self.elements[0].click()
        except Exception as err:
            print(f"Error in deselect_value: {err}")
            return None

    def is_checked(self):
        """
        checks if checkbox element is selected or not
        :return: bool: True if element is selected else False
        """

        try:
            return self.elements[0].is_selected()
        except:
            return False
