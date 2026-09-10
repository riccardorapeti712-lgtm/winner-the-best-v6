import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

SCHEDINA_TEXT = "WINNER THE BEST V12 LIVE\nBOMBA: Juve-Inter GOL @2.70\nReal-Barca OVER 2.5 @1.85\nTRILLO ATTIVATO MIO! BOT 100% ONLINE!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("WINNER ONLINE MIO! /schedina /trillo")

async def trillo_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("TRILLO ATTIVATO MIO!")

async def schedina_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SCHEDINA_TEXT)

def run_web():
    web = Flask(__name__)
    @web.route('/')
    def home():
        return "WINNER ONLINE"
    web.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))

Thread(target=run_web, daemon=True).start()

print("=== AVVIO BOT NEL MAIN THREAD - FIX set_wakeup_fd ===")
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("trillo", trillo_cmd))
app.add_handler(CommandHandler("schedina", schedina_cmd))
app.run_polling(drop_pending_updates=True)
