import time
import unittest
from selenium import webdriver
from ObjClasses.page import MainPage
from Locators.locators import MainPageLocators


class Carousel(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("https://www.amazon.com/")

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Verifies if the word "Amazon" is in title
        self.assertTrue(mainPage.titlematchesAmazon(), "Title doesn't match.")


    # Clicks the carousel Arrows, verifies there is an image container
    def testArrows(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)

        # Runs this block of code 3 times
        for i in range(3):
            
            # Clicks right next arrow
            mainPage.clickElement(MainPageLocators.RightArrow)
            time.sleep(1)
            # Verifies carousel container exists
            self.assertTrue(
                mainPage.elementDisplays(MainPageLocators.CarouselContainer), 
                "No results found."
                )
            time.sleep(1)

        # Runs this block of code 3 times
        for i in range(3):

            # Clicks left previous arrow
            mainPage.clickElement(MainPageLocators.LeftArrow)
            time.sleep(1)
            # Verifies carousel container exists
            self.assertTrue(
                mainPage.elementDisplays(MainPageLocators.CarouselContainer), 
                "No results found."
                )
            time.sleep(1)

        # Note: Using carousel container to verify because images on website are not static...
        # With internal API access I could verify the actual images.


    # Clicks the three images on the carousel, uses the driver to navigate back to the carousel
    def testImages(self):

        # Variable that contains the functionality needed to verify and interact with the page
        mainPage = MainPage(self.driver)
            
        # Clicks first visible image
        mainPage.clickElement(MainPageLocators.CarouselContainer)
        time.sleep(1)
        # Tells driver to go back a page
        self.driver.back()
        # Clicks the right next arrow
        mainPage.clickElement(MainPageLocators.RightArrow)
        time.sleep(1)
        # Clicks second visible image
        mainPage.clickElement(MainPageLocators.CarouselContainer)
        time.sleep(1)
        # Tells driver to go back a page
        self.driver.back()
        # Clicks right next arrow twice
        mainPage.clickElement(MainPageLocators.RightArrow)
        mainPage.clickElement(MainPageLocators.RightArrow)
        time.sleep(1)
        # Clicks third final visible image in the carousel
        mainPage.clickElement(MainPageLocators.CarouselContainer)
        time.sleep(1)
        # Tells driver to go back a page
        self.driver.back()


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
