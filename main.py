import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "立即開始",
                web_app=WebAppInfo(
                    url="https://www.4win.vip/myr/home"
                ),
            )
        ],
        [
            InlineKeyboardButton(
                "邀請好友",
                url="https://t.me/share/url?url=https://t.me/Kent4win_bot",
            ),
            InlineKeyboardButton(
                "官方客服",
                url="https://t.me/YOUR_SUPPORT",
            ),
        ],
        [
            InlineKeyboardButton(
                "官方頻道",
                url="https://t.me/YOUR_CHANNEL",
            ),
            InlineKeyboardButton(
                "官方大群",
                url="https://t.me/YOUR_GROUP",
            ),
        ],
    ]

    text = """
💎 GoFun 娛樂

💎 全球華人首選綜合娛樂平台
🎮 正版大廠遊戲，公平穩定運營

🟧【GoFun・核心優勢】

🔸 電子返水上限，天天回饋
🔸 官方頻道每日紅包不斷
🔸 真人、電子、體育、棋牌一站暢玩
🔸 資金儲備充足，100%穩定出款
"""

    with open("banner.jpg", "rb") as photo:
        await update.message.reply_photo(
            photo=photo,
            caption=text,
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot started...")

app.run_polling()
