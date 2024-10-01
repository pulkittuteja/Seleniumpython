from framework.base.BaseControl import BaseControl
from framework.utilities.common.elementUtils import *
from framework.utilities.common.pageUtils import *


class TextField(BaseControl):
    def get_value(self) -> str:
        """
        get the current value of textbox element
        :return: str: Value of element in a textbox
        """

        try:
            return self.elements[0].get_attribute("value")
        except Exception as err:
            print(f"Error in get_value: {err}")
            return None

    def set_value(self, value):
        """
        set the value in textbox element
        :param: value: Value of the element
        """

        try:
            self.elements[0].clear()
            self.elements[0].send_keys(value)
        except Exception as err:
            print(f"Error in set_value: {err}")
            return None

    def is_enabled(self, locator, time_out_in_seconds):
        """
        checks if element is enabled or not
        :param: locator: refers to the locator details
        :param: time_out_in_sec: time in sec after which exception will be thrown
        :return : bool: True if the element is enabled else False
        """
        try:
            element = wait_for_all_elements(locator, time_out_in_seconds)
            return element.is_enabled()
        except:
            return False