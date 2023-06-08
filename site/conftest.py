import pytest, yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager


with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture()
def browser():
    if browser == 'firefox':
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

#
# @pytest.fixture()
# def btn_add_post():
#     return """//*[@id="create-btn"]"""
#
#
# @pytest.fixture()
# def post_title():
#     return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""
#
#
# @pytest.fixture()
# def post_description():
#     return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""
#
#
# @pytest.fixture()
# def post_content():
#     return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""
#
#
# @pytest.fixture()
# def btn_save():
#     return """//*[@id="create-item"]/div/div/div[7]/div/button"""
#
#
# @pytest.fixture()
# def title():
#     return """//*[@id="app"]/main/div/div[1]/h1"""