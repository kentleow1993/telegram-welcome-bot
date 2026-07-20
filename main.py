import os
import asyncio
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)


TOKEN = os.getenv("BOT_TOKEN")

WEBSITE = "https://www.4win.vip/myr/home"


# ==========================
# Render Port Server
# ==========================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is running")


def run_web_server():

    port = int(os.environ.get("PORT", 10000))

    server = HTTPServer(
        ("0.0.0.0", port),
        HealthHandler
    )

    print("Web server running on port", port)

    server.serve_forever()



# ==========================
# Telegram Bot
# ==========================

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    text = """
🎉 Welcome to 4WIN Official Bot

🔥 Fast & Secure Online Platform

Click below to enter.
"""


    keyboard = [

        [
            InlineKeyboardButton(
                "🚀 ENTER NOW",
                url=WEBSITE
            )
        ]

    ]


    await update.message.reply_photo(
        photo=open("banner.jpg","rb"),
        caption=text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )




def main():

    # start Render web server
    threading.Thread(
        target=run_web_server,
        daemon=True
    ).start()


    app = (
        Application
        .builder()
        .token(TOKEN)
        .build()
    )


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    print("Bot started...")


    app.run_polling()



if __name__ == "__main__":
    main()
