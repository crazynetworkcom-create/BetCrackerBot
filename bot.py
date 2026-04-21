import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

logging.basicConfig(level=logging.INFO)

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = update.chat_join_request.chat.id
    user_id = user.id

    # Crea il pulsante
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("👉 Entra nel canale", url="https://t.me/+ekYImrq1wUhlNmRk")],
        [InlineKeyboardButton("Prendi il software in offerta 🔥", url="https://t.me/Varagasy?text=Ciao%2C%20vorrei%20informazioni%20per%20prendere%20il%20software%20in%20offerta!")]
    ])

    await context.bot.send_message(
        chat_id=user_id,
        text=(
            f"Ciao {user.first_name}, benvenuto in BetCracker! 🎉\n\n"
            "Puoi scrivere direttamente a @Varagasy per informazioni sul software, che è in offerta ancora per poco!\n\n"
            "Benvenuto, preparati a cambiare per sempre il tuo modo di scommettere! 🚀"
        ),
        reply_markup=keyboard
    )

    await context.bot.approve_chat_join_request(
        chat_id=chat_id,
        user_id=user_id
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join_request))

print("🤖 Bot avviato!")
app.run_polling()
