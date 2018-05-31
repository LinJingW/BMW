from appium import webdriver

desired_caps = { }
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '5.1'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'de.bmw.connected.cn.int'
desired_caps['appActivity'] = 'de.bmw.connected.lib.startup.views.StartupActivity'
desired_caps['autoAcceptAlert'] = 'True'
desired_caps['autoGrantPermission'] = 'True'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
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

# 1.input the pin code , click 1 four times
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()

# 2.double click pin again.
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()
driver.find_element_by_id(
    "de.bmw.connected.cn.int:id/pin_code_button_1"
).click()