import unittest

from selenium import webdriver
from POM.Pages.LoginPage import *

class LoginTest(unittest.TestCase):
  
  def setUpClass(cls):
    cls.driver = webdriver.Chrome("C:/Users/acer/Python/Python312/chromedriver.exe")
    cls.driver.implicitly_wait(20)
    cls.driver.maximize_window()
    
    
  def test_login_valid(self):
    driver = self.driver
    driver.get("https://www.automationexercise.com")
    
    login = LoginPage(driver)
    login.username("Minie")
    login.password("123456")
    login.button.click()
    
    
  def tearDown(self):
    self.driver.close()
    self.driver.quit()
    

if '__name__' == '__main__':
  unittest.TestCase()