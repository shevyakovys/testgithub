from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import urllib.parse

TOKEN = '7509768457:AAEiX8-bnMkr70Cs_VlyB7hAY0tGYrHbJaM'
CHANNEL_ID = '-1002250619753'
WEB_APP_URL = 'https://api.ucalc.pro/api/432078'  # Замените на HTTPS URL вашего веб-приложения

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    user_data = {
        "id": user.id,
        "username": user.username or "",
        "first_name": user.first_name or "",
        "last_name": user.last_name or ""
    }

    # Формируем URL с параметрами
    url_with_params = f"{WEB_APP_URL}?id={user_data['id']}&username={user_data['username']}&first_name={user_data['first_name']}&last_name={user_data['last_name']}"

    chat_member = await context.bot.get_chat_member(CHANNEL_ID, user.id)

    if chat_member.status in ['member', 'administrator', 'creator']:
        keyboard = [
            [InlineKeyboardButton("Регистрация на мероприятие", web_app={"url": url_with_params})]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            'Отлично! Вы подписаны на канал и готовы принять участие в конкурсе!',
            reply_markup=reply_markup
        )
    else:
        keyboard = [
            [InlineKeyboardButton("Подписаться", url='https://t.me/ci_jobs')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(
            'Для участия в конкурсе еобходимо подписаться на канал ИТ Центр-инвест',
            reply_markup=reply_markup
        )

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
