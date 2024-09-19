import time
import unittest

from POM.Tests.test_signup import SignupTest
from POM.Pages.Create import *
  
class CreateTest(SignupTest):
  
  @classmethod
  def setUpClass(cls):
    SignupTest.setUpClass()
    
  def test_create_account(self):
    self.test_signup_valid()
    
    create = Create(self.driver)
    
    create.ID()
    create.Password("123456")
    create.Days("10")
    create.Months("5")
    create.Years("2021")
    create.Newsletter()
    create.Optin()
    create.FirstName("minion")
    create.LastName("park")
    create.Company("abc")
    create.Address("canberra")
    create.AddressII("NewYork")
    create.Country("United States")
    create.City("gftgfh")
    create.State("Washington")
    create.Zipcode("0014")
    create.Number("0155968965")
    create.CreateButton()
    create.verify_text()
    
    time.sleep(5)
    
  @classmethod
  def tearDown(cls):
    cls.driver.close()
    cls.driver.quit()
    
if __name__ == '__main__':
  unittest.TestCase()