from selenium import webdriver
import time,random,string
from selenium.webdriver.support.select import Select

from _element import _createDep
from _element import _createUserElement
from _user import _GlobalKeywords
from _global import _logoutElement

class _RANKKeyswords(object):
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
    def createRank_ByAdmin(self):
        '''

        :return: true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        rankname=''.join(random.sample((string.letters+string.digits),5))
        _GlobalKeywords.webdriver.find_element(_createDep.rankname_inputText[0],_createDep.rankname_inputText[1]).send_keys(rankname)
        r=_GlobalKeywords.webdriver.find_element(_createDep.rank_status[0],_createDep.rank_status[1])
        Select(r).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.rank_description[0],_createDep.rank_description[1]).send_keys(rankname)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def  editRank_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.rank_editbutton[0],_createDep.rank_editbutton[1]).click()
        rankname = ''.join(random.sample((string.letters + string.digits), 5))
        time.sleep(2)
        r=_GlobalKeywords.webdriver.find_element(_createDep.rank_status[0],_createDep.rank_status[1])
        Select(r).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.rank_description[0],_createDep.rank_description[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createDep.rank_description[0],_createDep.rank_description[1]).send_keys(rankname)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def delRank_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.rank_checkbox[0],_createDep.rank_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()

    def selectRank_ByAdmin(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()


    def createRank_BySysadmin(self):
        '''

        :return: true or false
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        rankname=''.join(random.sample((string.letters+string.digits),5))
        _GlobalKeywords.webdriver.find_element(_createDep.rankname_inputText[0],_createDep.rankname_inputText[1]).send_keys(rankname)
        r=_GlobalKeywords.webdriver.find_element(_createDep.rank_status[0],_createDep.rank_status[1])
        Select(r).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.rank_description[0],_createDep.rank_description[1]).send_keys(rankname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def editRank_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.rank_editbutton[0],_createDep.rank_editbutton[1]).click()
        rankname = ''.join(random.sample((string.letters + string.digits), 5))
        r=_GlobalKeywords.webdriver.find_element(_createDep.rank_status[0],_createDep.rank_status[1])
        Select(r).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.rank_description[0],_createDep.rank_description[1]).clear()
        _GlobalKeywords.webdriver.find_element(_createDep.rank_description[0],_createDep.rank_description[1]).send_keys(rankname)
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)


    def delRank_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.rank_checkbox[0],_createDep.rank_checkbox[1]).click()
        _GlobalKeywords.webdriver.find_element(_createUserElement.dele_checkButton[0],_createUserElement.dele_checkButton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()


    def selectRank_BySysadmin(self,name):
        '''

        :param name:
        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.switch_to_default_content()
