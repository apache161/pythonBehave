from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'Launch Chrome Browser')
def launchChromeBrowser(context):
    context.driver = webdriver.Chrome(executable_path="C:\\Users\\syede\\Downloads\\Learning\\Drivers\\chromedriver.exe")

@when(u'nopCommerce launched')
def logineCommercePage(context):
   context.driver.get("https://admin-demo.nopcommerce.com/")


@then(u'Verify LogoPage of nopCommerce')
def verifyLogo(context):
    print("title of the page : ", context.driver.title)
    status = context.driver.find_element(By.XPATH, "//div[@class ='page-title']/h1").is_displayed()
    assert status is True
    #print(status)
    #assert status is True

@then(u'close Browser')
def closeBrowser(context):
    context.driver.close()

