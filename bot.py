import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

# Вставьте свой API ключ OpenWeatherMap
api_key = "12807ad835f0d5fdea74aa3c58721472"

# URL для запроса прогноза погоды
url = f"http://api.openweathermap.org/data/2.5/weather?q=Moscow&appid={api_key}&units=metric"

bot = telebot.TeleBot('6058734353:AAF5BCFaehT9h4GjIiMl9rxjIKKX-7FK5ok')

@bot.message_handler(commands=['start'])
def start(message):
    # Создание кнопки
    button = InlineKeyboardButton('Кликни по мне)', callback_data='button_pressed')
    # Создание клавиатуры с одной кнопкой
    keyboard = InlineKeyboardMarkup().add(button)
    # Отправка сообщения с клавиатурой
    bot.send_message(message.chat.id, 'Привет! Нажми на кнопку:', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'button_pressed':
        bot.answer_callback_query(call.id)
        bot.send_message(call.message.chat.id, ('Спасибо, мне понравилось!'))

@bot.message_handler(commands=["weather"])
def get_weather(message):
    response = requests.get(url)
    weather_data = response.json()
    
    # Получение данных о погоде
    description = weather_data["weather"][0]["description"]
    temp = weather_data["main"]["temp"]
    
    # Формирование сообщения о погоде
    weather_message = f"Сейчас {description} и температура составляет {temp}°C."
    print(weather_data)
    # Отправка сообщения о погоде пользователю
    bot.send_message(message.chat.id, weather_message)

# Запуск бота
bot.polling(none_stop=True)
