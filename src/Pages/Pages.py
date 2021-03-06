
from page_objects import PageElement, PageObject, MultiPageElement
import time


class StorePage(PageObject):
    span_empty_cart = PageElement(class_name="ajax_cart_no_product")
    btn_sign_in = PageElement(css="a.login")
    btn_logout = PageElement(css=".logout")
    cart_quantity = '0'
    url = "http://automationpractice.com"

    def checkCartQuantity(self, browser):
        self.cart_quantity = browser.find_element_by_css_selector(
            "span.ajax_cart_quantity:nth-child(2)").text
        return self.cart_quantity

    def goToLoginPage(self):
        self.btn_sign_in.click()

    def open(self):
        self.w.get(self.url)

    def logout(self):

        self.btn_logout.click()


class LoginPage(StorePage):
    input_email = PageElement(id_="email")
    input_passwd = PageElement(id_="passwd")
    btn_submit_login = PageElement(id_="SubmitLogin")
    span_empty_cart = PageElement(class_name="ajax_cart_no_product")
    alert = None
    url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"

    def fillPassword(self, password):
        self.input_passwd.send_keys(password)

    def fillEmail(self, email):
        self.input_email.send_keys(email)

    def submitLogin(self):
        self.btn_submit_login.click()

    def locateErrors(self, browser):
        self.alert = browser.find_elements_by_tag_name(
            "li")
        # self.alert = PageElement(class_name="alert")
        # for i in self.alert:
        #    print(i.text)
        #    if i.text == "An email address required.":
        #        print("pimba")
        return self.alert[14].text  # the only way i could find to do this


class HomePage(StorePage):
    products = MultiPageElement(class_name="product-container")
    btn_sign_in = PageElement(css="a.login")
    url = "http://automationpractice.com/index.php"

    def goToLogin(self):
        self.btn_sign_in.click()


class ProductPage(StorePage):
    btn_add_to_cart = PageElement(css="button.exclusive")
    input_quantity = PageElement(id_="quantity_wanted")
    option_size = PageElement(id_="group_1")
    url = "http://automationpractice.com/index.php?id_product=1&controller=product"
    # not sure this is the right way to create a product page
    # because the url is actually the index page referencing the product id

    def add_to_cart(self, quantity=1, size="S"):
        self.input_quantity.clear()
        self.input_quantity.send_keys(quantity)
        self.option_size.send_keys(size)
        self.btn_add_to_cart.click()
        time.sleep(3)
