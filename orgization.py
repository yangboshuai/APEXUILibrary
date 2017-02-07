from selenium import webdriver
import time,random,string
from selenium.webdriver.common.by import By


from _global import _GlobalKeywords
from _element import _createUserElement
from _element import _craeteOrg
from _element import _logoutElement

class _ORGKeyswords(object):
    '''    '''
    def __init__(self):
        '''

        '''
        pass
    def enterOrg(self):
        ''''
        '''

        _GlobalKeywords.webdriver.find_element_by_link_text("Organization").click()
        _GlobalKeywords.webdriver.switch_to_frame("menuFrame")
        _GlobalKeywords.webdriver.find_element_by_link_text("Automation").click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def createOrg(self):
        '''

        :return:true or false
        '''

        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        name=''.join(random.sample((string.letters+string.digits),5))
        _GlobalKeywords.webdriver.find_element(_craeteOrg.orgname_inputText[0],_craeteOrg.orgname_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_craeteOrg.office_inputText[0],_craeteOrg.office_inputText[1]).send_keys(random.sample(string.digits,6))
        time.sleep(2)
        email=''.join(random.sample(string.letters,8))
        _GlobalKeywords.webdriver.find_element(_craeteOrg.emmail_inputText[0],_craeteOrg.emmail_inputText[1]).send_keys(email+"@qq.com")
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def editOrg(self):
        '''

        :return: true or false
        '''

        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_craeteOrg.edit_button[0], _craeteOrg.edit_button[1]).click()
        _GlobalKeywords.webdriver.find_element(_craeteOrg.orgname_inputText[0], _craeteOrg.orgname_inputText[1]).clear()
        name = ''.join(random.sample((string.letters + string.digits), 5))
        _GlobalKeywords.webdriver.find_element(_craeteOrg.orgname_inputText[0], _craeteOrg.orgname_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_craeteOrg.office_inputText[0], _craeteOrg.office_inputText[1]).clear()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_craeteOrg.office_inputText[0], _craeteOrg.office_inputText[1]).send_keys(random.sample(string.digits, 6))
        time.sleep(3)
        email = ''.join(random.sample(string.letters, 8))
        _GlobalKeywords.webdriver.find_element(_craeteOrg.emmail_inputText[0], _craeteOrg.emmail_inputText[1]).clear()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_craeteOrg.emmail_inputText[0], _craeteOrg.emmail_inputText[1]).send_keys(email + "@qq.com")
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0], _createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(3)

    def delOrg(self):
        '''

        :return:
        '''

        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_craeteOrg.org_checkbox[0], _craeteOrg.org_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0], _logoutElement.yes_button[1]).click()

    def selectOrg(self,name):
        '''

        :return:
        '''

        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(3)

