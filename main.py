from bot import Chatbot
from selenium.common.exceptions import TimeoutException


def initial(bot):

    again = True
    while again:
        try:
            name = input("Digite o nome do usuario para procurar\n:")
            bot.searchContact(name)
            again = False
        except TimeoutException:
            print("[404] usuario, não encontrado")
    again = True

    message = input("Digite a menssagem  :")

    while again:
        count = int(input("Digite a quantidade de menssagens: "))
        again = False
        if count <= 0:
            print("[400] Digite um numero maior que 0!")

    bot.SendMessage(message, count)


print("[] Bot iniciado")

bot = Chatbot()
bot.openBrowser()

while True:
    initial(bot)
    if (input("Continuar? S/N: ").upper() == "S"):
        continue
    else:
        bot.driver.quit()
        break

print("[] Bot finalizado")