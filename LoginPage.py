import time
from appium import webdriver
import HTMLTestRunner
import unittest


class LoginPage(unittest.TestCase):
    desired_caps = { }
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'de.bmw.connected.cn.int'
    desired_caps['appActivity'] = 'de.bmw.connected.lib.startup.views.StartupActivity'
    desired_caps['autoAcceptAlert'] = 'True'
    desired_caps['autoGrantPermission'] = 'True'

    def test_LogIn(self):
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.desired_caps)
        driver.implicitly_wait(60)
        driver.find_element_by_id("de.bmw.connected.cn.int:id/eula_read_terms_compound_button").click()
        driver.find_element_by_id("de.bmw.connected.cn.int:id/eula_accept_button").click()
        driver.find_element_by_id("de.bmw.connected.cn.int:id/skip_button").click()
        driver.implicitly_wait(30)
        driver.find_element_by_id(
            "de.bmw.connected.cn.int:id/connected_drive_phone_number_edit_text"
        ).send_keys("18701897255")

        driver.find_element_by_id(
            "de.bmw.connected.cn.int:id/password_edit_text"
        ).send_keys("1qaz2wsx")

        driver.find_element_by_id(
            "de.bmw.connected.cn.int:id/login_button"
        ).click()

        # 1.input the pin code
        count = 0
        while count < 8:
            driver.find_element_by_id(
                "de.bmw.connected.cn.int:id/pin_code_button_1"
            ).click()
            count = count + 1


if __name__ == '__main__':
        suite = unittest.makeSuite(LoginPage)
        # now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
        # path = "C:\\UIA\\AutomationTestResult\\"
        # filename = path + now + "_Report.html"
        filename = "C:\UIA\AutomationTestResult\\Report.html"
        fp = file(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=u'BMW Automation test result',
            description='TestReport',
            verbosity=2
        )
        runner.run(suite)