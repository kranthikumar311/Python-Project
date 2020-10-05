from selenium.webdriver.common.by import By


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkoutsuccess = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def getCheckOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkout)

    def ConfirmCheckout(self):
        return self.driver.find_element(*CheckOutPage.checkoutsuccess)
