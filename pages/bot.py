import os
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHANNEL = "@MirStation"  # юзернейм вашего канала

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def on_start(message: types.Message):
    user = await bot.get_chat_member(CHANNEL, message.from_user.id)
    if user.status in ("creator", "administrator", "member"):
        # Если подписан
        await message.reply("Спасибо за подписку! Вот ваш гайд:")
        with open("pages/netrevozhnoe_cvetovodstvo_guide.pdf", "rb") as f:
            await bot.send_document(message.chat.id, f)
    else:
        # Если не подписан
        invite = await bot.export_chat_invite_link(CHANNEL)
        await message.reply(
            "Чтобы получить гайд, подпишитесь на наш канал:\n" + invite
        )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
