from selenium import webdriver
import time,random,string
from selenium.webdriver.common.by import By


from _element import _createUserElement
from _global import _GlobalKeywords
from _element import _logoutElement

class _USERKeywords(object):
    '''User model keywords'''
    def __init__(self):
        '''
        '''
        pass
    def  enterUser(self):
        '''
        self.glo.is_visible(_GlobalKeywords.webdriver, By.PARTIAL_LINK_TEXT, "User", 10)
        _GlobalKeywords.webdriver.find_element_by_link_text("ITAS").click()
        :return:
        '''

        _GlobalKeywords.webdriver.find_element_by_link_text("User").click()
        _GlobalKeywords.webdriver.switch_to_frame("menuFrame")
        time.sleep(5)
        _GlobalKeywords.webdriver.find_element_by_link_text("Automation").click()
        _GlobalKeywords.webdriver.switch_to_default_content()

    def createUser(self):
        '''
        :return: true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        time.sleep(3)
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.fullname_inputText[0],_createUserElement.fullname_inputText[1]).send_keys('ws123')
        loginName=''.join(random.sample((string.letters+string.digits),8))
        _GlobalKeywords.webdriver.find_element(_createUserElement.loginname_inputText[0],_createUserElement.loginname_inputText[1]).send_keys(loginName)
        _GlobalKeywords.webdriver.find_element(_createUserElement.email_inputText[0],_createUserElement.email_inputText[1]).send_keys(loginName+"@123.com")
        _GlobalKeywords.webdriver.find_element(_createUserElement.mobile_inputText[0],_createUserElement.mobile_inputText[1]).send_keys(random.sample(string.ascii_letters,6))
        _GlobalKeywords.webdriver.find_element(_createUserElement.id_inputText[0],_createUserElement.id_inputText[1]).send_keys(string.digits,12)
        time.sleep(3)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()



    def editUser(self):
        '''

        :return: true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        time.sleep(3)
        _GlobalKeywords.webdriver.find_element(_createUserElement.edit_button[0],_createUserElement.edit_button[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.fullname_inputText[0],_createUserElement.fullname_inputText[1]).clear()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.fullname_inputText[0],_createUserElement.fullname_inputText[1]).send_keys('ws1234')
        _GlobalKeywords.webdriver.find_element(_createUserElement.email_inputText[0],_createUserElement.email_inputText[1]).clear()
        time.sleep(2)
        loginName = ''.join(random.sample((string.letters + string.digits), 8))
        _GlobalKeywords.webdriver.find_element(_createUserElement.email_inputText[0],_createUserElement.email_inputText[1]).send_keys(loginName + "@123.com")
        _GlobalKeywords.webdriver.find_element(_createUserElement.mobile_inputText[0],_createUserElement.mobile_inputText[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createUserElement.mobile_inputText[0],_createUserElement.mobile_inputText[1]).send_keys(random.sample(string.ascii_letters, 6))
        _GlobalKeywords.webdriver.find_element(_createUserElement.id_inputText[0], _createUserElement.id_inputText[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createUserElement.id_inputText[0],_createUserElement.id_inputText[1]).send_keys(string.digits, 12)
        time.sleep(3)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def delUser(self):
        '''

        :return: true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        time.sleep(3)
        _GlobalKeywords.webdriver.find_element(_createUserElement.user_checkbox[0],_createUserElement.user_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0], _logoutElement.yes_button[1]).click()
        time.sleep(2)

    def selectUser(self,name):
        '''

        :param name: fullname
        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)


