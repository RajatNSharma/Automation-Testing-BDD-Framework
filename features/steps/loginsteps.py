from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
import time

# @given('launch firefox browser')
# def launchBrowser(context):
#     context.driver = webdriver.Firefox()
#
#
# @when('open orange hrm hompage')
# def openHomePage(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com")
#     time.sleep(5)

@when('Enter username "{user}" and password "{pwd}"')
def Enter_usrname_pass(context,user,pwd):
    context.driver.find_element(By.NAME,"username").send_keys(user)
    context.driver.find_element(By.NAME,"password").send_keys(pwd)

@when('Click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(5)


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text = context.driver.find_element(By.CSS_SELECTOR,"div.oxd-layout div.oxd-layout-navigation header.oxd-topbar div.oxd-topbar-header div.oxd-topbar-header-title > span.oxd-topbar-header-breadcrumb").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"



