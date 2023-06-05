import yaml
from module import Site
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_step1(x_selector1, x_selector2, btn_selector, x_selector3, result):
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == result


def test_step2(x_selector1, x_selector2, btn_selector, x_selector3, login_user):
    input1 = site.find_element("xpath", x_selector1)
    input1.clear()
    input1.send_keys(testdata['login'])
    input2 = site.find_element("xpath", x_selector2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn = site.find_element("css", btn_selector)
    btn.click()
    element = site.find_element("xpath", login_user)
    assert element.text == f"Hello, {testdata['login']}"


def test_step3(btn_add_post, post_title, post_description, post_content, btn_save, title):
    btn1 = site.find_element("xpath", btn_add_post)
    btn1.click()
    input1 = site.find_element('xpath', post_title)
    input1.send_keys(testdata['title'])
    input2 = site.find_element('xpath', post_description)
    input2.send_keys(testdata['description'])
    input3 = site.find_element('xpath', post_content)
    input3.send_keys(testdata['content'])
    btn2 = site.find_element("xpath", btn_save)
    btn2.click()
    time.sleep(testdata['sleep_time'])
    element = site.find_element('xpath', title)
    assert element.text == f'{testdata["title"]}'
    site.close()