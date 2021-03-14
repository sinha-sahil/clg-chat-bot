from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatBot =
  ChatBot(
    'BCE Bot',
    logic_adapters=
      ['chatterbot.logic.BestMatch', 'chatterbot.logic.TimeLogicAdapter']
    )

trainer = ListTrainer(chatBot)

trainer.train([
  'Hi',
  'Chal be laude',
  'I need your assistance regarding my order',
  'nae milega',
  'I have a complaint.',
  'gand marao.',
  'How long it will take to receive an order ?',
  'kabhi nae aaega.',
  'Okay Thanks',
  'ha nikal bsdk ke'
])