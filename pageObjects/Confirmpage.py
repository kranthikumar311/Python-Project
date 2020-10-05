from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    countryNameTextbox = (By.ID, "country")
    countryName = (By.LINK_TEXT, "India")
    successButton = (By.CSS_SELECTOR, "[class*='btn-lg']")
    successText = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")

    def getCountryTextBox(self):
        return self.driver.find_element(*ConfirmPage.countryNameTextbox)

    def getCountryName(self):
        return self.driver.find_element(*ConfirmPage.countryName)

    def success(self):
        return self.driver.find_element(*ConfirmPage.successButton)

    def getSuccessText(self):
        return self.driver.find_element(*ConfirmPage.successText)


