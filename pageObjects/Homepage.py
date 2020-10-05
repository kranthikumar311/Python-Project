from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop)

    def getname(self):
        return self.driver.find_element(*HomePage.name)

    def getemail(self):
        return self.driver.find_element(*HomePage.email)

    def getgender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitbutton(self):
        return self.driver.find_element(*HomePage.submit)

    def getalerttext(self):
        return self.driver.find_element(*HomePage.alert)




