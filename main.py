import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# Loggingni sozlash
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_USERNAME = os.environ.get("CHANNEL_USERNAME") # Masalan: @kanal_nomi yoki id

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! Men arxiv kanalingizdan hashtaglar orqali fayl qidirib beruvchi botman.\n\n"
        "Menga masalan #ish deb yozing, men o'sha hashtagli xabarlarni topib beraman."
    )

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text and text.startswith('#'):
        await update.message.reply_text(f"Qidirilmoqda: {text}\n(Kanalga ulash jarayoni yakunlanmoqda...)")
    else:
        await update.message.reply_text("Iltimos, qidirish uchun # bilan boshlanuvchi so'z yozing (masalan: #ish)")

def main():
    if not TOKEN:
        print("Xatolik: BOT_TOKEN topilmadi!")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), search_handler))

    print("Bot ishga tushdi...")
    app.run_polling()

if __name__ == '__main__':
    main()
