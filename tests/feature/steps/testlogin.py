from behave import given, then, when
from src.Pages.Pages import LoginPage
from unittest import TestCase
from hamcrest import assert_that, equal_to


class testLogin(TestCase):

    @then(u'I will be in the login page')
    def step_impl(context):
        assert (context.browser.title == "Login - My Store")

    @given(u'I am currently at login page')
    def step_impl(context):
        context.home_page.goToLoginPage()
        context.login_page = LoginPage(
            context.browser, context.browser.current_url)

    @when(u'I tipe a valid e-mail: "admin@test.com"')
    def step_impl(context):
        context.login_page.fillEmail("admin@test.com")

    @when(u'type the corresponding password "admin"')
    def step_impl(context):
        context.login_page.fillPassword("admin")

    @then(u'I will be in the account page')
    def step_impl(context):
        context.home_page.logout()

    @when(u'type the wrong password "123"')
    def step_impl(context):
        context.login_page.fillPassword("123")

    @when(u'submit login form')
    def step_impl(context):
        context.login_page.submitLogin()

    @then(u'the correct error message {text} should be displayed')
    def step_impl(context, text):
        alert = context.login_page.locateErrors(context.browser)
        assert_that(text, equal_to(alert))
