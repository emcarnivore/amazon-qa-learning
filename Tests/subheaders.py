import time
import unittest
from selenium import webdriver
from ObjClasses.page import MainPage, ResultsPage
from Locators.locators import MainPageLocators, ResultsPageLocators


class SubHeaders(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Clicks "All" hamburger menu, clicks "Hello, Sign in", verifies results page displays "Sign-In"
    def testA_HamburgerHelloSignIn(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "All" hamburger menu
        mainPage.clickElement(MainPageLocators.AllHamburgerMenu)
        time.sleep(1)
        # Clicks "Hello, Sign in" header
        mainPage.clickElement(MainPageLocators.HamburgerHelloSignIn)
        time.sleep(1)
        # Verifies results page displays "Sign-In" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.SignInHeader, "Sign-In"), 
            "No results found."
            )

        
    # Clicks "Best Sellers", verifies results page displays "Amazon Best Sellers"
    def testB_HamburgerBestSellers(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "All" hamburger menu
        mainPage.clickElement(MainPageLocators.AllHamburgerMenu)
        time.sleep(1)
        # Verifies menu displays "Trending" subheader
        self.assertTrue(
            mainPage.elementMatches(MainPageLocators.HamburgerTrendingSubHeader, "Trending"), 
            "No results found."
            )

        #Clicks "Best Sellers"
        mainPage.clickElement(MainPageLocators.HamburgerBestSellers)
        time.sleep(1)
        # Verifies results page displays "Amazon Best Sellers" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.AmazonBestSellersHeader, "Amazon Best Sellers"), 
            "No results found."
            )
            

    # Clicks "New Releases", verifies results page displays "Amazon Hot New Releases"
    def testC_HamburgerNewReleases(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "All" hamburger menu
        mainPage.clickElement(MainPageLocators.AllHamburgerMenu)
        time.sleep(1)
        # Verifies menu displays "Trending" subheader
        self.assertTrue(
            mainPage.elementMatches(MainPageLocators.HamburgerTrendingSubHeader, "Trending"), 
            "No results found."
            )

        #Clicks "New Releases"
        mainPage.clickElement(MainPageLocators.HamburgerNewReleases)
        time.sleep(1)
        # Verifies results page displays "Amazon Hot New Releases" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.AmazonHotNewReleasesHeader, "Amazon Hot New Releases"), 
            "No results found."
            )


    # Clicks "Movers & Shakers", verifies results page displays "Amazon Movers & Shakers"
    def testD_HamburgerMoversShakers(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "All" hamburger menu
        mainPage.clickElement(MainPageLocators.AllHamburgerMenu)
        time.sleep(1)
        # Verifies menu displays "Trending" subheader
        self.assertTrue(
            mainPage.elementMatches(MainPageLocators.HamburgerTrendingSubHeader, "Trending"), 
            "No results found."
            )

        # Clicks "Movers & Shakers"
        mainPage.clickElement(MainPageLocators.HamburgerMoversShakers)
        time.sleep(1)
        # Verifies results page displays "Amazon Movers & Shakers" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.AmazonMoversShakersHeader, "Amazon Movers & Shakers"), 
            "No results found."
            )


    # TODO: Test more elements in "All" hamburger menu


    # Clicks "Amazon Basics", verifies results page displays "Amazon Basics"
    def testE_AmazonBasics(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "Amazon Basics"
        mainPage.clickElement(MainPageLocators.AmazonBasics)
        time.sleep(1)
        # Verifies results page displays "Amazon Basics" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.AmazonBasicsHeader, "Amazon Basics"), 
            "No results found."
            )


    # Clicks "Customer Service", verifies results page displays "Welcome to Amazon Customer Service"
    def testF_CustomerService(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Clicks "Customer Service"
        mainPage.clickElement(MainPageLocators.CustomerService)
        time.sleep(1)
        # Verifies results page displays "Welcome to Amazon Customer Service" header
        self.assertTrue(
            resultsPage.elementMatches(ResultsPageLocators.AmazonCustServiceHeader, "Welcome to Amazon Customer Service"), 
            "No results found."
            )


    # Hovers over "Prime", verifies "Try Prime" displays
    # Clicks "Prime", verifies Prime logo displays, clicks on "Try Prime FREE"
    def testG_Prime(self):

        # Variables that contain functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
        resultsPage = ResultsPage(self.driver)

        # Hovers over "Prime"
        mainPage.hoverOver(MainPageLocators.Prime)
        time.sleep(1)
        # Verifies hover window displays "Try Prime" anchor
        self.assertTrue(
            mainPage.elementMatches(MainPageLocators.TryPrimeAnchor, "Try Prime"), 
            "No results found."
            )

        # Clicks "Prime"
        mainPage.clickElement(MainPageLocators.Prime)
        time.sleep(1)
        # Verifies results page displays "Prime" logo
        self.assertTrue(
            resultsPage.elementDisplays(ResultsPageLocators.PrimeLogo), 
            "No results found."
            )

        resultsPage.clickElement(ResultsPageLocators.TryPrimeSubmitButton)
        time.sleep(1)


    # TODO: Test more elements on navigation subheaders bar


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
