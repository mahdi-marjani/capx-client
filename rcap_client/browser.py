from abc import ABC, abstractmethod


class Browser(ABC):

    @abstractmethod
    def find(self, selector: str, timeout: float, status: str):
        ...

    @abstractmethod
    def find_text_inside_element(self, element):
        ...

    @abstractmethod
    def get_element_text(self, element):
        ...

    @abstractmethod
    def click(self, selector: str, timeout: float):
        ...

    @abstractmethod
    def get_attribute(self, selector: str, name: str, timeout: float):
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

    @abstractmethod
    def get_captcha_image_urls(self):
        ...

    @abstractmethod
    def get_new_dynamic_image_urls(self, answers: list, old_urls: list):
        ...