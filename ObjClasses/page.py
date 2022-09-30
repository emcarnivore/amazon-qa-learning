from selenium.webdriver.common.action_chains import ActionChains
from Elements.elements import BasePageElement


# Gets text from the specified locator
class TextElement(BasePageElement):

    pass

# Base class to initialize the base page that will be called from all pages
class BasePage(object):

    def __init__(self, driver):

        self.driver = driver

     # Clicks element
    def clickElement(self, locator):

        element = self.driver.find_element(*locator)
        element.click()

    # Hovers over element
    def hoverOver(self, locator):

        element = self.driver.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # Uses key(s) on element
    def sendKeys(self, locator, keys):

        element = self.driver.find_element(*locator)
        element.send_keys(*keys)

    # Verifies element matches the text
    def elementMatches(self, locator, text):

        element = self.driver.find_element(*locator)
        return text in element.text

    # Verifies element displays or is present
    def elementDisplays(self, locator):

        element = self.driver.find_element(*locator)
        return element.is_displayed()

    #


# Home page action methods
class MainPage(BasePage):

    # Verifies that the hardcoded text "Amazon" appears in page title
    def titlematchesAmazon(self):

        return "Amazon" in self.driver.title

    # 


# Results page action methods
class ResultsPage(BasePage):

    def resultsFound(self):

        return "No results for " not in self.driver.page_source

    # 
