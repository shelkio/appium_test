import pytest
from appium import webdriver
from lib.base_page import BasePage
from lib import baiduorcapi
from lib.yamlContorl import YamlUsage
import logging

yml = YamlUsage('./datebase/config.yaml')
yml_conf = yml.get_yaml_conf()[0]
# 我的按钮
wd_button = 'id=>com.zcbl.bjjj_driving:id/tv_home_mine'
# 我的-立即登录按钮
now_login = 'id=>com.zcbl.bjjj_driving:id/tv_login_top'
# 用户名输入框
unm = 'x=>//android.widget.ListView/android.view.View[1]/android.widget.EditText[1]'
# 密码输入框
pwd = 't=>new UiSelector().text("请输入密码")'
# 验证码输入框
code = 'x=>//android.widget.ListView/android.view.View[3]/android.widget.EditText[1]'
# 验证码图片
code_img = 'x=>//android.widget.ListView/android.view.View[3]/android.view.View[2]'
# 登录按钮
login_button = 't=>new UiSelector().text("授权并登录")'


def getcode(driver):
    bb = BasePage(driver)
    for i in range(100):
        # 定位到验证码元素
        code_element = bb.find_element(code_img)
        code_element.screenshot('./img/easy_img/code.png')
        code = baiduorcapi.bdocrapi('./img/easy_img/code.png')
        if not code:
            bb.sleep(5)
            bb.click(code_img)
            # 定位到验证码元素
            code_element = bb.find_element(code_img)
            code_element.screenshot('./img/easy_img/code.png')
            code = baiduorcapi.bdocrapi('./img/easy_img/code.png')
        return code[0]['words']


@pytest.fixture()
def driver():
    url = "http://127.0.0.1:4723/wd/hub"
    driver = webdriver.Remote(url, yml_conf)
    logging.info("*************** 进入app ***************")
    driver.implicitly_wait(3)
    yield driver
    logging.info("*************** 关闭app ***************")


@pytest.fixture(autouse=False)
def login(driver):
    dd = BasePage(driver)
    logging.info("*************** 打开个人中心 ***************")
    dd.click(wd_button)
    logging.info("*************** 进入登录页面 ***************")
    dd.click(now_login)
    dd.type(unm, "17600352198")
    dd.type(pwd, "a12345678")
    dd.type(code, getcode(driver))
    dd.click(login_button)
    i = 1
    while dd.get_page_title == '登录':
        i = i + 1
        dd.type(code, getcode(driver))
        dd.click(login_button)
    else:
        print('验证码识别次数:' + str(i))
        print('登录成功')
    logging.info("*************** 登录成功返回个人中心 ***************")

