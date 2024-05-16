import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '7079213427:AAGzWaK3U-aI-RnDm5ePIf5j3unaecCJO0k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Start command handler
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    frontend_button = KeyboardButton('Frontend')
    backend_button = KeyboardButton('Backend')
    keyboard.add(frontend_button, backend_button)
    await message.answer("Assalomu alaykum siz S-Orca o'quv markazining darslar jadvaliga Hush kelibsiz!. O'qish yo'nalishingizni tanlang:", reply_markup=keyboard)

# Frontend button handler
@dp.message_handler(lambda message: message.text == 'Frontend')
async def frontend_handler(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(1, 6):
        button = KeyboardButton(str(i))
        keyboard.add(button)
    await message.answer("Guruhni tanlang:", reply_markup=keyboard)

# Room selection handler
@dp.message_handler(lambda message: message.text in ['1', '2', '3', '4', '5'])
async def room_selection_handler(message: types.Message):
    if message.text == '1':
        await message.answer("🧑🏻‍🏫  Dushanba 15:30-17:00")
        await message.answer("🧑🏻‍🏫  Chorshanba 15:30-17:00")
        await message.answer("🧑🏻‍🏫  Juma 15:30-17:00")
    elif message.text == '2':
        await message.answer("🧑🏻‍🏫  Dushanba 10:30-12:00")
        await message.answer("🧑🏻‍🏫  Chorshanba 10:30-12:00")
        await message.answer("🧑🏻‍🏫  Juma 10:30-12:00")
    elif message.text == '3':
        await message.answer("🧑🏻‍🏫  Dushanba 14:00-15:30")
        await message.answer("🧑🏻‍🏫  Chorshanba 14:00-15:30")
        await message.answer("🧑🏻‍🏫  Juma 14:00-15:30")
    elif message.text == '4':
        await message.answer("🧑🏻‍🏫  Dushanba 09:00-10:30")
        await message.answer("🧑🏻‍🏫  Chorshanba 09:00-10:30")
        await message.answer("🧑🏻‍🏫  Juma 09:00-10:30")
    elif message.text == '5':
        await message.answer("🧑🏻‍🏫  Seshanba 14:00-15:30")
        await message.answer("🧑🏻‍🏫  Payshanba 14:00-15:30")
        await message.answer("🧑🏻‍🏫  Shanba 14:00-15:30")

if __name__ == '__main__':
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dp.start_polling())