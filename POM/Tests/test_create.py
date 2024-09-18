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
    create.Days("20")
    create.Months("3")
    create.Years("2000")
    create.Newsletter()
    create.Optin()
    create.FirstName("minion")
    create.LastName("kim")
    create.Company("abc")
    create.Address("canberra")
    create.AddressII("NewYork")
    create.Country("United States")
    create.City("Ktm")
    create.State("America")
    create.Zipcode("0014")
    create.Number("0155449965")
    create.CreateButton()
    
    time.sleep(5)
    
  @classmethod
  def tearDown(cls):
    cls.driver.close()
    cls.driver.quit()
    
if __name__ == '__main__':
  unittest.TestCase()