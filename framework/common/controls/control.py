import abc
from framework.common.form.input_mode import InputMode


# The 'abc' module in the Python library provides the infrastructure for defining custom abstract base classes


class ControlInterface(abc.ABC):
    """
    The ControlInterface class is an abstract base class
    that defines the interface for controlling an input device.
    """

    @abc.abstractmethod
    def get_value(self) -> any:
        pass

    @abc.abstractmethod
    def set_value(self, value: any, mode: InputMode) -> any:
        pass
