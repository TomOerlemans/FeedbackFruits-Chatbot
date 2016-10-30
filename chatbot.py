from itertools import chain
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer


chatBot = ChatBot(
    "FeedBackFruits",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="chatterbot.data.cities.db",
    read_only=True
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        bot_input = chatBot.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
