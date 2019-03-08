from selene import browser
from selene.support.conditions import be

from src.component.login_page import Login
from src.pages.Main_page import MainPage


class LoginPage(object):
    def __init__(self):
        self.login = Login()

    def open_url(self):
        browser.open_url('/')
        return self

    def login_as(self, user):
        self.login.login_input.should(be.visible).set(user.email)
        self.login.password_input.should(be.visible).set(user.password)
        self.login.sign_in_button.should(be.clickable).click()
        return MainPage()



