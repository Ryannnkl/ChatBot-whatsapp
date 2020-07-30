from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time


class Chatbot:
    def __init__(self, user):
        self.name = user
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def openBrowser(self):
        print("[] opening web site")
        self.driver.get("https://web.whatsapp.com")
        time.sleep(30)
        person = self.driver.find_element_by_xpath(
            f"//span[@title='{self.name}']")
        time.sleep(5)
        person.click()
        print("[] Usuario encontrado")
        time.sleep(3)

    def SendSimpleMessage(self, message):
        # <span dir="auto" title="Sininho" class="_3ko75 _5h6Y_ _3Whw5">
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        input_chat = self.driver.find_element_by_class_name('_3uMse')
        time.sleep(1)
        input_chat.click()
        print("digitando")
        input_chat.send_keys(message)
        send_button = self.driver.find_element_by_xpath(
            "//span[@data-icon='send']")
        time.sleep(1)
        send_button.click()
        print("menssagem enviada")
        self.driver.quit()

    def SendLoopMessage(self, message, count):
        for i in range(count):
            input_chat = self.driver.find_element_by_class_name('_3uMse')
            print(f"[{i}] writing")
            time.sleep(0.5)
            input_chat.send_keys(message + Keys.RETURN)
            time.sleep(0.5)
            send_button = self.driver.find_element_by_xpath(
                "//span[@data-icon='send']")
            time.sleep(0.5)
            send_button.click()
            time.sleep(0.3)

            print("[] sending message")
        print("[] end of messages")
        self.driver.quit()
