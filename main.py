from bot import Chatbot

print("[] initialized bot")

name = input("Digite o nome do usuario para procurar\n ")
message = input("Digite a menssagem para ser exibida\n ")

bot = Chatbot(name)

bot.SendMessage(message)

print("[] finalized bot")