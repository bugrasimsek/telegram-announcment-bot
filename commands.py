import logging
import telegram
import scraper

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

# event handler of /start
def start(update, context):
    update.message.reply_text("Bot Started!")


# event handler of /help
def help(update, context):
    update.message.reply_text("Cake is a lie! (No help feature for now)")


# echoes the message sent to the bot
def echo(update, context):
    update.message.reply_text(update.message.text)


def check(update, context):
    update.message.reply_text(scraper.scrape())


# Log Errors caused by Updates
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def callback_minute(context: telegram.ext.CallbackContext):
    context.bot.send_message(chat_id="", text="Two messages every hour")
