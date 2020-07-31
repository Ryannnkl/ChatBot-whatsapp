from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

import time


class Chatbot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def openBrowser(self):
        print("[] opening web site")
        self.driver.get("https://web.whatsapp.com")
        self.driver.maximize_window()

    def searchContact(self, name):
        person = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//span[@title='{name}']")))
        person.click()
        print("[] Usuario encontrado")

    def SendSimpleMessage(self, message):
        input_chat = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_3uMse')))
        input_chat.click()
        # input_chat = self.driver.find_element_by_class_name('_3uMse')
        print("[] writing...")
        input_chat.send_keys(message + Keys.RETURN)
        time.sleep(2)
        # send_button = self.driver.find_element_by_xpath("//span[@data-icon='send']")
        # send_button = WebDriverWait(self.driver, 3).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, f"//span[@data-icon='send']")))
        # send_button.click()
        print("[] Sended message!")

    def SendLoopMessage(self, message, count):
        for i in range(count):
            input_chat = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_3uMse')))
            input_chat.click()
            print(f"[{i+1}] writing...")
            time.sleep(0.5)
            input_chat.send_keys(message + Keys.RETURN)
            time.sleep(0.5)
            print("[] sending message")
        print("[] end of messages")
