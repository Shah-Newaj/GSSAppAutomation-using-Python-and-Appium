import time
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    "platformName": "android",
    "automationName": "UIAutomator2",
    "deviceName": "android",
    # "appPackage": "com.socialnmobile.dictapps.notepad.color.note",
    # "appActivity": "com.socialnmobile.colornote.activity.Main",
    "language": "en",
    "locale": "US"

}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(50)

wait = WebDriverWait(driver, timeout= 10)
# Click on APP
app = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@content-desc='StaySafe']")))
app.click()

#see different allocated views
time.sleep(10)
map_hospital_view = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Hospital View")
map_hospital_view.click()
time.sleep(5)
map_sci_office = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="SCI Office")
map_sci_office.click()
time.sleep(5)
map_danger_area = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Danger Area")
map_danger_area.click()
time.sleep(5)
map_grp_member_location = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Group Members Location")
map_grp_member_location.click()
time.sleep(5)

#Route Mapping
map_location_search = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Location Search")
map_location_search.click()
time.sleep(5)
destination = driver.find_element(by=AppiumBy.CLASS_NAME, value="android.widget.EditText")
destination.click()
time.sleep(5)
destination.send_keys("gulshan 2")
time.sleep(5)
destination.click()
time.sleep(5)
destination_address = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="গুলশান ২ \nগুলশান ২, গুলশান, ঢাকা, ঢাকা মহানগর, ঢাকা জেলা, ঢাকা বিভাগ, 1212, বাংলাদেশ \nquarter ")
destination_address.click()
time.sleep(10)
map_show_route = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Show Route")
map_show_route.click()
time.sleep(20)
el9 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]")
el9.click()
time.sleep(5)
el10 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id=\"android:id/content\"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]")
el10.click()
time.sleep(5)

#Panic Alert
tab_panic_alert = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Panic Alert\nTab 3 of 3")
tab_panic_alert.click()
time.sleep(10)
panic_accident = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Accident")
panic_accident.click()
time.sleep(5)

#Head Count
notification = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.FrameLayout[@resource-id='android:id/content']/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]")
notification.click()
time.sleep(5)
head_count = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Head Count")
head_count.click()
time.sleep(5)
response = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Danger Name : Head Count Tree 2")
response.click()
time.sleep(5)
el16 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Yes")
el16.click()

