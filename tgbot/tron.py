# /usr/bin/env python3.7

"""
The python-telegram-bot API is called telegram.ext. Here we define the
functions that will make the bot respond.
"""

from TextToOwO import owo
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    """
    Send a message when the /start command is issued.
    """
    update.message.reply_text("Hello! (Kitty.)")

def help(update, context):
    """
    Define the /help instructions.
    """
    update.message.reply_text("I'm afraid there is no help for you.")

def main():
    """
    This actually runs the bot given the functions above.
    First, start the updater with your bot's token.
    Second, create a dispatcher so that you can define handlers.
    Third, register the handlers from above.
    Finally, start the bot.
    """
    updater = Updater("bot_api_token", use_context=True)
    dispatch = updater.dispatcher

    # if you have new handlers, you can register them here
    dispatch.add_handler(CommandHandler("start", start))
    dispatch.add_handler(CommandHandler("help", help))

    # start the bot and let it run until terminated
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
