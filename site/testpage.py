from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.CSS_SELECTOR, """button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_HELLO_USER = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[3]/a""")
    LOCATOR_CREATE_POST_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_BTN_SAVE_POST = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_TITLE_TEXT = (By.XPATH, """//*[@id="app"]/main/div/div[1]/h1""")
    LOCATOR_CONTACT = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_YOUR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    def enter_login(self, word):
        logging.info(f'Send "{word}" to element')
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f'Send "{word}" to element')
        pass_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        pass_field.clear()
        pass_field.send_keys(word)

    def click_login_button(self):
        logging.info('Click login button')
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        text = error_field.text
        logging.info(f'We find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}')
        return text

    def get_hello_user(self):
        hello_user_field = self.find_element(TestSearchLocators.LOCATOR_HELLO_USER, time=5)
        text = hello_user_field.text
        return text

    def click_create_post(self):
        logging.info('Click create post button')
        self.find_element(TestSearchLocators.LOCATOR_CREATE_POST_BTN, time=5).click()

    def enter_title(self, text):
        title_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        title_field.clear()
        title_field.send_keys(text)

    def enter_description(self, text):
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(text)

    def enter_content(self, text):
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(text)

    def click_save_post(self):
        logging.info('Click save post button')
        self.find_element(TestSearchLocators.LOCATOR_BTN_SAVE_POST).click()

    def get_new_post(self):
        logging.info('Search locator')
        post_title = self.find_element(TestSearchLocators.LOCATOR_TITLE_TEXT, time=7)
        return post_title.text

    def click_contact(self):
        logging.info('Click contact')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT, time=5).click()

    def enter_name(self, text):
        name_field = self.find_element(TestSearchLocators.LOCATOR_YOUR_NAME_FIELD)
        name_field.clear()
        name_field.send_keys(text)

    def enter_email(self, text):
        email_field = self.find_element(TestSearchLocators.LOCATOR_EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(text)

    def content_enter(self, text):
        field_content = self.find_element(TestSearchLocators.LOCATOR_CONTENT)
        field_content.clear()
        field_content.send_keys(text)

    def click_contact_us(self):
        logging.info('Click contact us button')
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN, time=5).click()

    def get_alert(self):
        alert = self.driver.switch_to.alert
        return alert.text










