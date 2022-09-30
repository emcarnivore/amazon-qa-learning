import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from ObjClasses.page import MainPage, ResultsPage, TextElement
from Locators.locators import MainPageLocators


class Search(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Adds class containing a locator to a variable
        self.searchBox = TextElement(self.driver, MainPageLocators.SearchBox)

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Searches for text in default "All Departments" using search button, verifies results are not empty
    def testA_SearchButton(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Games")
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchSubmitButton)
        time.sleep(1)
        #Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # Searches for text in default "All Departments" using Enter Key, verifies results are not empty
    def testB_SearchEnterKey(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Movies")
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        #Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # Searches for text in "Alexa Skills" drop down menu, verifies results are not empty
    def testSearchAlexaSkills(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Music")
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchDropDownMenu)
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchAlexaSkills)
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        # Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # Searches for text in "Amazon Devices" drop down menu, verifies results are not empty
    def testSearchAmazonDevices(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Fire Stick")
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchDropDownMenu)
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchAmazonDevices)
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        # Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # Searches for text in "Amazon Explore" drop down menu, verifies results are not empty
    def testSearchAmazonExplore(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Tokyo")
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchDropDownMenu)
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchAmazonExplore)
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        # Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # Searches for text in "Amazon Fresh" drop down menu, verifies results are not empty
    def testSearchAmazonFresh(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Cereal")
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchDropDownMenu)
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchAmazonFresh)
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        # Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # Searches for text in "Amazon Pharmacy" drop down menu, verifies results are not empty
    def testSearchAmazonPharmacy(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Ibuprofen")
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchDropDownMenu)
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchAmazonPharmacy)
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        # Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # Searches for text in "Amazon Warehouse" drop down menu, verifies results are not empty
    def testSearchAmazonWarehouse(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Searches for text
        self.searchBox.setValue("Amazon Basics")
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchDropDownMenu)
        time.sleep(1)
        mainPage.clickElement(MainPageLocators.SearchAmazonWarehouse)
        time.sleep(1)
        mainPage.sendKeys(MainPageLocators.SearchBox, (Keys.ENTER))
        time.sleep(1)
        # Verifies that the results page is not empty
        self.assertTrue(resultsPage.resultsFound(), "No results found.")


    # TODO: Test more elements in drop down menu
    

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
