
import threading
from flask import Flask
from telegram.ext import Updater, CommandHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "NomadSenseAI is running"

def start_tg():
    updater = Updater("PUT_YOUR_TOKEN_HERE", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", lambda update, context: update.message.reply_text("Hello from NomadSenseAI")))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    t = threading.Thread(target=start_tg)
    t.start()
    app.run(host="0.0.0.0", port=5000)
