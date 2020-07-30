from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()

browser.get('http://web.whatsapp.com/')
time.sleep(30)

messager = browser.find_element_by_class_name(
    "_3FRCZ copyable-text selectable-text")
send_button = browser.find_element_by_class_name("_1U1xa")

messager.send_keys("testando boot" + Keys.RETURN)

send_button.click()

# elem = browser.find_element_by_name('p')  # Find the search box
# elem.send_keys('seleniumhq' + Keys.RETURN)

# browser.quit()