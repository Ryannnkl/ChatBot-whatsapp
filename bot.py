from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
print("teste")


class Chatbot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("lang=pt-br")
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

    def openBrowser(self):
        print("[] Abrindo navegador\n[] Acessando https://web.whatsapp.com")
        self.driver.get("https://web.whatsapp.com")
        self.driver.maximize_window()

    def searchContact(self, name):
        person = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, f"//span[@title='{name}']")))
        person.click()
        print("[] Usuario encontrado")

    def SendMessage(self, message, count):
        start_time = time.time()
        for i in range(count):
            input_chat = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_3uMse')))
            input_chat.click()
            print(f"[{i+1}] Escrevendo...")
            time.sleep(0.5)
            input_chat.send_keys(message + Keys.RETURN)
            time.sleep(0.8)
            print("[] Menssagem enviada")
        end_time = time.time()
        print("[] Fim das menssagens")
        print("Tempo total:", round(end_time - start_time, 2), " segundos")
