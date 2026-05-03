import requests
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8790710163:AAEeY9MpGkRu1lzZbx6Tdm7zrIi1uLdd6nM"


app.add_handler(CommandHandler("quote", quote))
async def start(update, context):
    await update.message.reply_text("Привіт, я бот по серії книжок Коти-Вояки, у мене є декілька цікавих команд")
# 🚀 Запуск бота
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("quote", quote))

app.run_polling()
# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт, я бот по серії книжок Коти-Вояки, у мене є декілька цікавих команд")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
# Функція отримання мема з Reddit
def get_meme():
    url = "https://www.reddit.com/r/WarriorCatsMemes/new.json?limit=50"
    
    headers = {"User-Agent": "telegram-bot"}
    response = requests.get(url, headers=headers)
    data = response.json()

    posts = data["data"]["children"]
    
    images = []
    for post in posts:
        post_data = post["data"]
        if post_data["url"].endswith((".jpg", ".png", ".jpeg")):
            images.append(post_data["url"])

    if images:
        return random.choice(images)
    return None

# Команда
async def randommem(update: Update, context: ContextTypes.DEFAULT_TYPE):
    meme = get_meme()
    
    if meme:
        await update.message.reply_photo(photo=meme)
    else:
        await update.message.reply_text("Не знайшов мем 😿")

# Запуск
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("randommem", randommem))
    
    print("Бот працює 🚀")
    app.run_polling()

if __name__ == "__main__":

    async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):

# 😂 Список твоїх смішних цитат
        quotes = [
            "Не будь злюкою як Тигрозір, бо будеш в Темному Лісі гуляти.",
            "Ти можеш все - Сойкопер же зміг.",
            "Я не ледачий, я просто тренуюся бути старійшиною.",
            "Вогнезір: стає провідником. Я: не можу навіть прокинутись вчасно.",
            "Коли сказали 'ти обраний', але ти просто хотів поспати."
            "— Я піду на полювання — Ти ж щойно їв — Це було емоційне полювання"
            "Коли порушив Вояцький правильник, але зробив це красиво."
            "Коли старійшини знову розповідають одну й ту ж історію: Я це вже чув 9 життів тому"
            "Коти-Вояки навчили мене двом речам: 1) Довіряй інстинктам 2) Не довіряй нікому"
            "Коли пішов за травами і випадково став учнем медикота"
            "Я: хочу спокійного життя. Всесвіт Котів-Вояків: війна, зрада, пророцтва"
            "Справжня дружба — це коли ви разом порушуєте Вояцький правильник"
            "— Як ти думаєш, якщо я запихну свою лапу у цю пастку, я зможу не йти в патруль? —... — (замахується лапою в пастку) — ЛЕВОЛАПЕ НІ—"]

# 📩 Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Напиши /quote щоб отримати смішну цитату 😄")

# 📩 Команда /quote
async def quote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    random_quote = random.choice(quotes)
    await update.message.reply_text(random_quote)