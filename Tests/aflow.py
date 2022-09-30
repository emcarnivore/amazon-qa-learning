import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ObjClasses.page import MainPage, ResultsPage, TextElement
from Locators.locators import MainPageLocators, ResultsPageLocators

# Handles .env files to load environment variables
from dotenv import load_dotenv
# Actually load the key:value pairs in the .env file as environment variables
load_dotenv()


class TestBench(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Test flow of sign in, search, add items to cart, and checkout
    def testAFlow(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)
        
        time.sleep(1)
        # Clicks "Hello, Sign in"
        mainPage.clickElement(MainPageLocators.HelloSignIn)
        # Verifies results page displays "Sign-In" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.SignInHeader, "Sign-In"), 
            "No results found."
            )

        # Adds class containing a locator to a variable
        self.signInEmailNumBox = TextElement(self.driver, ResultsPageLocators.SignInEmailNumBox)

        # Adds text to variables
        self.signInEmailNumBox.setValue(os.getenv("AMAZON_TEST_EMAIL"))
        time.sleep(1)
        # Clicks submit button
        resultsPage.clickElement(ResultsPageLocators.SignInContinueButton)
        time.sleep(1)

        # Adds class containing a locator to a variable
        self.signInPwdBox = TextElement(self.driver, ResultsPageLocators.SignInPwdBox)

        # Adds text to variables
        self.signInPwdBox.setValue(os.getenv("AMAZON_TEST_PASSWORD"))
        # Clicks submit button
        resultsPage.clickElement(ResultsPageLocators.SignInSubmitButton)
        # Verifies page displays "Hello, TestBot" header
        self.assertTrue(
            mainPage.elementMatches(MainPageLocators.HelloSignIn, "Hello, TestBot"),
            "No results found."
        )

        # Adds class containing a locator to a variable
        self.searchBox = TextElement(self.driver, MainPageLocators.SearchBox)

        # Adds text to variables
        self.searchBox.setValue("Bunny Phone Holder")
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        # Verifies that results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")
        time.sleep(1)
        # Clicks 3rd item on results page
        resultsPage.clickElement(ResultsPageLocators.ResultsItem)
        time.sleep(1)
        # Adds item to cart
        resultsPage.clickElement(ResultsPageLocators.AddToCartButton)
        time.sleep(1)

        # Adds text to variables
        self.searchBox.setValue("HDMI Cable 4K")
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        # Verifies that results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")
        time.sleep(1)
        # Clicks 3rd item on results page
        resultsPage.clickElement(ResultsPageLocators.ResultsItem)
        time.sleep(1)
        # Adds item to cart
        resultsPage.clickElement(ResultsPageLocators.AddToCartButton)
        time.sleep(1)

        # Adds text to variables
        self.searchBox.setValue("Divoom")
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        # Verifies that results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")
        time.sleep(1)
        # Clicks 3rd item on results page
        resultsPage.clickElement(ResultsPageLocators.ResultsItem)
        time.sleep(1)
        # Adds item to cart
        resultsPage.clickElement(ResultsPageLocators.AddToCartButton)
        time.sleep(1)
        # Declines protection plan pop up
        resultsPage.clickElement(ResultsPageLocators.NoThanksButton)

        time.sleep(2)
        # Clicks "Go to Cart" 
        resultsPage.clickElement(ResultsPageLocators.GoToCartButton)
        time.sleep(1)
        # Clicks "Proceed to checkout"
        resultsPage.clickElement(ResultsPageLocators.ProceedToCheckout)

        # Verifies results page displays "Select a shipping address" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.SelecAddressHeader, "Select a shipping address"), 
            "No results found."
            )


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
