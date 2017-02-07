from selenium import webdriver
import time,string,random
from selenium.webdriver.common.by import By


from _element import _createUserElement
from _element import _menuElement
from _element import _submenuElemnet
from _element import _createDep
from _global import _GlobalKeywords
from _element import _linkDepElement
from _global import _logoutElement

class _DepKeysword(object):
    '''

    '''
    def __init__(self):
        '''

        '''
        pass

    def enterRoles(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.find_element_by_link_text("Department").click()
        _GlobalKeywords.webdriver.find_element_by_link_text("Roles").click()
        time.sleep(2)

    def createRoles(self):
        '''

        :return:true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        rolename=''.join(random.sample((string.letters+string.digits),4))
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0],_createDep.rolename_inputText[1]).send_keys(rolename)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)


    def editRoles(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_linkDepElement.edit_button[0],_linkDepElement.edit_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0], _createDep.rolename_inputText[1]).clear()
        rolename = ''.join(random.sample((string.letters + string.digits), 4))
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0],_createDep.rolename_inputText[1]).send_keys(rolename)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)


    def deleRoles(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.roles_checkbox[0],_createDep.roles_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.reason_textarea[0],_createDep.reason_textarea[1]).send_keys("123")
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()
        time.sleep(2)

    def selectRoles(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()


    def link(self):
        '''

        :return:true or false
        '''
        self.webdriver.find_element(_menuElement.dep_menuText[0], _menuElement.dep_menuText[1]).click()
        self.webdriver.find_element(_submenuElemnet.role_menuText[0], _submenuElemnet.role_menuText[1]).click()
        time.sleep(2)
        self.webdriver.switch_to_frame("mainFrame")
        self.webdriver.find_element(_linkDepElement.link_button[0],_linkDepElement.link_button[1]).click()
        self.webdriver.switch_to_default_content()
        self.webdriver.switch_to_frame("topPopModalCommonFrame")
        self.webdriver.switch_to_frame("orguserMF")
        self.webdriver.find_element(_linkDepElement.page_inputText[0],_linkDepElement.page_inputText[1]).send_keys("3")
        self.webdriver.find_element(_linkDepElement.go_button[0],_linkDepElement.go_button[1]).click()
        time.sleep(2)
        self.webdriver.find_element(_linkDepElement.check_button[0],_linkDepElement.check_button[1]).click()
        self.webdriver.switch_to_default_content()
        self.webdriver.switch_to_default_content()
        time.sleep(2)
        self.webdriver.find_element(_linkDepElement.submit_button[0],_linkDepElement.submit_button[1]).click()
        time.sleep(2)


    def enable(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.enabled_button[0],_createUserElement.enabled_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()
        time.sleep(2)



