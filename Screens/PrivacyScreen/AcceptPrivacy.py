# -*- coding: utf-8 -*-


class AcceptPrivacy():
    def __init__(self, driver):
        self.driver = driver

    def termsofuse(self):
        return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/terms_of_use_button")

    def privacypolicy(self):
        return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/privacy_policy_button")

    def connecteddriveterms(self):
        return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/connected_drive_terms_button")

    def checkbox(self):
        return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/eula_read_terms_compound_button")

    def consentSwitch(self):
        return self.driver.find_element_by_accessibility_id("Consent Switch")

    def accpetbutton(self):
        return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/eula_accept_button")

    def skipbutton(self):
        return self.driver.find_element_by_id("de.bmw.connected.cn.int:id/skip_button")

    def tapskipbutton(self):
        self.skipbutton().click()

    def tapCheckBox(self):
        self.checkbox().click()

    def tapAcceptBtn(self):
        self.accpetbutton().click()
