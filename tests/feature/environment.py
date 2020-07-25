from selenium import webdriver
from src.Pages.Pages import HomePage, LoginPage


def before_feature(context, feature):
    context.home_page = HomePage(
        context.browser, "http://automationpractice.com/index.php")
    #print("before_feature activated")


def before_all(context):
    context.browser = webdriver.Firefox()
    #print("before_all activated")


def after_all(context):
    context.browser.quit()
    #print("after_all activated")
