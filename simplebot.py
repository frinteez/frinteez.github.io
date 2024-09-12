import telebot
import requests
import os
import logging
from telebot import types

# Замените TOKEN на ваш реальный токен
TOKEN = os.getenv('TELEGRAM_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Путь к файлу логов
LOG_FILE = "messages_log.txt"

# Настройка логирования
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def log_message(message):
    """Функция для записи сообщения в лог файл."""
    username = message.from_user.username or "No username"
    user_id = message.from_user.id
    first_name = message.from_user.first_name or "No first name"
    last_name = message.from_user.last_name or "No last name"
    text = message.text

    log_entry = (f"User ID: {user_id}\n"
                 f"Username: {username}\n"
                 f"First Name: {first_name}\n"
                 f"Last Name: {last_name}\n"
                 f"Message: {text}\n"
                 f"{'-'*40}\n")

    try:
        logging.info(log_entry)
    except Exception as e:
        print(f"Error writing to log file: {e}")

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
    """Обработка команды /start для открытия мини-приложения."""
    markup = types.InlineKeyboardMarkup()
    mini_app_button = types.InlineKeyboardButton(text="Open Mini App", url="https://frinteez.github.io/")
    markup.add(mini_app_button)
    
    bot.send_message(message.chat.id, "Click the button below to open the mini app:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    """Обработка всех сообщений."""
    log_message(message)  # Запись сообщения в лог
    
    # Отправка случайного изображения котика или собачки
    if message.text.lower() == 'cat':
        send_cat_picture(message.chat.id)
    elif message.text.lower() == 'dog':
        send_dog_picture(message.chat.id)

def send_cat_picture(chat_id):
    """Отправка случайного изображения котика."""
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    if response.status_code == 200:
        cat_url = response.json()[0]['url']
        bot.send_photo(chat_id, cat_url)
    else:
        logging.error(f"Failed to get cat picture: {response.status_code}")

def send_dog_picture(chat_id):
    """Отправка случайного изображения собачки."""
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    if response.status_code == 200:
        dog_url = response.json()['message']
        bot.send_photo(chat_id, dog_url)
    else:
        logging.error(f"Failed to get dog picture: {response.status_code}")

# Запуск бота
bot.polling()
