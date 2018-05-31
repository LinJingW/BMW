# -*- coding: utf-8 -*-


class LogIn():
    def __init__(self, driver):
        # type: (object) -> object
        self.driver = driver

    def AccountTxtBox(self):
            return self.driver.find_element_by_id(
                "de.bmw.connected.cn.int:id/connected_drive_phone_number_edit_text"
            )

    def PwdTxtBox(self):
            return self.driver.find_element_by_id(
                "de.bmw.connected.cn.int:id/password_edit_text"
            )

    def loginButton(self):
            return self.driver.find_element_by_id(
                "de.bmw.connected.cn.int:id/login_button"
            )

    def forgetPwdLink(self):
            return self.driver.find_element_by_id(
                "de.bmw.connected.cn.int:id/forgot_password_button"
            )

    def createNewUser(self):
            return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/create_account_button")

    def pinCode(self):
        return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/pin_code_button_1")

    def enterPin(self):
        self.pinCode().click()