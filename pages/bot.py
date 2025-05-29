import os

# Первое сообщение в консоль для диагностики
print("BOT: запускаюсь…")

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

# Читаем токен из переменной окружения
API_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not API_TOKEN:
    print("ERROR: Переменная TELEGRAM_TOKEN не установлена")
    exit(1)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(Command("start"))
async def send_guide(message: Message):
    await message.answer(
        "Привет! 🌿\n"
        "Добро пожаловать в Mir Station.\n"
        "Вот ваш гайд «Нетревожное цветоводство»:"
    )
    # Отправляем PDF (убедитесь, что файл лежит по этому пути)
    with open("pages/netrevozhnoe_cvetovodstvo_guide.pdf", "rb") as f:
        await message.answer_document(f)

# Второе сообщение в консоль перед запуском polling
if __name__ == "__main__":
    print("BOT: polling запущен")
    dp.run_polling(bot)
