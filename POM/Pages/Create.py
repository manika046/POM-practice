from selenium.common import NoSuchElementException

from POM.Pages.Signup import *

class Create():

  def __init__(self, driver):
    self.driver = driver
    
    self.mrs_id = Locator.mrs_id
    self.password = Locator.password_id
    self.days = Locator.days_id
    self.months = Locator.months_id
    self.years = Locator.years_id
    self.newsletter = Locator.newsletter_id
    self.optin = Locator.optin_id
    self.firstname = Locator.firstname_id
    self.lastname = Locator.lastname_id
    self.company = Locator.company_id
    self.address = Locator.address_id
    self.address2 = Locator.address2_id
    self.country = Locator.country_id
    self.city = Locator.city_id
    self.state = Locator.state_id
    self.zipcode = Locator.zipcode_id
    self.number = Locator.number_id
    self.createbutton = Locator.create_button
    self.textcreated = Locator.text_created
    
  def ID(self):
    self.driver.find_element(By.ID, self.mrs_id).click()
  
  def Password(self, password):
    self.driver.find_element(By.ID, self.password).send_keys(password)
  
  def Days(self, days):
    Select(self.driver.find_element(By.ID, self.days)).select_by_value(days)
  
  def Months(self, months):
    Select(self.driver.find_element(By.ID, self.months)).select_by_value(months)
  
  def Years(self, years):
    Select(self.driver.find_element(By.ID, self.years)).select_by_value(years)
  
  def Newsletter(self):
    self.driver.find_element(By.ID, self.newsletter).click()
  
  def Optin(self):
    self.driver.find_element(By.ID, self.optin).click()
  
  def FirstName(self, firstname):
    self.driver.find_element(By.ID, self.firstname).send_keys(firstname)
  
  def LastName(self, lastname):
    self.driver.find_element(By.ID, self.lastname).send_keys(lastname)
  
  def Company(self, company):
    self.driver.find_element(By.ID, self.company).send_keys(company)
  
  def Address(self, address):
    self.driver.find_element(By.ID, self.address).send_keys(address)
  
  def AddressII(self, address2):
    self.driver.find_element(By.ID, self.address2).send_keys(address2)
    
  def Country(self, country):
    Select(self.driver.find_element(By.ID, self.country)).select_by_value(country)
    
  def City(self, city):
    self.driver.find_element(By.ID, self.city).send_keys(city)
    
  def State(self, state):
    self.driver.find_element(By.ID, self.state).send_keys(state)
    
  def Zipcode(self, zipcode):
    self.driver.find_element(By.ID, self.zipcode).send_keys(zipcode)
    
  def Number(self, number):
    self.driver.find_element(By.ID, self.number).send_keys(number)
    
  def CreateButton(self):
    self.driver.find_element(By.XPATH, self.createbutton).click()
  
  def verify_text(self):
    try:
      text_verify = self.driver.find_element(By.XPATH, self.textcreated).text
      assert "ACCOUNT CREATED!" in text_verify
      print("Account Created")
    
    except NoSuchElementException:
      print("Element not found, text verification failed")
    
    except AssertionError:
      print("Text does not contain 'ACCOUNT CREATED!'")
    
    except Exception as e:
      print(f"An error occurred: {e}")