from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('launch firefox browser')
def launchBrowser(context):
    context.driver = webdriver.Firefox()


@when('open orange hrm hompage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com")
    time.sleep(5)

@then('verify that the logo present on page')
def verifyLogo(context):
    status = context.driver.find_element(By.XPATH,"//div[@class='orangehrm-login-branding']").is_displayed()
    assert status is True



@then('close browser')
def closeBrowser(context):
    context.driver.close()


