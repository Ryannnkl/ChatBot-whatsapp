from selenium import webdriver
import time


class Chatbot:
    def __init__(self, user):
        self.name = user
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def SendMessage(self, message):
        # <span dir="auto" title="Sininho" class="_3ko75 _5h6Y_ _3Whw5">
        # <div tabindex="-1" class="_3uMse">
        # <span data-testid="send" data-icon="send" class="">
        print("[] opening web site")
        self.driver.get("https://web.whatsapp.com")
        time.sleep(30)
        person = self.driver.find_element_by_xpath(
            f"//span[@title='{self.name}']")
        time.sleep(5)
        person.click()
        time.sleep(3)
        print("Usuario encontrado")
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
