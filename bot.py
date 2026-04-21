import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes
import os

TOKEN = os.environ.get("TOKEN")

logging.basicConfig(level=logging.INFO)

async def handle_join_request(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.chat_join_request.from_user
    chat_id = update.chat_join_request.chat.id
    user_id = user.id

    await context.bot.send_message(
        chat_id=user_id,
        text=(
            f"Ciao {user.first_name}, benvenuto in BetCracker! 🎉\n\n"
            "Qui sotto trovi il link d'accesso al canale:\n"
            "👉 https://t.me/+ekYImrq1wUhlNmRk\n\n"
            "Puoi scrivere direttamente a @Varagasy per informazioni sul software!\n\n"
            "Benvenuto, preparati a cambiare per sempre il tuo modo di scommettere! 🚀"
        )
    )

    await context.bot.approve_chat_join_request(
        chat_id=chat_id,
        user_id=user_id
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(handle_join_request))

print("🤖 Bot avviato!")
app.run_polling()