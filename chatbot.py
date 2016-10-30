from chatterbot import ChatBot

chatBot = ChatBot(
    "FeedBackFruits",
    storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    input_adapter="chatterbot.adapters.input.TerminalAdapter",
    output_adapter="chatterbot.adapters.output.TerminalAdapter",
    database="cities.db",
    logic_adapters=[
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    read_only=True
)

print("Type something to begin...")

# The following loop will execute each time the user enters input
while True:
    try:
        bot_input = chatBot.get_response(None)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
