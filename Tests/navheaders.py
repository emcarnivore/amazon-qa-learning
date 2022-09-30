import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ObjClasses.page import MainPage, ResultsPage, TextElement
from Locators.locators import MainPageLocators, ResultsPageLocators


class NavHeaders(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Clicks Amazon navigation logo, verifies it takes you to the Home Page
    def testAmazonNavLogo(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Clicks Amazon navigation logo
        mainPage.clickElement(MainPageLocators.AmazonNavLogo)
        # Verifies that the results page is not empty
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Clicks "Select your address", verifies pop up window displays "Choose your location"
    def testSelectYourAddress(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Clicks "Select your address"
        mainPage.clickElement(MainPageLocators.SelectYourAddress)
        # Verifies pop up window displays "Choose your location" header
        self.assertTrue(
            mainPage.elementMatches(MainPageLocators.ChooseYourLocationHeader, "Choose your location"),
            "No results found."
            )
            
    # TODO: Test more elements on "Choose your location" window
    

    # Clicks language settings Flag, verifies results page displays "Language Settings"
    def testLanguageSettings(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Hovers over Flag
        mainPage.hoverOver(MainPageLocators.LanguageSettingsFlag)
        time.sleep(1)
        # Clicks Flag
        mainPage.clickElement(MainPageLocators.LanguageSettingsFlag)
        # Verifies results page displays "Language Settings" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.LanguageSettingsHeader, "Language Settings"), 
            "No results found."
            )


    # Clicks "Learn more" link, verifies results page displays "Help & Customer Service"
    def testLanguageSettingsLearnMore(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Hovers over Flag
        mainPage.hoverOver(MainPageLocators.LanguageSettingsFlag)
        time.sleep(1)
        # Clicks "Learn more" link
        mainPage.clickElement(MainPageLocators.LearnMoreLink)
        # Verifies results window displays "Help & Customer Service" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.HelpCustomerServiceHeader, "Help & Customer Service"), 
            "No results found."
            )

    
    # TODO: Test more elements on language settings Flag hover window

    
    # Hovers over "Hello, Sign in", verifies "Sign in" displays
    # Clicks "Hello, Sign in", verifies results page displays "Sign-In"
    def testHelloSignIn(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Hovers over "Hello, Sign in"
        mainPage.hoverOver(MainPageLocators.HelloSignIn)
        time.sleep(1)
        # Verifies "Sign in" submit button displays
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


    # Clicks "Returns & Orders", verifies results page displays "Sign-In"
    def testReturnsOrders(self):
        
        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "Returns & Orders"
        mainPage.clickElement(MainPageLocators.ReturnsOrders)
        # Verifies results page displays "Sign-In" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.SignInHeader, "Sign-In"), 
            "No results found."
            )


    # Clicks empty "Cart", verifies cart displays "Your Amazon Cart is empty"
    def testCart(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "Cart" 
        mainPage.clickElement(MainPageLocators.Cart)
        # Verifies results page displays "Your Amazon Cart is empty" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.CartEmptyText, "Your Amazon Cart is empty"), 
            "No results found."
            )


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
