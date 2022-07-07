import allure
import pytest
import logging

from lib.base_page import BasePage
from lib.readconfg import read_config
from lib.yamlContorl import YamlUsage
from lib.sendrequest import SendRequests
# 首页按钮
home_page = 'id=>com.zcbl.bjjj_driving:id/tv_home_shouye'
# 车管所入口
cgs_button = 't=>new UiSelector().text("掌上车管所")'


@allure.title("进入车管所")
def test_open_cgs(driver, login):
    base_driver = BasePage(driver)
    base_driver.click(home_page)
    base_driver.click(cgs_button)
    print("1111")







