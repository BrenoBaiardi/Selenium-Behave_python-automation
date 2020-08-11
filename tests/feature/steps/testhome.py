from behave import given, then, when
from src.Pages.Pages import ProductPage
from hamcrest import assert_that, equal_to, not_


@given(u'I am currently at home page')
def step_impl(context):
    context.home_page.open()
    assert_that(context.browser.title, equal_to("My Store"))


@when(u'I click the sign in button')
def step_impl(context):
    context.home_page.goToLogin()


@given(u'the cart is empty')
def step_impl(context):
    assert_that(context.home_page.checkCartQuantity(context.browser),
                equal_to(""))


@when(u'I click add to cart button in a product')
def step_impl(context):
    raise NotImplementedError(
        u'STEP: Then the cart need to recieve the product')


@ then(u'the cart need to have only one product')
def step_impl(context):
    context.home_page.open()
    print(context.home_page.checkCartQuantity(context.browser))


@ given(u'I add something to the cart')
def step_impl(context):
    context.home_page.open()
    product = context.home_page.products[0]
    product.click()
    prod_page = ProductPage(context.browser, context.browser.current_url)
    prod_page.add_to_cart(1, "L")


@ given(u'the cart is not empty')
def step_impl(context):
    #assert context.home_page.span_empty_cart.text != "(empty)"
    assert_that(context.home_page.checkCartQuantity(context.browser),
                not_(""))


@ then(u'the cart need to recieve the product')
def step_impl(context):
    assert_that(context.home_page.checkCartQuantity(context.browser),
                equal_to("3"))
