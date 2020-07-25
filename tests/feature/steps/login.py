from behave import given, then, when


@given('I am currently at {link}')
def step_impl(context, link):
    context.browser.get(link)
    pass
    # assert (context.browser.title == "My Store")


@when(u'I click the "sign in button"')
def step_impl(context):
    pass


@then(u'I will be in the login page')
def step_impl(context):
    pass
