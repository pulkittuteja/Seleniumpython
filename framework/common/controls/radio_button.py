from framework.base.BaseControl import BaseControl
from framework.utilities.common.elementUtils import *
from framework.utilities.common.pageUtils import *


class RadioButton(BaseControl):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def get_value(self) -> str:
        """
        get the current value of radio button
        :return: str: Value of element in a dropdown
        """

        try:
            self.elements
            for radioButtons in self.elements:
                if radioButtons.is_selected():
                    return radioButtons.get_attribute("value")
        except Exception as err:
            print(f"Error in get_value: {err}")
            return None

    def set_value(self, value, selection_type):
        """
        set the value of radio button
        :param: value: value of the element
        :param: selection_type: defines type of selection which includes- by value, by index and by visible text
        """

        try:
            radio_buttons = self.elements
            if selection_type == "by_value":
                for radioButtons in radio_buttons:
                    if radioButtons.get_attribute("value") == value:
                        radioButtons.click()
            elif selection_type == "by_index":
                if value < len(radio_buttons) and value >= 0:
                    radio_buttons[value].click()
        except Exception as err:
            print(f"Error in set_value of radio button: {err}")
            return None

    def is_enabled(self, locator, time_out_in_seconds):
        """
        checks if radio button element is enabled or not
        :param: locator: refers to the locator details
        :param: time_out_in_sec: time in sec after which exception will be thrown
        :return: bool: True if radio button is enabled else False
        """

        try:
            element = wait_for_all_elements(locator, time_out_in_seconds)
            return element.is_enabled()
        except:
            return False