import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv("BOT_TOKEN")

SCHEDINA = """🔵 WINNER THE BEST - PROVA TEST AUTOMATICA 🏆

💎 BOMBA DEL GIORNO:
⚽️ Juventus - Inter | GOL @2.70
⚽️ Real - Barca | OVER 2.5 @1.85

🔔 TRILLO ATTIVATO MIO!
✅ BOT 100% AUTOMATICO OK!
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔵 WINNER ONLINE MIO! Scrivi /schedina")

async def trillo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔔 TRILLO ATTIVATO MIO!")

async def schedina(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SCHEDINA)

def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trillo", trillo))
    app.add_handler(CommandHandler("schedina", schedina))
    app.run_polling()

Thread(target=run_bot, daemon=True).start()

web = Flask(__name__)
@web.route('/')
def home(): return "WINNER ONLINE"
web.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
