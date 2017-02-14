from selenium import webdriver
import time,random,string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from _global import _GlobalKeywords
from _element import _createUserElement
from _element import _createDep
from _global import _logoutElement

class _GROUPKeyswords(object):
    '''     '''
    def __init__(self):
        '''

        '''
    pass

    def enterGroup(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.find_element_by_link_text("Department").click()
        _GlobalKeywords.webdriver.find_element_by_link_text("Group").click()
        _GlobalKeywords.webdriver.switch_to_frame("menuFrame")
        _GlobalKeywords.webdriver.find_element_by_link_text("Group").click()
        _GlobalKeywords.webdriver.switch_to_default_content()

    def createGroup_ByAdmin(self):
        '''

        :return:true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        groupname=''.join(random.sample((string.letters+string.digits),8))
        _GlobalKeywords.webdriver.find_element(_createDep.groupname_inputText[0],_createDep.groupname_inputText[1]).send_keys(groupname)
        g=_GlobalKeywords.webdriver.find_element(_createDep.group_status[0],_createDep.group_status[1])
        Select(g).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.group_description[0],_createDep.group_description[1]).send_keys(groupname)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def editGroup_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.groupedit_button[0],_createUserElement.groupedit_button[1]).click()
        _GlobalKeywords.webdriver.find_element(_createDep.groupname_inputText[0], _createDep.groupname_inputText[1]).clear()
        time.sleep(2)
        groupname = ''.join(random.sample((string.letters + string.digits), 8))
        _GlobalKeywords.webdriver.find_element(_createDep.groupname_inputText[0],_createDep.groupname_inputText[1]).send_keys(groupname)
        time.sleep(2)
        g=_GlobalKeywords.webdriver.find_element(_createDep.group_status[0],_createDep.group_status[1])
        Select(g).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.group_description[0],_createDep.group_description[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createDep.group_description[0],_createDep.group_description[1]).send_keys(groupname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()

    def delGroup_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.group_checkbox[0],_createDep.group_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()

    def selectGroup_ByAdmin(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)


    def createGroup_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button_Sysadmin[0],_createUserElement.new_button_Sysadmin[1]).click()
        groupname=''.join(random.sample((string.letters+string.digits),8))
        _GlobalKeywords.webdriver.find_element(_createDep.groupname_inputText[0],_createDep.groupname_inputText[1]).send_keys(groupname)
        _GlobalKeywords.webdriver.find_element(_createDep.role_description[0],_createDep.role_description[1]).send_keys(groupname)
        _GlobalKeywords.webdriver.find_element(_createDep.submit_button[0],_createDep.submit_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def editGroup_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.groupedit_button[0],_createUserElement.groupedit_button[1]).click()
        _GlobalKeywords.webdriver.find_element(_createDep.groupname_inputText[0], _createDep.groupname_inputText[1]).clear()
        time.sleep(2)
        groupname = ''.join(random.sample((string.letters + string.digits), 8))
        _GlobalKeywords.webdriver.find_element(_createDep.groupname_inputText[0],_createDep.groupname_inputText[1]).send_keys(groupname)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.group_description[0],_createDep.group_description[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createDep.group_description[0],_createDep.group_description[1]).send_keys(groupname)
        _GlobalKeywords.webdriver.find_element(_createDep.submit_button[0],_createDep.submit_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def delGroup_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.group_checkbox[0],_createDep.group_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()


    def selectGroup_BySysadmin(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)