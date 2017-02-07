from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

from _element import _createCal
from _element import _loginElement
from _element import _logoutElement
from _global import _GlobalKeywords
from _element import _createTask
from _element import _createTemplate

class _SYSTEMKeysword(object):
    '''

    '''
    def __init__(self):
        '''

        '''
    def creatCalendar(self):
        '''

        :return:true or false
        '''
        self.webdriver.switch_to_frame("mainFrame")
        self.webdriver.find_element(_createCal.new_buttonText[0],_createCal.new_buttonText[1]).click()
        self.webdriver.switch_to_default_content()
        self.webdriver.switch_to_frame("topPopModalCommonFrame")
        self.webdriver.find_element(_createCal.reminderContent_inputText[0],_createCal.reminderContent_inputText[1]).send_keys("1243")
        time.sleep(5)
        self.webdriver.find_element(_createCal.starttime_inputText[0],_createCal.starttime_inputText[1]).click()
        iframe=self.webdriver.find_element(_createCal.iframe[0],_createCal.iframe[1])
        self.webdriver.switch_to_frame(iframe)
        self.webdriver.find_element(_createCal.day_checkbutton[0],_createCal.day_checkbutton[1]).click();
        self.webdriver.switch_to_default_content();
        self.webdriver.find_element(_createCal.endtime_inputText[0],_createCal.endtime_inputText[1]).send_keys("15-01-2017 15:23:27")
        time.sleep(2)
        Select(self.webdriver.find_element(_createCal.type_select[0],_createCal.type_select[1])).select_by_index(2)
        Select(self.webdriver.find_element(_createCal.reminder_select[0],_createCal.reminder_select[1])).select_by_index(3)
        Select(self.webdriver.find_element(_createCal.repeat_select[0],_createCal.repeat_select[1])).select_by_index(2)
        self.webdriver.find_element(_createCal.email_checkbox[0],_createCal.email_checkbox[1]).click()
        time.sleep(5)
        self.webdriver.find_element(_createCal.save_button[0],_createCal.save_button[1]).click()
        self.webdriver.switch_to_default_content()

    def creatTask(self):
        '''

        :return: true or false
        '''
        self.webdriver.switch_to_frame("mainFrame")
        self.webdriver.find_element(_createTask.new_button[0],_createTask.new_button[1]).click()
        content="jishdahd\ngyudgi"
        self.webdriver.find_element(_createTask.content_textarea[0],_createTask.content_textarea[1]).send_keys(content)
        self.webdriver.switch_to_default_content()
        time.sleep(2)
    def createTemplate(self):
        '''

        :return: true or false
        '''
        self.webdriver.switch_to_frame("mainFrame")
        self.webdriver.find_element(_createTemplate.templateCode_inputText[0],_createTemplate.templateCode_inputText[1]).send_keys("")
        self.webdriver.find_element(_createTemplate.templateName_inputText[0],_createTemplate.templateName_inputText[1]).send_keys("")
        time.sleep(2)
        self.webdriver.find_element(_createTemplate.textField_redioText[0],_createTemplate.textField_redioText[1]).click()
        self.webdriver.find_element(_createTemplate.content_textarea[0],_createTemplate.content_textarea[1]).send_keys("")
        '''
        self.webdriver.find_element(_createTemplate.textEditor_redioText[0],_createTemplate.textEditor_redioText[1]).click()
        self.webdriver.switch_to_frame("ueditor_0")
        self.webdriver.find_element(_createTemplate.editor_viewText[0],_createTemplate.editor_viewText[1]).send_keys("")
        self.webdriver.switch_to_default_content()
        '''
        self.webdriver.switch_to_default_content()

    def createWorkBeach(self):
        '''

        :return true or false:
        '''

    def logout(self):
        '''
        :return: true or false
        '''
        self.webdriver.find_element(_logoutElement.admin_button[0],_logoutElement.admin_button[1]).click()
        self.webdriver.find_element(_logoutElement.logout_button[0],_logoutElement.logout_button[1]).click()
        self.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()
        time.sleep(3)
        self.webdriver.quit()