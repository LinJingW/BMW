import unittest
from appium import webdriver
from PrivacyScreen import AcceptPrivacy
from AcceptPrivacy import AcceptPrivacy
from LoginScreen import LogIn
from LoginScreen.LogIn import LogIn
from TestData import UserInfo


class LoginTest(unittest.TestCase):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'Galaxy J5'
    desired_caps['appPackage'] = 'de.bmw.connected.cn.int'
    desired_caps['appActivity'] = 'de.bmw.connected.lib.startup.views.StartupActivity'
    desired_caps['autoAcceptAlert'] = 'True'
    desired_caps['autoGrantPermission'] = 'True'

    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(60)
        # self.driver.switch_to.alert.accept()
        self.AcceptPrivacy = AcceptPrivacy(self.driver)
        self.AcceptPrivacy.tapCheckBox()
        self.AcceptPrivacy.tapAcceptBtn()
        self.AcceptPrivacy.tapskipbutton()
        self.logIn = LogIn(self.driver)

    def tearDown(self):
        self.driver.quit()

    # 1.correct account + correct password
    def test_LoginScreenInitState(self):
        self.assertTrue(self.logIn.AccountTxtBox().is_displayed())
        self.logIn.AccountTxtBox().send_keys(UserInfo.valid_user)
        self.assertTrue(self.logIn.PwdTxtBox().is_displayed())
        self.logIn.PwdTxtBox().send_keys(UserInfo.valid_password)
        self.logIn.loginButton().click()
        self.driver.implicitly_wait(30)
        count = 0
        while count < 8:
            self.logIn.enterPin()
            count = count + 1

    if __name__ == '__main__':
        unittest.main(verbosity=2)
    # suite = unittest.testSuite()
