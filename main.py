import os
import asyncio
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

SCHEDINA_TEXT = "WINNER THE BEST - PROVA TEST AUTOMATICA\nBOMBA DEL GIORNO:\nJuve - Inter | GOL @2.70\nReal - Barca | OVER 2.5 @1.85\nTRILLO ATTIVATO MIO!\nBOT 100% ONLINE!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("WINNER ONLINE MIO! /schedina = prova /trillo = trillo")

async def trillo_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("TRILLO ATTIVATO MIO!")

async def schedina_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(SCHEDINA_TEXT)

def run_bot():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("trillo", trillo_cmd))
    app.add_handler(CommandHandler("schedina", schedina_cmd))
    app.run_polling(drop_pending_updates=True)

Thread(target=run_bot, daemon=True).start()
web = Flask(__name__)
@web.route('/')
def home():
    return "WINNER ONLINE"
web.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
