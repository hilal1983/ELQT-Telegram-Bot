import os
import telebot
from flask import Flask, request

# توكن البوت
TOKEN = "7595521583:AAGDXG8me8qCaNLp9AR5AaM2X0kiFY_ByYg"
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "🤖 ELQT Telegram Bot is Running!"

@app.route('/setwebhook', methods=['GET'])
def set_webhook():
    bot.remove_webhook()
    # تحديد الرابط العام مباشرةً
    repl_slug = os.environ.get('REPL_SLUG', 'elqt-telegram-bot-banyahilal')
    repl_owner = os.environ.get('REPL_OWNER', 'banyahilal')
    webhook_url = f"https://{repl_slug}.{repl_owner}.repl.co/{TOKEN}"
    bot.set_webhook(url=webhook_url)
    print(f"Webhook set to: {webhook_url}")  # يظهر الرابط في الـ Console
    return f"Webhook set to {webhook_url}", 200

@app.route('/' + TOKEN, methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 مرحباً بك في ELQT Bot!\nاكتب /help لمعرفة الأوامر المتاحة.")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "🧾 الأوامر المتاحة:\n/start - بدء الاستخدام\n/help - عرض المساعدة")

if __name__ == "__main__":
    print("🚀 ELQT Bot is starting...")
    print("🔗 افتح الرابط التالي لتفعيل Webhook بعد التشغيل:")
    print("https://elqt-telegram-bot-banyahilal.banyahilal.repl.co/setwebhook")
    app.run(host="0.0.0.0", port=8080)
