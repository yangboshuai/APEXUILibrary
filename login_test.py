import time,random,string

from selenium import webdriver
from selenium.webdriver.common.by import By
import selenium.webdriver.support.ui as ui
import selenium.webdriver.support.expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("http://10.10.2.40:8080/apex/login")
driver.maximize_window()

driver.find_element(By.ID,'username').send_keys('admin')
driver.find_element_by_id('password').send_keys('1234a*')
driver.find_element_by_id('login_submit').click()

if driver.find_element(By.XPATH,"//div[@class='modal-footer']/button[@class='btn btn-primary ax-yes']").is_displayed() :
    driver.find_element(By.XPATH, "//div[@class='modal-footer']/button[@class='btn btn-primary ax-yes']").click()

ui.WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "homePageHref")))

driver.find_element_by_partial_link_text("User").click()
driver.switch_to_frame("menuFrame")
time.sleep(5)
driver.find_element_by_partial_link_text("Automation").click()
driver.switch_to_default_content()
driver.switch_to_frame("mainFrame")
time.sleep(3)
driver.find_element(By.ID,'btnAddNew').click()
driver.find_element_by_id("entity_fullName").send_keys('AutomationTest')
loginName=''.join(random.sample((string.letters + string.digits),8))
driver.find_element_by_id("entity_loginName").send_keys(loginName)
driver.find_element_by_id("entity_email").send_keys(loginName+"@123.com")
driver.find_element_by_id("entity_mobile").send_keys(random.sample(string.digits, 6))
driver.find_element_by_id("entity_identityCard").send_keys(string.digits, 12)
time.sleep(3)
driver.find_element_by_id("btnSave").click()

driver.switch_to_default_content()
time.sleep(2)
driver.find_element_by_id("abc").click()
driver.find_element_by_xpath("//*[@id='logobg']/div/div[1]/ul/li/ul/li[7]/a").click()
driver.find_element(By.XPATH,"//div[@class='modal-footer']/button[@class='btn btn-primary save ax-save']").click()
time.sleep(3)

driver.quit()