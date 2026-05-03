import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

# ===== НАЛАШТУВАННЯ =====
TOKEN = "8647684989:AAE_qHOd6TspYufN6H7UqDkiKt6HJVZkgac"

SET_RANGE = 1

# ===== МОВИ =====
LANGUAGES = {
    "uk": {
        "choose_lang": "Оберіть мову:",
        "lang_set": "Мову змінено на українську",
        "random": "Випадкове число",
        "choose": "Я обираю",
        "enter_range": "Введи діапазон (наприклад: 1 100)",
        "error": "Невірний формат. Напиши: 1 100",
    },
    "en": {
        "choose_lang": "Choose language:",
        "lang_set": "Language set to English",
        "random": "Random number",
        "choose": "I choose",
        "enter_range": "Enter range (example: 1 100)",
        "error": "Wrong format. Write: 1 100",
    }
}

# ===== ДОПОМОЖНІ =====
def get_lang(context):
    return context.user_data.get("lang", "uk")

# ===== /start =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Використовуй /random_number або /choose")

# ===== /random_number =====
async def random_number(update: Update, context: ContextTypes.DEFAULT_TYPE):
    number = random.randint(1, 100)
    lang = get_lang(context)
    await update.message.reply_text(f"{LANGUAGES[lang]['random']}: {number}")

# ===== /set_number =====
async def set_number_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context)
    await update.message.reply_text(LANGUAGES[lang]["enter_range"])
    return SET_RANGE

async def set_number_receive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context)

    try:
        a, b = map(int, update.message.text.split())
        number = random.randint(a, b)
        await update.message.reply_text(f"{LANGUAGES[lang]['random']}: {number}")
    except:
        await update.message.reply_text(LANGUAGES[lang]["error"])
        return SET_RANGE

    return ConversationHandler.END

# ===== /choose =====
async def choose_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = get_lang(context)

    text = update.message.text.replace("/choose", "").strip()

    if not text:
        await update.message.reply_text("Напиши варіанти через кому:\n/choose чай, кава, вода")
        return

    options = [x.strip() for x in text.split(",")]
    choice = random.choice(options)

    await update.message.reply_text(f"{LANGUAGES[lang]['choose']}: {choice}")

# ===== /lang =====
async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Українська", callback_data="lang_uk"),
            InlineKeyboardButton("English", callback_data="lang_en"),
        ]
    ]

    await update.message.reply_text(
        "Оберіть мову:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def language_button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    lang = query.data.split("_")[1]
    context.user_data["lang"] = lang

    await query.edit_message_text(LANGUAGES[lang]["lang_set"])

# ===== /cancel =====
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Скасовано")
    return ConversationHandler.END

# ===== MAIN =====
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # Діалог
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("set_number", set_number_start)],
        states={
            SET_RANGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, set_number_receive)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )

    # Команди
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("random_number", random_number))
    app.add_handler(CommandHandler("choose", choose_command))
    app.add_handler(CommandHandler("lang", set_language))

    # Callback
    app.add_handler(CallbackQueryHandler(language_button))

    # Діалог
    app.add_handler(conv_handler)

    print("Бот запущений...")
    app.run_polling()

if __name__ == "__main__":
    main()