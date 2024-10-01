from framework.base.BaseControl import BaseControl
from framework.utilities.common.elementUtils import *
from framework.utilities.common.pageUtils import *
from selenium.webdriver.support.ui import Select


class MultiSelect(BaseControl):
    def get_value(self):
        """
        get the value of multi select element
        :return: list: list of selected values
        """

        try:
            select_element = Select(self.elements[0])
            selected_values = []
            for option in select_element.all_selected_options:
                selected_values.append(option.get_attribute("value"))
            return selected_values
        except Exception as err:
            print(f"Error in get_value: {err}")
            return None

    def set_value(self, value, selection_type):
        """
        set the value of multi select element
        :param: value: value of the multi select element
        :param: selection_type: defines the selection type which includes- by value, by index and by visible text
        """

        try:
            multi_select = Select(self.elements[0])

            if selection_type == "by_value":
                multi_select.select_by_value(value)
            elif selection_type == "by_index":
                multi_select.select_by_index(value)
            elif selection_type == "by_visible_text":
                multi_select.select_by_visible_text(value)
            else:
                raise ValueError("Invalid selection type: {}".format(selection_type))
        except Exception as err:
            print(f"Error in set_value: {err}")
            return None

    def deselect(self, value, selection_type):
        """
        deselect pre-selected options from a Multi-select element using the different deselect methods
        :param: value: value of the multi select element
        :param: selection_type: defines the selection type which includes- all, by value, by index and by visible text
        """

        try:
            deselect_element = Select(self.elements[0])

            if selection_type == "all":
                deselect_element.deselect_all()
            elif selection_type == "by_value":
                deselect_element.deselect_by_value(value)
            elif selection_type == "by_index":
                deselect_element.deselect_by_index(value)
            elif selection_type == "by_visible_text":
                deselect_element.deselect_by_visible_text(value)
            else:
                raise ValueError("Invalid selection type: {}".format(selection_type))
        except Exception as err:
            print(f"Error in deselect: {err}")
            return None

    def is_multi_select(self):
        """
        checks if element supports multi select or not
        :return: bool: True if element is multi select else False
        """

        try:
            ms = Select(self.elements[0])
            return ms.is_multiple
        except Exception as err:
            print(f"Error in is_multi_select: {err}")
            return None

    def all_selected_options(self):
        """
        get all selected options
        :return: list of selected options
        """

        try:
            all_options = Select(self.elements[0])
            return all_options.all_selected_options()
        except Exception as err:
            print(f"Error in all_selected_options: {err}")
            return None