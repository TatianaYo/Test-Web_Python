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
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    time.sleep(testdata['sleep'])
    testpage.click_login_button()
    time.sleep(testdata['sleep'])
    assert testpage.get_hello_user() == f'Hello, {testdata["login"]}'


def test_step2(browser):
    logging.info('Test 2 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    time.sleep(testdata['sleep'])
    testpage.click_login_button()
    time.sleep(testdata['sleep'])
    testpage.click_about_link()
    time.sleep(testdata['sleep'])
    assert testpage.get_title_text_about() == testdata['title_about']


def test_step3(browser):
    logging.info('Test 3 starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata['login'])
    testpage.enter_pass(testdata['password'])
    time.sleep(testdata['sleep'])
    testpage.click_login_button()
    time.sleep(testdata['sleep'])
    testpage.click_about_link()
    time.sleep(testdata['sleep'])
    assert testpage.get_property() == '32px'
