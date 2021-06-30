import constants as keys
from telegram.ext import *
import responses as r
from telegram.ext import Filters
#Filters.text

print("Bot started.....")


def start_command(update, context: CallbackContext):
    update.message.reply_text("""
               Welcome to The library bot, 
        Enter your Branch(Eg:if in First year , enter lib_FE)
        Type help for help regarding this bot
                """)


def help_command(update, context):
    update.message.reply_text("""Type the following words to do the following:
                  lib_start- starts the bot
                  lib_about- tells you about the bot
                  lib_support- Contact detail to give feedback
                  lib_add- Add librarybot to your group 
                  lib_exit- Exit librarybot 
                       """)


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Updates {update} caused error {context.error}")


#def greet_user(`update: Update, context: CallbackContext`):
#update.message.reply_text('hello')

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help",help_command))
    all = Filters.all

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()
