import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# @pytest.mark.usefixtures("setup")
from Utilities.BaseClass import BaseClass
from pageObjects.Checkoutpage import CheckOutPage
from pageObjects.Confirmpage import ConfirmPage
from pageObjects.Homepage import HomePage


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        checkoutpage = CheckOutPage(self.driver)
        confirmpage = ConfirmPage(self.driver)
        homepage.shopItems().click()
        cards = checkoutpage.getCardTitles()
        i = - 1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.getCardFooter()[i].click()
        checkoutpage.getCheckOutItems().click()
        checkoutpage.ConfirmCheckout().click()
        confirmpage.getCountryTextBox().send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        confirmpage.getCountryName().click()
        confirmpage.success().click()
        log.info("--Submitting the Form--")
        msg = confirmpage.getSuccessText().text
        log.info("--Success Message--: " + msg)
        assert "Success" in msg
