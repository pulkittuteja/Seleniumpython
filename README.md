Sample Architecture for PyTest Framework
The proposed architecture is designed to provide a robust and scalable framework for automated testing of both APIs and UI applications. It integrates key testing practices, such as the Page Object Model (POM) for UI testing and Data-Driven Testing for versatile input handling

we are using the hybrid framework which will be a combination of PyTest, POM (Page Object Model) and Data driven.

Page Object Model?
Page Object Model is a design pattern where the core focus is on reducing code duplication and minimization of the effort involved in code update/maintenance. Under the Page Object Model, page classes are created for all the webpages that are a part of the Automation Under Test (AUT).
This makes the code more modular since locators/elements used by the test suites/test scenarios are stored in a separate class file & the test cases (that contain the core test logic) are in a different file. Hence, any change in the web UI elements will require minimal (or no changes) in the test scenarios since locators & test scripts are stored separately.

PyTest:
PyTest is Python based testing framework which provides flexible way to write and execute the automated tests. The key features that we are going to use of this framework are:
Fixtures, Parameterization, Assertions, markers, re-executing the failed tests etc

Data Driven testing:
This framework helps us to organize the data sets that covers different combinations to test the various scenarios along with the expected output. We are planning to include all the above frameworks together as a hybrid framework where we take the features of each of the above framework to cover end to end automation of TC+.

Framework

![Architecture](https://github.com/user-attachments/assets/12f12b1b-aa56-494c-a628-f132c94cb7b4)

The Setup:

Create new project and install required Packages/plugins.

Selenium: Selenium Libraries
Webdriver-manager: Webdriver
Python: Python Unit Test Framework
pytest-html: PyTest HTML reports
pytest-xdist: Run tests parallel
Openpyxl: MS Excel support
Allure-pytest: to generate allure reports

![Folder Structure](https://github.com/user-attachments/assets/10ab07f1-293c-4cee-9100-21aebd0e6442)

for API Automation functions

Locators->api->api_requests.py

