from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

trainingData= [
    'Hi'
  , 'Chal be laude'
  , 'I need your assistance regarding my order'
  , 'nae milega'
  , 'I have a complaint.'
  , 'gand marao.'
  , 'How long it will take to receive an order ?'
  , 'kabhi nae aaega.'
  , 'Okay Thanks'
  , 'ha nikal bsdk ke'
  ]


class chatbot():
  def __init__(self):
    bot = ChatBot( 'BCE Bot', logic_adapters= ['chatterbot.logic.BestMatch', 'chatterbot.logic.TimeLogicAdapter'])
    trainer = ListTrainer(bot)
    trainer.train(trainingData)

  def talk(message):
    bot.get_response(message)
