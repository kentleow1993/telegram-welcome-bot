import os
import asyncio

# Fix Python 3.14 event loop issue (safe)
try:
    asyncio.get_event_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())


from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)


TOKEN = os.getenv("BOT_TOKEN")


# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🌐 Open Website",
                url="https://www.4win.vip/myr/home"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)


    message = """
🎉 Welcome!

Thank you for joining our Telegram bot.

Click the button below to visit our website.
"""


    # Send banner image
    try:
        with open("banner.jpg", "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                caption=message,
                reply_markup=reply_markup
            )

    except FileNotFoundError:

        await update.message.reply_text(
            message,
            reply_markup=reply_markup
        )



# Error handler
async def error_handler(update, context):
    print("Error:", context.error)



def main():

    if not TOKEN:
        print("ERROR: BOT_TOKEN missing")
        return


    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )


    app.add_handler(
        CommandHandler("start", start)
    )


    app.add_error_handler(error_handler)


    print("Bot started...")


    app.run_polling()



if __name__ == "__main__":
    main()
