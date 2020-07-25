from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Firefox()
    print("before_all activated")


def after_all(context):
    context.browser.quit()
    print("after_all activated")
