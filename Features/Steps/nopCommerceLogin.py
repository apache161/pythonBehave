from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'Launch the Chrome Browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\syede\\Downloads\\Learning\\Drivers\\chromedriver.exe")

@when(u'nopCommerce is launched')
def nopCommerceLaunched(context):
    context.driver.get("https://admin-demo.nopcommerce.com/")

@when(u'Enter Username "{user}" and Password "{password}" in nopCommerce LoginPage')
def enterLoginInfo(context, user, password):
    context.driver.find_element(By.XPATH, "//input[@id='Email']").clear()
    context.driver.find_element(By.XPATH, "//input[@id='Email']").send_keys(user)
    context.driver.find_element(By.XPATH, "//input[@id='Password']").clear()
    context.driver.find_element(By.XPATH, "//input[@id='Password']").send_keys(password)

@when(u'Click on LoginButton')
def clickLogin(context):
    context.driver.find_element(By.XPATH, "//button[text()='Log in']").click()

@then(u'User should be able to successful login into nopCommerce website')
def verifySuccessfulLogin(context):
    try:
        status = context.driver.find_element(By.XPATH, "//div[@class='content-header']/h1").text # if login successful, then grab title
    except: #except block to close driver and fail the test case if unsuccessful login
        context.driver.close()
        assert False, "Test failed" # comments as optional along with assert
    if status == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"


