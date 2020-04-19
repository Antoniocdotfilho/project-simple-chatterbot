from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

nome = input('Qual é o seu nome?')

ChatBot = ChatBot('Paulo')
treino = (['oi','oi','como você está?', 'bem'])

ChatBot.train(treino)

while True:
    pergunta = input(nome,': ')
    print ('Paulo BOT: ',ChatBot.get_response(quest))
