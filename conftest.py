import random
import string
import pytest
from webdriver_manager.driver import ChromeDriver
from src.constants.users import BY_DEFAULT
from src.pages.Login_page import LoginPage
from src.pages.Main_page import MainPage


# generate random names for devices
@pytest.fixture(scope="session")
def generate_new_value():
    list = [id_generator(), id_generator()]
    return list


# pre- & post- conditions to each test
@pytest.yield_fixture()
def browser():
    browser.driver = ChromeDriver(os_type="windows", version="latest")
    # login to keeptit
    LoginPage().open_url().login_as(user=BY_DEFAULT)
    # teardown method - delete all created test devices before test starts
    MainPage().delete_all_test_items_in_table()
    b = {}
    yield b
    # teardown method - delete all created test devices after test is completed
    MainPage().delete_all_test_items_in_table()
    MainPage().log_out()


def id_generator(size=3, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
