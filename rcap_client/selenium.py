from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from .browser import Browser
from .solver import RecaptchaSolver
from .detector import Detector


class SeleniumBrowser(Browser):

    def __init__(self, driver: WebDriver):
        self.driver = driver


    def switch_to_frame(self, selector: str):
        self.switch_to_main_frame()
        iframe = self.find_element(selector, 10, 'present')
        self.driver.switch_to.frame(iframe)


    def switch_to_main_frame(self):
        self.driver.switch_to.default_content()


    def click(self, selector: str, timeout: float):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(
                (By.XPATH, selector)
            )
        ).click()


    def wait_for(self, selector: str, timeout: float, status: str):
        _CONDITIONS = {
            'clickable': EC.element_to_be_clickable,
            # 'visible': EC.visibility_of_element_located,
            'present': EC.presence_of_element_located,
        }

        condition = _CONDITIONS[status]

        WebDriverWait(self.driver, timeout).until(
            condition((By.XPATH, selector))
        )


    def get_attribute(self, element: WebElement, name: str):
        return element.get_attribute(name)


    def find_element(self, selector: str, timeout: float, status: str):
        _CONDITIONS = {
            # 'clickable': EC.element_to_be_clickable,
            # 'visible': EC.visibility_of_element_located,
            'present': EC.presence_of_element_located,
        }

        condition = _CONDITIONS[status]

        return WebDriverWait(self.driver, timeout).until(
            condition((By.XPATH, selector))
        )


    def find_elements(self, selector: str, timeout: float, status: str):
        _CONDITIONS = {
            'present': EC.presence_of_all_elements_located
        }

        condition = _CONDITIONS[status]

        return WebDriverWait(self.driver, timeout).until(
            condition((By.XPATH, selector))
        )


    def find_element_inside_element(self, element: WebElement, selector: str):
        return element.find_element(By.XPATH, selector)


    def get_element_text(self, element: WebElement):
        return element.text


class SeleniumRecaptchaSolver(RecaptchaSolver):

    def __init__(self, driver):
        super().__init__(
            browser=SeleniumBrowser(driver),
            detector=Detector(),
        )