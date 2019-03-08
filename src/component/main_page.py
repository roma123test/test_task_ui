from selene.support import by
from selene.support.jquery_style_selectors import s, ss


class Main(object):

    def __init__(self):
        # header section
        self.header_wrap = s('.navigation-menu')
        self.header_logo = self.header_wrap.s('.logo')
        self.header_setting_icon = self.header_wrap.s('.settings')

        # table with online devices
        self.sync_device_table = s("#sync-devices")
        self.all_add_link = ss('#sync-devices-button')
        self.add_link = s('#sync-devices-button')
        self.setting_icon = s('.edit-device-menu-item.edit-item')

        # add online drive drop-down
        self.add_online_drive_link = s('.open').s(by.text('Online Drive'))
        self.all_add_dropdown_open = ss('.dropdown-menu .drive-device')

        # modal window 'create new item'
        self.modal_wrap = s('.modal.in')
        self.modal_name_input = self.modal_wrap.s('#name')
        self.modal_save_button = self.modal_wrap.s('.btn-success')
        self.modal_delete_icon = self.modal_wrap.s('.delete-item')

        # modal alert for confirm delete item
        self.confirm_delete_yes_button = s(by.xpath("//a[contains(@id, 'yes-button')]"))

        # error message popup
        self.error_alert_popup = s('.message.alert.alert-error')

        # header logout alert
        self.logout_alert = self.header_setting_icon.s('.open .dropdown-menu')
        self.logout_alert_sign_out_button = self.logout_alert.s('#logout')

    def get_all_settings_icons(self):
        return ss('.edit-device-menu-item')
