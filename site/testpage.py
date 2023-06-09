from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml
import requests


class TestSearchLocators:
    ids = dict()
    with open('./locators.yaml') as f:
        locators = yaml.safe_load(f)
    for locator in locators['xpath'].keys():
        ids[locator] = (By.XPATH, locators['xpath'][locator])
    for locator in locators['css'].keys():
        ids[locator] = (By.CSS_SELECTOR, locators['css'][locator])


class OperationsHelper(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.requests = None

    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f'Send "{word}" to element {element_name}')
        field = self.find_element(locator)
        if not field:
            logging.error(f'Element {locator} not found')
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f'Exception while operate with {locator}')
            return False
        return True

    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=2)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f'Exception while get text from {element_name}')
            return None
        logging.info(f'We find text {text} in field {element_name}')
        return text

    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception('Exception with click')
            return False
        logging.info(f'Clicked {element_name} button')
        return True

# ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_LOGIN_FIELD'], word, description='login form')

    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_PASS_FIELD'], word, description='password form')

    def enter_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE_FIELD'], word, description='title form')

    def enter_description(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_DESCRIPTION_FIELD'], word,
                                   description='description form')

    def enter_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_TITLE_FIELD'], word, description='content form')

    def enter_name(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_YOUR_NAME_FIELD'], word, description='contact name')

    def enter_email(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_EMAIL_FIELD'], word, description='contact email')

    def content_enter(self, word):
        self.enter_text_into_field(TestSearchLocators.ids['LOCATOR_YOUR_NAME_FIELD'], word,
                                   description='contact content')

# CLICK
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_LOGIN_BTN'], description='button login')

    def click_create_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CREATE_POST_BTN'], description='button create post')

    def click_save_post(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_BTN_SAVE_POST'], description='button save post')

    def click_contact(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT'], description='click contact')

    def click_contact_us(self):
        self.click_button(TestSearchLocators.ids['LOCATOR_CONTACT_US_BTN'], description='button contact us')

# GET TEXT
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_ERROR_FIELD'], description='error label')

    def get_hello_user(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_HELLO_USER'], description='username')

    def get_new_post(self):
        return self.get_text_from_element(TestSearchLocators.ids['LOCATOR_TITLE_TEXT'], description='title text')

    def get_alert(self):
        logging.info('Get alert text')
        text = self.get_alert_text()
        logging.info(text)
        return text








