from selene.support.jquery_style_selectors import s


class Login(object):

    def __init__(self):
        # login form elements
        self.login_input = s('#login-form-login')
        self.password_input = s('#login-form-password')
        self.sign_in_button = s('#login-form-login-button')

        # keeptit html main page
        self.nav_bar = s('.nav.navbar-nav')
        self.sign_in_item = self.nav_bar.s('#signin-page')
