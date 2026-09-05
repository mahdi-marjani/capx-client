from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement

from .browser import Browser
from .solver import RecaptchaSolver
from .detector import Detector

import utils


class SeleniumBrowser(Browser):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def switch_to_frame(self, selector: str):
        utils.selenium_switch_to_iframe(self.driver, selector)

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

    def get_attribute(self, selector: str, name: str, timeout: float):
        return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(
                    (By.XPATH, selector)
                )
            ).get_attribute(name)

    def find(self, selector: str, timeout: float, status: str):
        _CONDITIONS = {
            # 'clickable': EC.element_to_be_clickable,
            # 'visible': EC.visibility_of_element_located,
            'present': EC.presence_of_element_located,
        }

        condition = _CONDITIONS[status]

        return WebDriverWait(self.driver, timeout).until(
            condition((By.XPATH, selector))
        )

    def find_text_inside_element(self, element: WebElement):
        return element.find_element(By.XPATH, ".//strong").text

    def get_element_text(self, element: WebElement):
        return element.text

    def get_captcha_image_urls(self):
        return utils.selenium_get_captcha_image_urls(self.driver)

    def get_new_dynamic_image_urls(self, answers: list, old_urls: list):
        return utils.selenium_get_new_dynamic_image_urls(answers, old_urls, self.driver)


class SeleniumRecaptchaSolver(RecaptchaSolver):

    def __init__(self, driver):
        super().__init__(
            browser=SeleniumBrowser(driver),
            detector=Detector(),
        )