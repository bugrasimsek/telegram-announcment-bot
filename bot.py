from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import commands
import scraper

# port changed to 8443
PORT = int(os.environ.get("PORT", 8443))

# to go public, change chat_id = chat_id


def sendDuyuruList(botObj):
    duyuruList = scraper.scrape()

    if len(duyuruList) == 0:
        return

    else:
        for duyuru in duyuruList:
            botObj.send_message(chat_id=myuser_id, text=duyuru)


def main():
    # token creditensials are in heroku config vars
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", commands.start))
    dp.add_handler(CommandHandler("help", commands.help))
    dp.add_handler(CommandHandler("check", commands.check))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, commands.echo))

    # log all errors
    dp.add_error_handler(commands.error)

    """
    What this is doing is that it changes the polling method to webhook, 
    listening in to 0.0.0.0 with the port you specified above with the PORT variable.
    """
    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=token,
        webhook_url="https://young-mesa-06808.herokuapp.com/" + token,
    )

    sendDuyuruList(updater.dispatcher.bot)
    # updater.dispatcher.bot.send_message(chat_id=myuser_id, text=scraper.scrape())

    #   updater.dispatcher.bot.send_message(
    #     chat_id=myuser_id, text=scraper.scrape()[0].encode("utf-8")
    # )

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == "__main__":
    main()
