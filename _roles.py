from selenium import webdriver
import time,string,random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from _element import _createUserElement
from _element import _createDep
from _global import _GlobalKeywords
from _element import _linkDepElement
from _global import _logoutElement

class _RolesKeysword(object):
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

    def createRoles_ByAdmin(self):
        '''

        :return:true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        rolename=''.join(random.sample((string.letters+string.digits),4))
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0],_createDep.rolename_inputText[1]).send_keys(rolename)
        s=_GlobalKeywords.webdriver.find_element(_createDep.role_status[0],_createDep.role_status[1])
        Select(s).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).send_keys(rolename)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def editRoles_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_linkDepElement.edit_button[0],_linkDepElement.edit_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0], _createDep.rolename_inputText[1]).clear()
        rolename = ''.join(random.sample((string.letters + string.digits), 4))
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0],_createDep.rolename_inputText[1]).send_keys(rolename)
        s=_GlobalKeywords.webdriver.find_element(_createDep.role_status[0],_createDep.role_status[1])
        Select(s).select_by_index('0')
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).send_keys(rolename)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).send_keys(rolename)
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def deleRoles_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.roles_checkbox[0],_createDep.roles_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()
        time.sleep(5)
        _GlobalKeywords.webdriver.find_element(_createDep.reason_textarea[0],_createDep.reason_textarea[1]).send_keys("123456")
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.reason_yesbutton[0],_createDep.reason_yesbutton[1]).click()
        time.sleep(2)

    def selectRoles_ByAdmin(self,name):
        '''

            :param name:
            :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()



    def createRole_BySysadmin(self):
        '''

        :return: true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button_Sysadmin[0],_createUserElement.new_button_Sysadmin[1]).click()
        rolename=''.join(random.sample((string.letters+string.digits),4))
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0],_createDep.rolename_inputText[1]).send_keys(rolename)
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).send_keys(rolename)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.submit_button[0],_createDep.submit_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)


    def editRoles_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_linkDepElement.edit_button[0],_linkDepElement.edit_button[1]).click()
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0],_createDep.rolename_inputText[1]).clear()
        rolename=''.join(random.sample((string.letters+string.digits),4))
        _GlobalKeywords.webdriver.find_element(_createDep.rolename_inputText[0],_createDep.rolename_inputText[1]).send_keys(rolename)
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).send_keys(rolename)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.submit_button[0],_createDep.submit_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def delRoles_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.roles_checkbox[0],_createDep.roles_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()
        time.sleep(5)
        _GlobalKeywords.webdriver.find_element(_createDep.reason_textarea[0],_createDep.reason_textarea[1]).send_keys("abc")
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.reason_yesbutton[0],_createDep.reason_yesbutton[1]).click()
        time.sleep(2)


    def selectRoles_BySysadmin(self,name):
        '''

        :param name:
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
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_linkDepElement.link_button[0],_linkDepElement.link_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.switch_to_frame("topPopModalCommonFrame")
        _GlobalKeywords.webdriver.switch_to_frame("orguserMF")
        _GlobalKeywords.webdriver.find_element(_linkDepElement.page_inputText[0],_linkDepElement.page_inputText[1]).send_keys("3")
        _GlobalKeywords.webdriver.find_element(_linkDepElement.go_button[0],_linkDepElement.go_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_linkDepElement.check_button[0],_linkDepElement.check_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_linkDepElement.submit_button[0],_linkDepElement.submit_button[1]).click()
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