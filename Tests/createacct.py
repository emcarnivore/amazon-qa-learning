import time
import unittest
from selenium import webdriver
from ObjClasses.page import MainPage, ResultsPage, TextElement
from Locators.locators import MainPageLocators, ResultsPageLocators


class CreateAccount(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Tests Create Account, verifies "Continue" and "Verify email" displays
    def testVerifyEmail(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Hovers over "Hello, Sign in"
        mainPage.hoverOver(MainPageLocators.HelloSignIn)
        time.sleep(1)
        # Clicks "Start here." on hover window
        mainPage.clickElement(MainPageLocators.StartHere)

        time.sleep(1)
        # Verifies results page displays "Create account" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreateAccountHeader, "Create account"), 
            "No results found."
            )

        # Note: Text on submit button changes when email/number is entered
        # Verifies submit button displays "Continue" while email/number box is empty
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreateContinueText, "Continue"), 
            "No results found."
        )

        # Adds class containing a locator to a variable
        self.createNameBox = TextElement(self.driver, ResultsPageLocators.CreateNameBox)
        self.createNumEmailBox = TextElement(self.driver, ResultsPageLocators.CreateNumEmailBox)
        self.createPwdBox = TextElement(self.driver, ResultsPageLocators.CreatePwdBox)
        self.createRePwdBox = TextElement(self.driver, ResultsPageLocators.CreateRePwdBox)
        # Adds text to variables
        self.createNameBox.setValue("TestBot")
        self.createNumEmailBox.setValue("testemail@test.com")
        self.createPwdBox.setValue("abc123!")
        self.createRePwdBox.setValue("abc")
        
        time.sleep(1)
        # Verifies submit button displays "Verify email"
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreateEmailText, "Verify email"),
            "No results found."
        )

        time.sleep(1)
        # Clicks submit button
        resultsPage.clickElement(ResultsPageLocators.CreateSubmitButton)
        
        time.sleep(1)
        # Verifies alert displays "Passwords must match"
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreatePwdsAlert, "Passwords must match"),
            "No results found."
        )


    # Tests Create Account, verifies "Continue" and "Verify mobile number" displays
    def testVerifyNumber(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Hovers over "Hello, Sign in"
        mainPage.hoverOver(MainPageLocators.HelloSignIn)
        time.sleep(1)
        # Clicks "Start here." on hover window
        mainPage.clickElement(MainPageLocators.StartHere)

        time.sleep(1)
        # Verifies results page displays "Create account" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreateAccountHeader, "Create account"), 
            "No results found."
            )

        # Note: Text on submit button changes when email/number is entered
        # Verifies submit button displays "Continue" while email/number box is empty
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreateContinueText, "Continue"), 
            "No results found."
        )

        # Adds class containing a locator to a variable
        self.createNameBox = TextElement(self.driver, ResultsPageLocators.CreateNameBox)
        self.createNumEmailBox = TextElement(self.driver, ResultsPageLocators.CreateNumEmailBox)
        self.createPwdBox = TextElement(self.driver, ResultsPageLocators.CreatePwdBox)
        self.createRePwdBox = TextElement(self.driver, ResultsPageLocators.CreateRePwdBox)
        # Adds text to variables
        self.createNameBox.setValue("TestBot")
        self.createNumEmailBox.setValue("7141231234")
        self.createPwdBox.setValue("abc123!")
        self.createRePwdBox.setValue("abc")
        
        time.sleep(1)
        # Verifies submit button displays "Verify email"
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreateNumText, "Verify mobile number"),
            "No results found."
        )

        time.sleep(1)
        # Clicks submit button
        resultsPage.clickElement(ResultsPageLocators.CreateSubmitButton)
        
        time.sleep(1)
        # Verifies alert displays "Passwords must match"
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CreatePwdsAlert, "Passwords must match"),
            "No results found."
        )


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
