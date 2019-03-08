from conftest import generate_new_value
from src.pages.Main_page import MainPage


class TestAddNewItems:

    def test_create_new_drive_item(self, browser, item=generate_new_value()[0]):
        MainPage().create_new_device(item)

    def test_check_existent_drive_item(self, browser, item=generate_new_value()[1]):
        MainPage().check_exist_drive(item)
