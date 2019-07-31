from selenium.webdriver.android.webdriver import WebDriver
from fixture.sessions import SessionHelper


class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        wd.get("https://spycloud.com/")

    def navigate_to_customer_portal(self):
        wd = self.wd
        wd.find_element_by_xpath("//a[.='Email Addresses']").click()
        # Here test@example could be passed thru variable %s
        wd.find_element_by_xpath("//a[.='test@example.com']").click()

    def switch_show_passwords_toggle(self):
        wd = self.wd
        wd.find_element_by_css_selector(".switchery-small").click()