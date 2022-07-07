# _*_ coding: utf-8 _*_
import time
from selenium.common.exceptions import NoSuchElementException
import os
import logging


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self,driver):
        self.driver = driver

    # 浏览器前进
    def forward(self):
        self.driver.forward()

    # 浏览器后退
    def back(self):
        self.driver.back()

    # 隐式等待
    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logging.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            logging.info("Closing and quit the browser")
        except Exception as e:
            logging.error("Failed to quit the browser with %s" %e)

    # 保存图片
    def get_windows_img(self):
        """在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.getcwd()) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logging.info("Had take screenshot and save to folder : /screenshots")
        except Exception as e:
            logging.info("Failed to take screenshot! %s" % e)
            self.get_windows_img()

    # 定位元素方法
    def find_element(self,selector):
        """
        根据 => 来切割字符串
        :param selector:
        :return:
        """
        element = ' '
        if '=>' not in selector:
            return self.driver.find_element_by_id(selector)
        selector_by = selector.split('=>')[0]
        selector_value = selector.split('=>')[1]

        if selector_by == 'i' or selector_by == 'id':
            try:
                element = self.driver.find_element_by_id(selector_value)
                logging.info("Had find the element \' %s \' seccessful "
                            "by %s via value:  %s " % (element.text,selector_by,selector_value))
            except NoSuchElementException as e:
                logging.error("NoSuchElementException: %s" % e)
                self.get_windows_img() # 截图
        elif selector_by == 'n' or selector_by == 'name':
            element = self.driver.find_element_by_name(selector_value)
        elif selector_by == 'c' or selector_by == 'class_name':
            element = self.driver.find_element_by_class_name(selector_value)
        elif selector_by == 'l' or selector_by == 'link_text':
            element = self.driver.find_element_by_link_text(selector_value)
        elif selector_by == 't' or selector_by == 'tag_name':
            element = self.driver.find_element_by_android_uiautomator(selector_value)
        elif selector_by == 'x' or selector_by == 'xpath':
            element = self.driver.find_element_by_xpath(selector_value)
            try:
                element = self.driver.find_element_by_xpath(selector_value)
                logging.info("Had find the element \' %s \' seccessful "
                            "by %s via value: %s " % (element.text,selector_by,selector_value))
            except NoSuchElementException as e:
                logging.error("NoSuchElementException: %s " % e)
                self.get_windows_img()
        elif selector_by == 's' or selector_by == 'selector_selector':
            element = self.driver.find_element_by_css_selector(selector_value)
        else:
            raise NameError("Please enter a valid type of targeting elements.")

        return element

    # 输入
    def type(self,selector,text):
        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logging.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logging.error("Failed to type in input box with %s" % e)
            self.get_windows_img()

    # 清除文本框
    def clear(self,selector):

        el = self.find_element(selector)
        try:
            el.clear()
            logging.info("Clear txt in input box before typing")
        except NameError as e:
            logging.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self,selector):

        el = self.find_element(selector)
        try:
            logging.info("The element \' %s ' was clicked." % el.text)
            el.click()
        except NameError as e:
            logging.error("Failed to click the element with %s" %e)

    '''
    获取元素的内容
    '''

    def get_attribute(self,selector):

        el = self.find_element(selector)
        try:
            content = el.get_attribute('textContent')
            logging.info("Had Content  \' %s \' in element" % content)
            return content
        except NameError as e:
            logging.error("Failed to click the element with %s" % e)
        self.get_windows_img()

    # 获取网页标题
    def get_page_title(self):
        logging.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    # 等待时间
    def sleep(self,seconds):
        time.sleep(seconds)
        logging.info("Sleep for %d seconds" % seconds)








