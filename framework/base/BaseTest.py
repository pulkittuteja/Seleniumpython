import pytest


@pytest.mark.usefixtures("setup_driver", "log_on_failure")
class BaseTest:
    pass