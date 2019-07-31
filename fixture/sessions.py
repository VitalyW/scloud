import time


"""
This is a helper class that is responsible for the session itself
highlevel actions like login and logout

In the constructor im passing in a reference to the fixture
"""
class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        # Remove sleep
        time.sleep(5)
        wd.find_element_by_xpath(
            "//li[@class='menu-item-18 contact menu-item menu-item-type-custom menu-item-object-custom sf-std-menu']").click()
        wd.find_element_by_css_selector("[type='email']").send_keys(username)
        wd.find_element_by_css_selector("[type='password']").send_keys(password)
        wd.find_element_by_css_selector("[type='submit']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_css_selector(".profile-address").click()
        wd.find_element_by_xpath("//*[contains(text(), 'Logout')]").click()