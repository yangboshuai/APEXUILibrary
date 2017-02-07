from selenium import webdriver
import  time,random,string
from selenium.webdriver.common.by import By

from _global import _GlobalKeywords
from _element import _createUserElement
from _element import _menuElement
from _element import _submenuElemnet
from _element import _createWork
from _element import _loginElement
from _element import _logoutElement

class _ProcessKeyswords(object):
    '''

    '''
    glo=_GlobalKeywords()
    webdriver=webdriver.Chrome()
    def __init__(self):
        '''

        '''
        pass
    def openBrowser(self):

        self.webdriver.get("http://10.10.2.40:8080/apex/login")
        self.webdriver.maximize_window()


    def login(self,username,password):
        '''
        1.input username,password; 2. click login button
        :param username: login name
        :param password: login password
        :return:login result true or false
        '''

        self.webdriver.find_element(_loginElement.username_inputText[0],_loginElement.username_inputText[1]).send_keys(username)
        self.webdriver.find_element(_loginElement.password_inputText[0],_loginElement.password_inputText[1]).send_keys(password)
        self.webdriver.find_element(_loginElement.submit_inputText[0],_loginElement.submit_inputText[1]).click()
        time.sleep(2)
        loginResult = self.glo._is_visible(self.webdriver, By.ID, 'homePageHref', 10)
        if loginResult=='True':
            return loginResult
        else:
            if self.webdriver.find_element(By.XPATH,
                                       "//div[@class='modal-footer']/button[@class='btn btn-primary ax-yes']").is_displayed():
                self.webdriver.find_element(By.XPATH,
                                        "//div[@class='modal-footer']/button[@class='btn btn-primary ax-yes']").click()
            loginResult1=self.glo._is_visible(self.webdriver,By.ID, 'homePageHref',10)
            return loginResult1

    def createProcess(self):
        '''

        :return: true or false
        '''
        self.webdriver.find_element(_menuElement.workflow_menuText[0],_menuElement.workflow_menuText[1]).click()
        self.webdriver.find_element(_submenuElemnet.process_menuText[0],_submenuElemnet.process_menuText[1]).click()
        self.webdriver.switch_to_frame("mainFrame")
        self.webdriver.find_element(_createUserElement.new_button[0],_createUserElement.new_button[1]).click()
        time.sleep(2)
        processname=''.join(random.sample((string.letters+string.digits),4))
        self.webdriver.find_element(_createWork.processname_inputText[0],_createWork.processname_inputText[1]).send_keys(processname)
        self.webdriver.find_element(_createWork.processkey_inputText[0],_createWork.processkey_inputText[1]).send_keys("123456")
        time.sleep(2)
        self.webdriver.find_element(_createUserElement.save_button[0],_createUserElement.save_button[1]).click()
        time.sleep(2)
        self.webdriver.switch_to_default_content()

    def logout(self):
        '''
        :return: true or false
        '''
        self.webdriver.find_element(_logoutElement.admin_button[0],_logoutElement.admin_button[1]).click()
        self.webdriver.find_element(_logoutElement.logout_button[0],_logoutElement.logout_button[1]).click()
        self.webdriver.find_element(_logoutElement.yes_button[0],_logoutElement.yes_button[1]).click()
        time.sleep(3)
        self.webdriver.quit()