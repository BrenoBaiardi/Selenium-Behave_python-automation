from behave import given, then, when
from src.Pages.Pages import ProductPage


@given(u'I am currently at home page')
def step_impl(context):
    context.home_page.get('')


@given(u'the cart is empty')
def step_impl(context):
    assert context.home_page.span_empty_cart.text == "(empty)"


@when(u'I click add to cart button in a product')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the cart need to recieve the product')


@then(u'the cart need to have only one product')
def step_impl(context):
    context.home_page.get('')
    print(context.home_page.checkCartQuantity())


@given(u'I add something to the cart')
def step_impl(context):
    product = context.home_page.products[0]
    product.click()
    prod_page = ProductPage(context.browser, context.browser.current_url)
    prod_page.add_to_cart(1, "L")


@given(u'the cart is not empty')
def step_impl(context):
    assert context.home_page.span_empty_cart.text != "(empty)"


@then(u'the cart need to recieve the product')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the cart need to recieve the product')
