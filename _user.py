from selenium import webdriver
import time,random,string
from selenium.webdriver.common.by import By

from _element import _loginElement
from _element import _createUserElement
from _global import _GlobalKeywords

class _USERKeywords(object):
    '''User model keywords'''

    def __init__(self):
        '''
        '''

    def createUser(self):
        '''

        :param loginName:
        :param fullName:
        :param mobile:
        :param idCard:
        :return: true or false
        '''
        self.glo.is_visible(_GlobalKeywords.webdriver, By.PARTIAL_LINK_TEXT, "User", 10)
        _GlobalKeywords.webdriver.find_element_by_partial_link_text("User").click()
        _GlobalKeywords.webdriver.switch_to_frame("menuFrame")
        time.sleep(5)
        _GlobalKeywords.webdriver.find_element_by_partial_link_text("Automation").click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        time.sleep(3)
        _GlobalKeywords.webdriver.find_element(By.ID, 'btnAddNew').click()
        _GlobalKeywords.webdriver.find_element_by_id("entity_fullName").send_keys('AutomationTest')
        loginName = ''.join(random.sample((string.letters + string.digits), 8))
        _GlobalKeywords.webdriver.find_element_by_id("entity_loginName").send_keys(loginName)
        _GlobalKeywords.webdriver.find_element_by_id("entity_email").send_keys(loginName + "@123.com")
        _GlobalKeywords.webdriver.find_element_by_id("entity_mobile").send_keys(random.sample(string.digits, 6))
        _GlobalKeywords.webdriver.find_element_by_id("entity_identityCard").send_keys(string.digits, 12)
        time.sleep(3)
        _GlobalKeywords.webdriver.find_element_by_id("btnSave").click()

    def editUser(self):
        pass

