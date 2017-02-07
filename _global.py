import time

from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium import webdriver

class _GlobalKeywords(object):
    '''global keywords'''

    webdriver=webdriver.Ie()

    def __init__(self):
        pass

    def setBrowser(self,browser):
        '''
        set browser type: chrome,ie,firefox
        :param browser:browser type
        :return:
        '''

        if browser.upper()=='CHROME':
            self.webdriver = webdriver.Chrome()
        elif browser.upper() == 'FIREFOX':
            self.webdriver =webdriver.Firefox()
        else:
            self.webdriver = webdriver.Ie()

    def openBrowser(self):
        _GlobalKeywords.webdriver.get("http://10.10.2.40:8080/apex/login")
        _GlobalKeywords.webdriver.maximize_window()

    def login(self,username,password):
        '''
        1.input username,password; 2. click login button
        :param username: login name
        :param password: login password
        :return:login result true or false
        '''

        _GlobalKeywords.webdriver.find_element(_loginElement.username_inputText[0],_loginElement.username_inputText[1]).send_keys(username)
        _GlobalKeywords.webdriver.find_element(_loginElement.password_inputText[0],_loginElement.password_inputText[1]).send_keys(password)
        _GlobalKeywords.webdriver.find_element(_loginElement.submit_inputText[0],_loginElement.submit_inputText[1]).click()
        time.sleep(2)

        if _GlobalKeywords.webdriver.find_element(By.XPATH,
                               "//div[@class='modal-footer']/button[@class='btn btn-primary ax-yes']").is_displayed():
            _GlobalKeywords.webdriver.find_element(By.XPATH,
                                "//div[@class='modal-footer']/button[@class='btn btn-primary ax-yes']").click()

        loginResult=self.glo.is_visible(_GlobalKeywords.webdriver,By.ID, "homePageHref",10)

        return loginResult

    def logout(self):
        '''
        :return: true or false
        '''

        _GlobalKeywords.webdriver.switch_to_default_content()
        time.sleep(2)
        _GlobalKeywords.webdriver.find_element_by_id("abc").click()
        _GlobalKeywords.webdriver.find_element_by_xpath("//*[@id='logobg']/div/div[1]/ul/li/ul/li[7]/a").click()
        _GlobalKeywords.webdriver.find_element(By.XPATH,"//div[@class='modal-footer']/button[@class='btn btn-primary save ax-save']").click()
        time.sleep(3)
        _GlobalKeywords.webdriver.quit()

    def is_visible(self,driver,by,locator,timeout=10):
        '''

        :param locator:
        :param timeout:
        :return:ture or false
        '''
        try:
            ui.WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False

    def is_not_visible(self,driver,by,locator, timeout=10):
        '''

        :param driver:
        :param by:
        :param locator:
        :param timeout:
        :return:
        '''
        try:
            ui.WebDriverWait(driver, timeout).until_not(EC.visibility_of_element_located((by, locator)))
            return True
        except TimeoutException:
            return False
