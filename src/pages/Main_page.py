import time

from selene.support.conditions import be, have
from src.common_methods import move_to_element
from src.component.login_page import Login
from src.component.main_page import Main
from src.constants.timeout import MIDDLE_TIME_OUT


class MainPage(object):
    def __init__(self):
        self.main = Main()
        self.login = Login()

    def verify_table_visibility(self):
        self.main.sync_device_table.should(be.visible, MIDDLE_TIME_OUT)
        return self

    def _steps_for_creating_item_in_driver_table(self, item):
        # steps for creating new driver
        move_to_element(self.main.add_link)
        self.main.add_link.should(be.visible).click()
        self.main.add_online_drive_link.should(be.visible).click()
        # work with dialog alert
        self.main.modal_name_input.set_value(item)
        # verify that input contain expected test
        self.main.modal_name_input.should(have.value(item))
        self.main.modal_save_button.should(be.visible).click()

    def create_new_device(self, item):
        self.verify_table_visibility()
        self._steps_for_creating_item_in_driver_table(item)
        return self

    def log_out(self):
        move_to_element(self.main.header_setting_icon)
        self.main.header_setting_icon.should(be.visible).click()
        self.main.logout_alert_sign_out_button.should(be.visible).click()
        # check if 'sign in' tab is visible after we logged out
        self.login.sign_in_item.should(be.visible, MIDDLE_TIME_OUT)
        return self

    def _check_existed_items_in_driver_talbe(self, item):
        self.main.error_alert_popup.should(be.visible)
        # wait until element will be hidden
        self.main.error_alert_popup.should_not(be.visible)
        return self

    def check_exist_drive(self, item):
        # create new device
        self.create_new_device(item)
        # wait after device table will be rendered
        time.sleep(1)
        # create the same device
        self._steps_for_creating_item_in_driver_table(item)
        # check error message
        self._check_existed_items_in_driver_talbe(item)
        pass

    def delete_all_test_items_in_table(self):
        while True:
            # temporary solution for wait elements in table
            time.sleep(1)
            # get count of elements in drives table
            count = len(self.main.get_all_settings_icons())
            if count > 0:
                # delete element from table
                self.main.setting_icon.should(be.visible).click()
                self.main.modal_delete_icon.should(be.visible).click()
                self.main.confirm_delete_yes_button.should(be.visible).click()
                # check that collection equals count '-1'
                count -= 1
                self.main.get_all_settings_icons().should(have.size(count))
            else:
                break
