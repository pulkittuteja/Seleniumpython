from framework.utilities import jsonUtils as rj
import os



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.locator = self.get_locator(self.__class__.__name__)

    def get_locator(self, file_name):
        """
        This function is used to get the path of the locator
        :param: file_name: name of the file
        :return: locator path
        """
        try:
            root_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath((__file__)))))
            locator_path = os.path.join(root_dir + "/locators/" + file_name + '.json')
            locator = rj.read_json(locator_path)
            return locator
        except FileNotFoundError:
             print("File not found: " + str(file_name))
             return None