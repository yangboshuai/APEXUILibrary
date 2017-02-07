from selenium import webdriver
import time,random,string

from _element import _createDep
from _element import _createUserElement
from _user import _GlobalKeywords
from _global import _logoutElement

class RANKKeyswords(object):
    '''

    '''
    def __init__(self):
        '''

        '''
        pass

    def enterRank(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.find_element_by_link_text("Department").click()
        _GlobalKeywords.webdriver.find_element_by_link_text("Rank").click()
    def createRank(self):
        '''

        :return: true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        rankname=''.join(random.sample((string.letters+string.digits),5))
        _GlobalKeywords.webdriver.find_element(_createDep.rankname_inputText[0],_createDep.rankname_inputText[1]).send_keys(rankname)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def  editRank(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.rank_editbutton[0],_createDep.rank_editbutton[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.rankname_inputText[0],_createDep.rankname_inputText[1]).clear()
        rankname = ''.join(random.sample((string.letters + string.digits), 5))
        _GlobalKeywords.webdriver.find_element(_createDep.rankname_inputText[0],_createDep.rankname_inputText[1]).send_keys(rankname)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def delRank(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.rank_checkbox[0],_createDep.rank_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()

    def selectRank(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()
