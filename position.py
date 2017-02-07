import time,random,string
from selenium.webdriver.common.by import By

from _element import _createUserElement
from _global import _GlobalKeywords
from _element import _createDep
from _global import _logoutElement


class _POSITIONKeywords(object):
    '''   '''
    def __init__(self):
        '''

        '''
        pass

    def enterPosit(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.find_element_by_link_text("Department").click()
        _GlobalKeywords.webdriver.find_element_by_link_text("Position").click()
        time.sleep(2)


    def _createPosit(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        positionname=''.join(random.sample((string.letters+string.digits),6))
        _GlobalKeywords.webdriver.find_element(_createDep.positionname_inputText[0],_createDep.positionname_inputText[1]).send_keys(positionname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()


    def _editPosit(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.position_editbutton[0],_createDep.position_editbutton[1]).click()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.positionname_inputText[0],_createDep.positionname_inputText[1]).clear()
        positionname = ''.join(random.sample((string.letters + string.digits), 6))
        _GlobalKeywords.webdriver.find_element(_createDep.positionname_inputText[0],_createDep.positionname_inputText[1]).send_keys(positionname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()


    def _delPosit(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.position_delebutton[0],_createDep.position_delebutton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()

    def _selectPosit(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()