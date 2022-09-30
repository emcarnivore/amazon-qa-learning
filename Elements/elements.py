from selenium.webdriver.support.ui import WebDriverWait


# Base page class that is initialized on every page object class
class BasePageElement(object):

    def __init__(self, driver, locator):

        self.driver = driver
        self.locator = locator
    
    # Sets the value property of an element
    def setValue(self, value):

        driver = self.driver
        # Waits until element is found by locator with timeout
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )
        # Removes the value in the value property
        driver.find_element(*self.locator).clear()
        # Sets the value in the value property
        driver.find_element(*self.locator).send_keys(value)

    # Gets the value property of an element
    def getValue(self):

        driver = self.driver
        # Waits until element is found by locator with timeout
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )

        element = driver.find_element(*self.locator)
        # Returns the value of the value property
        return element.get_attribute("value")
    
    # Deletes the value property of an element
    def delValue(self):
        
        driver = self.driver
        # Waits until element is found by locator with timeout
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(*self.locator)
        )
        # Removes the value in the value property
        driver.find_element(*self.locator).clear()
