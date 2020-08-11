from selenium import webdriver
from src.Pages.Pages import HomePage, LoginPage


def before_all(context):
    context.browser = webdriver.Firefox(
        "/home/brenobaiardi/AME-Python/venv/bin/")
    context.browser.implicitly_wait(4)  # seconds


def before_feature(context, feature):
    context.home_page = HomePage(
        context.browser)


def after_all(context):
    context.browser.quit()
    #print("after_all activated")
