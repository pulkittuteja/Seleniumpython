from selenium.webdriver.support.ui import Select
from framework.base.BaseControl import BaseControl
from framework.utilities.common.elementUtils import *
from framework.utilities.common.pageUtils import *


class Dropdown(BaseControl):
    def __init__(self, driver, locator):
        super().__init__(driver, locator)

    def get_value(self) -> str:
        """
        get the current value of dropdown element
        :return: str: Value of element in a dropdown
        """

        try:
            # GET_VALUE= Select(self.elements[0].get_attribute("value"))
            # options = GET_VALUE.options
            # for option in options:
            #     return option.get_attribute("value")
            return self.elements[0].text
        except Exception as err:
            print(f"Error in get_value: {err}")
            return None

    def get_options_startswith(self, value):
        """
        get the list of options from dropdown element that starts with a specific alphabet
        :param: value: value by which we will get a list of options
        return: list: list of elements in a dropdown
        """

        try:
            dropdown = Select(self.elements[0].get_attribute("value"))
            dropdown.click()
            options = dropdown.options
            list_of_options = [
                option.get_attribute("value")
                for option in options
                if option.get_attribute("value").startswith(value)
            ]
            return list_of_options
        except Exception as err:
            print(f"Error in get_options_startswith: {err}")
            return None

    def set_value(self, locator, time_out_in_sec):
        """
        set the value of dropdown element
        :param: locator: refers to the locator type and value
        :param: time_out_in_sec: time in sec after which exception will be thrown
        """

        try:
            self.elements[0].click()
            click(locator, time_out_in_sec)
        except Exception as err:
            print(f"Error in set_value: {err}")
            return None

    def set_value_select(self, value, selection_type):
        """
        set the value of dropdown element using Select class
        :param: value: value of the element
        :param: selection_type: defines type of selection which includes- by value,by index and by visible text
        """

        try:
            dropdown = Select(self.elements[0])
            print(dropdown)

            if selection_type == "by_value":
                dropdown.select_by_value(value)
            elif selection_type == "by_index":
                dropdown.select_by_index(value)
            elif selection_type == "by_visible_text":
                dropdown.select_by_visible_text(value)
        except Exception as err:
            print(f"Error in set_value_select: {err}")
            return None

    def is_enabled(self):
        """
        checks if dropdown element is enabled or not
        :param: locator: refers to the locator details
        :param: time_out_in_sec: time in sec after which exception will be thrown
        :return: bool: True if dropdown is enabled else False
        """

        try:
            return self.elements[0].is_enabled()
        except:
            return False
