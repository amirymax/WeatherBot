from aiogram import Dispatcher, Bot, types, executor
from Assistant import WeatherAssistant

bot = Bot(token="Напишите свой токен здесь")

dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    username=message.from_user.first_name
    await bot.send_message(message.chat.id,
                           f'_Салом_, *{username}*\n\nИн бот ба шумо обу ҳавои шаҳри мехостагиатонро нишон медиҳад.\n_Номи шаҳратонро нависед_',parse_mode='markdown')


obj = WeatherAssistant(' ')


@dp.message_handler()
async def weather(message):
    city_name = message.text
    obj.city = city_name

    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("Обу ҳаво барои имрӯз", callback_data='today')
    button2 = types.InlineKeyboardButton("Барои 5 рӯз", callback_data='days5')
    keyboard.add(button1, button2)

    await bot.send_message(message.chat.id, 'Варианти худро интихоб кунед:', reply_markup=keyboard)


@dp.callback_query_handler(lambda callback: callback.data == 'today')
async def today(callback: types.CallbackQuery):
    message = obj.today()
    await bot.send_message(callback.message.chat.id, message, parse_mode='markdown')


@dp.callback_query_handler(lambda callback: callback.data == 'days5')
async def days5(callback: types.CallbackQuery):
    message = obj.print_weather_5days()
    await bot.send_message(callback.message.chat.id, message, parse_mode='markdown')


executor.start_polling(dp, skip_updates=True)
