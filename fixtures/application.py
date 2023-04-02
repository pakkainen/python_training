from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.group import GroupHelper
from fixtures.contact import ContactHelper
import os

install_dir = "/snap/firefox/current/usr/lib/firefox"
# driver_loc = os.path.join(install_dir, "geckodriver")
binary_loc = os.path.join(install_dir, "firefox")

opts = webdriver.FirefoxOptions()
opts.binary_location = binary_loc


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(options=opts)
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        # self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
