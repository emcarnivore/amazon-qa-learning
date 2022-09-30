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


    # TODO: Tests here...
        


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
