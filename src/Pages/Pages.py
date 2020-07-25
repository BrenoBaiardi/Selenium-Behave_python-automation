
from page_objects import PageElement, PageObject, MultiPageElement
from selenium import webdriver


class StorePage(PageObject):
    empty_cart_span = PageElement(class_name="ajax_cart_no_product")


class LoginPage(PageObject):
    input_email = PageElement(id_="email")
    input_passwd = PageElement(id_="passwd")
    btn_submit_login = PageElement(id_="SubmitLogin")
    empty_cart_span = PageElement(class_name="ajax_cart_no_product")

    def login(self):
        self.input_email.send_keys("email")
        self.input_passwd.send_keys("pw")
        self.btn_submit_login.click()


class HomePage(PageObject):
    products = MultiPageElement(class_name="product-container")
    empty_cart_span = PageElement(class_name="ajax_cart_no_product")


class ProductPage(StorePage):
    btn_add_to_cart = PageElement(css="button.exclusive")
    input_quantity = PageElement(id_="quantity_wanted")
    option_size = PageElement(id_="group_1")

    def add_to_cart(self, quantity=1, size="S"):
        self.input_quantity.clear()
        self.input_quantity.send_keys(quantity)
        self.option_size.send_keys(size)
        self.btn_add_to_cart.click()


browser = webdriver.Firefox()
'''
login_page = LoginPage(
    browser, "http://automationpractice.com/index.php?controller=authentication&back=my-account")
login_page.get('')
login_page.login()
'''

home_page = HomePage(
    browser, "http://automationpractice.com/index.php")
home_page.get('')
produto = home_page.products[0]
produto.click()

prod_page = ProductPage(
    browser, browser.current_url)

prod_page.add_to_cart(23, "L")
