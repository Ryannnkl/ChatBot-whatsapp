from bot import Chatbot


def initial(bot):

    name = input("Digite o nome do usuario para procurar\n:")
    bot.searchContact(name)

    message = input("Digite a menssagem para ser exibida\n:")

    metod = int(
        input(
            "Digite uma opção:\nMenssagem simples [1]\nmultiplos envios [2]\n: "
        ))

    if metod == 1:
        bot.SendSimpleMessage(message)
    if metod == 2:
        count = int(input("digite a quantidade de vezes"))
        bot.SendLoopMessage(message, count)
    else:
        print("Opção invalida")


print("[] initialized bot")

bot = Chatbot()
bot.openBrowser()

while True:
    initial(bot)
    if (input("Continuar? S/N: ").upper() == "S"):
        continue
    else:
        bot.driver.quit()
        break

print("[] finalized bot")