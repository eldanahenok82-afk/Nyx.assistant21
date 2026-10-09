import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

# Your official bot token
BOT_TOKEN = "8790815756:AAFP_X7IbEs2XcMr9tJF3WFe80pJ3AbC-ik"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="📋 My Daily Focus", callback_data="todo")],
        [InlineKeyboardButton(text="💡 Quick Ideas", callback_data="ideas")]
    ])
    await message.answer(
        f"👋 Hello boss! <b>NexaNyx Assistant</b> is wired to GitHub and online.",
        reply_markup=keyboard,
        parse_mode="HTML"
    )

@dp.message(Command("todo"))
async def cmd_todo(message: Message):
    await message.answer(
        "📋 <b>NexaNyx Personal Task List:</b>\n\n"
        "1. Optimize Whop digital product store templates\n"
        "2. Review student hub prompt library\n"
        "3. Push updates to GitHub repository",
        parse_mode="HTML"
    )

async def main():
    print("🚀 Starting GitHub-backed NexaNyx bot...")
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped.")
