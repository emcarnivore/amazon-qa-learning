import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ObjClasses.page import MainPage, ResultsPage, TextElement
from Locators.locators import MainPageLocators, ResultsPageLocators


class SignIn(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Tests Sign-In, verifies "Continue", "Sign-In", and "There was a problem" displays
    def testSignInEmail(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Hovers over "Hello, Sign in"
        mainPage.hoverOver(MainPageLocators.HelloSignIn)
        time.sleep(1)
        # Verifies hover window displays "Sign in" submit button
        self.assertTrue(
            mainPage.elementMatches(MainPageLocators.SignInButton, "Sign in"), 
            "No results found."
            )
        
        # Clicks "Hello, Sign in"
        mainPage.clickElement(MainPageLocators.HelloSignIn)
        time.sleep(1)
        # Verifies results page displays "Sign-In" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.SignInHeader, "Sign-In"), 
            "No results found."
            )

        # Adds class containing a locator to a variable
        self.signInEmailNumBox = TextElement(self.driver, ResultsPageLocators.SignInEmailNumBox)

        # Adds text to variables
        self.signInEmailNumBox.setValue("testemail@test.com")
        time.sleep(1)
        # Clicks submit button
        resultsPage.clickElement(ResultsPageLocators.SignInContinueButton)
        
        # Adds class containing a locator to a variable
        self.signInPwdBox = TextElement(self.driver, ResultsPageLocators.SignInPwdBox)

        # Adds text to variables
        self.signInPwdBox.setValue("abc")
        # Clicks submit button
        resultsPage.clickElement(ResultsPageLocators.SignInSubmitButton)
        time.sleep(1)
        # Verifies alert displays "There was a problem" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.SignInThereWasAProblem, "There was a problem"),
            "No results found."
        )


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
