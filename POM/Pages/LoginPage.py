from selenium.webdriver.common.by import By
from POM.Locator.locator import *


class LoginPage():
  
  def __init__(self, driver):
    self.driver = driver
    
    self.email_textbox = Locator.email_textbox
    self.password_textbox = Locator.password_textbox
    self.button = Locator.button
    
  def username(self, username):
    self.driver.find.element(By.XPATH, self.email_textbox).send_keys(username)
    
  def password(self, password):
    self.driver.find.element(By.XPATH, self.password_textbox).send_keys(password)
    
  def button(self):
    self.driver.find.element(By.XPATH, self.button).click()