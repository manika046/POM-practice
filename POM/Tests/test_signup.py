import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from POM.Pages.Signup import *

service = Service("C:\\Users\\acer\\Python\\Python312\\chromedriver.exe")
class SignupTest(unittest.TestCase):
  
  @classmethod
  def setUpClass(cls):
    cls.driver = webdriver.Chrome(service=service)
    cls.driver.implicitly_wait(20)
    cls.driver.maximize_window()
  
  def test_signup_valid(self):
    driver = self.driver
    driver.get("https://www.automationexercise.com")
    
    signup = SignUpPage(driver)
    
    signup.InitialButton()
    signup.username("Minie")
    signup.Email("moni@gmail")
    signup.Button()
  
    time.sleep(2)
    
  @classmethod
  def tearDown(cls):
    cls.driver.close()
    cls.driver.quit()


if __name__ == '__main__':
  unittest.TestCase()