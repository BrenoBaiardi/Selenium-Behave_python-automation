from behave import given, then, when


@given(u'I am currently at home page')
def step_impl(context):
    # context.browser.get("http://automationpractice.com/index.php")
    context.home_page.get('')


@given(u'the cart is empty')
def step_impl(context):
    assert context.home_page.empty_cart_span.text == "(empty)"


@when(u'I click add to cart button in a product')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: When I click add to cart button in a product')


@then(u'the cart need to have only one product')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the cart need to have only one product')


@given(u'I add something to the cart')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I add something to the cart')


@given(u'the cart is not empty')
def step_impl(context):
    assert context.home_page.empty_cart_span.text != "(empty)"


@then(u'the cart need to recieve the product')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the cart need to recieve the product')
