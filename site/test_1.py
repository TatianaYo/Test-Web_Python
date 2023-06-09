from testpage import OperationsHelper
import logging
import yaml
import time
from post import send_mail


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser):
    logging.info('Test 1 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('test')
    testpage.enter_pass('test')
    time.sleep(testdata['sleep'])
    testpage.click_login_button()
    time.sleep(testdata['sleep'])
    assert testpage.get_error_text() == '401'


def test_step2(browser):
    logging.info('Test 2 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    time.sleep(testdata['sleep'])
    testpage.click_login_button()
    time.sleep(testdata['sleep'])
    assert testpage.get_hello_user() == f'Hello, {testdata["login"]}'


def test_step3(browser):
    logging.info('Test 3 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    time.sleep(testdata['sleep'])
    testpage.click_login_button()
    time.sleep(testdata['sleep'])
    testpage.click_create_post()
    time.sleep(testdata['sleep'])
    testpage.enter_title(testdata['title'])
    testpage.enter_description(testdata['description'])
    time.sleep(testdata['sleep'])
    testpage.click_save_post()
    time.sleep(testdata['sleep'])
    assert testpage.get_new_post() == f"{testdata['title']}"


def test_step4(browser):
    logging.info('Test 4 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    time.sleep(testdata['sleep'])
    testpage.click_login_button()
    time.sleep(testdata['sleep'])
    testpage.click_contact()
    time.sleep(testdata['sleep'])
    testpage.enter_name(testdata['name'])
    testpage.enter_email(testdata['email'])
    testpage.content_enter(testdata['content_1'])
    time.sleep(testdata['sleep'])
    testpage.click_contact_us()
    time.sleep(testdata['sleep'])
    send_mail()
    assert testpage.get_alert() == testdata['alert_text']




