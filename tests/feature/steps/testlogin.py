from behave import given, then, when
from src.Pages.Pages import HomePage


"""@given(u'I am currently at home page')
def step_impl(context):
    # context.browser.get("http://automationpractice.com/index.php")
    home_page = HomePage(
        context.browser, "http://automationpractice.com/index.php")
"""


@when(u'I click the sign in button')
def step_impl(context):
    btn_login = context.browser.find_element_by_css_selector('a.login')
    btn_login.click()


@then(u'I will be in the login page')
def step_impl(context):
    assert (context.browser.title == "Login - My Store")
