from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def find_element(self, selector: str, timeout: float, status: str):
        ...

    @abstractmethod
    def find_elements(self, selector: str, timeout: float, status: str):
        ...

    @abstractmethod
    def find_element_inside_element(self, element, selector: str):
        ...

    @abstractmethod
    def get_element_text(self, element):
        ...

    @abstractmethod
    def click(self, selector: str, timeout: float):
        ...

    @abstractmethod
    def get_attribute(self, element, name: str):
        ...

    @abstractmethod
    def switch_to_frame(self, selector: str):
        ...

    @abstractmethod
    def switch_to_main_frame(self):
        ...

    @abstractmethod
    def wait_for(self, selector: str, timeout: float, status: str):
        ...
