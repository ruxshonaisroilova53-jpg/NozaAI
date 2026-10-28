import os
import telebot
import random

TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN sozlanmagan!")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(
        message,
        "Assalomu alaykum! 🌸\n"
        "Men Noza AI botman! 🤖\n"
        "Menga istalgan savolingizni yozing 😊\n\n"
        "/help — yordam\n"
        "/motiv — motivatsiya"
    )

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(
        message,
        "Mavjud buyruqlar:\n"
        "/start — botni boshlash\n"
        "/help — yordam\n"
        "/motiv — motivatsion gap\n\n"
        "Oddiy hisoblash uchun: 5 + 3"
    )

@bot.message_handler(commands=["motiv"])
def motiv(message):
    gaplar = [
        "O‘zingga ishon! Har bir qadam muhim. 🌷",
        "Bugungi mehnating — ertangi natijang. 💪",
        "Orzularing sari harakat qilishdan to‘xtama! ✨"
    ]
    bot.reply_to(message, random.choice(gaplar))

@bot.message_handler(func=lambda message: True)
def javob(message):
    matn = message.text.lower().strip()

    if matn == "salom":
        javob_matni = "Salom! 😊 Qalaysiz?"
    elif "isming" in matn:
        javob_matni = "Mening ismim Noza AI 🤖"
    elif matn in ["qalaysan", "qalaysiz"]:
        javob_matni = "Rahmat, yaxshiman! Siz-chi? 🌷"
    else:
        javob_matni = "Xabaringizni oldim 😊 /help buyrug‘ini sinab ko‘ring."

    bot.reply_to(message, javob_matni)

print("Noza AI ishga tushdi!")
bot.infinity_polling()
