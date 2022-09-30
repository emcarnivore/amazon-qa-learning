import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ObjClasses.page import MainPage, ResultsPage, TextElement
from Locators.locators import MainPageLocators, ResultsPageLocators


class TestBench(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Searches for item, adds to cart, verifies cart displays "Subtotal (1 item):"
    def testCart1Item(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Adds class containing a locator to a variable
        self.searchBox = TextElement(self.driver, MainPageLocators.SearchBox)
        
        # Adds text to variables
        self.searchBox.setValue("Cute Bunny Phone Holder")
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        # Verifies that results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")

        # Clicks 3rd item on results page
        resultsPage.clickElement(ResultsPageLocators.ResultsItem)
        time.sleep(1)
        # Adds item to cart
        resultsPage.clickElement(ResultsPageLocators.AddToCartButton)
        time.sleep(1)
        # Clicks cart 
        mainPage.clickElement(MainPageLocators.Cart)
        time.sleep(1)

        # Verifies results page displays "Shopping Cart" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.ShoppingCartHeader, "Shopping Cart"), 
            "No results found."
            )

        # Verifies results page displays "Subtotal (1 item)"
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.SubtotalXItems, "Subtotal (1 item):"), 
            "No results found."
            )


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
