import time,random,string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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


    def createPosit_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        positionname=''.join(random.sample((string.letters+string.digits),6))
        _GlobalKeywords.webdriver.find_element(_createDep.positionname_inputText[0],_createDep.positionname_inputText[1]).send_keys(positionname)
        p=_GlobalKeywords.webdriver.find_element(_createDep.position_status[0],_createDep.position_status[1])
        Select(p).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.position_description[0],_createDep.position_description[1]).send_keys(positionname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()

    def editPosit_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.position_editbutton[0],_createDep.position_editbutton[1]).click()
        time.sleep(2)
        positionname = ''.join(random.sample((string.letters + string.digits), 6))
        p=_GlobalKeywords.webdriver.find_element(_createDep.position_status[0],_createDep.position_status[1])
        Select(p).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.position_description[0],_createDep.position_description[1]).clear()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.position_description[0],_createDep.position_description[1]).send_keys(positionname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def delPosit_ByAdmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.position_delebutton[0],_createDep.position_delebutton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()

    def selectPosit_ByAdmin(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()


    def createPosit_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        positionname=''.join(random.sample((string.letters+string.digits),6))
        _GlobalKeywords.webdriver.find_element(_createDep.positionname_inputText[0],_createDep.positionname_inputText[1]).send_keys(positionname)
        p=_GlobalKeywords.webdriver.find_element(_createDep.position_status[0],_createDep.position_status[1])
        Select(p).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.position_description[0],_createDep.position_description[1]).send_keys(positionname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()


    def editPosit_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.position_editbutton[0],_createDep.position_editbutton[1]).click()
        time.sleep(2)
        positionname = ''.join(random.sample((string.letters + string.digits), 6))
        p=_GlobalKeywords.webdriver.find_element(_createDep.position_status[0],_createDep.position_status[1])
        Select(p).select_by_index('1')
        _GlobalKeywords.webdriver.find_element(_createDep.position_description[0],_createDep.position_description[1]).clear()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_createDep.position_description[0],_createDep.position_description[1]).send_keys(positionname)
        _GlobalKeywords.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)

    def delPosit_BySysadmin(self):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createDep.position_delebutton[0],_createDep.position_delebutton[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()


    def selectPosit_BySysadmin(self,name):
        '''

        :return:
        '''
        _GlobalKeywords.webdriver.switch_to_frame("mainFrame")
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_inputText[0],_createUserElement.search_inputText[1]).send_keys(name)
        _GlobalKeywords.webdriver.find_element(_createUserElement.search_button[0],_createUserElement.search_button[1]).click()
        _GlobalKeywords.webdriver.switch_to_default_content()