from selenium import webdriver
from selenium.webdriver.support.select import Select
import pytest

from TestData.HomePageData import HomePageData
from Utilities.BaseClass import BaseClass
from pageObjects.Homepage import HomePage


class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):
        log = self.getlogger()
        homepage = HomePage(self.driver)
        log.info("FIRSTNAME :"+getData["firstname"])
        log.info("EMAIL :" + getData["email"])
        homepage.getname().send_keys(getData["firstname"])
        homepage.getemail().send_keys(getData["email"])
        sel = Select(homepage.getgender())
        sel.select_by_visible_text("Female")
        homepage.submitbutton().click()
        message = homepage.getalerttext().text
        log.info(message)
        assert ("success" in message)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def getData(self, request):
        return request.param

