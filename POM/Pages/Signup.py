from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from POM.Locator.locator import *


class SignUpPage:
  
  def __init__(self, driver):
    self.driver = driver
    
    self.initial_button = Locator.nav_login
    self.username_textbox = Locator.sign_name
    self.email_textbox = Locator.sign_email
    self.button = Locator.sign_button
  
  def InitialButton(self):
    self.driver.find_element(By.XPATH, self.initial_button).click()
  
  def username(self, username):
    self.driver.find_element(By.XPATH, self.username_textbox).send_keys(username)
  
  def Email(self, email):
    self.driver.find_element(By.XPATH, self.email_textbox).send_keys(email)
  
  def Button(self):
    self.driver.find_element(By.XPATH, self.button).click()
