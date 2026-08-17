import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import BOT_TOKEN


logging.basicConfig(level=logging.INFO)

dp = Dispatcher()


def start_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(
        text="📱 Buy TG Accounts",
        callback_data="buy_accounts"
    )

    builder.button(
        text="💰 Deposit",
        callback_data="deposit"
    )

    builder.button(
        text="💳 Balance",
        callback_data="balance"
    )

    builder.button(
        text="📋 My Orders",
        callback_data="my_orders"
    )

    builder.button(
        text="💬 Support ↗",
        url="https://t.me/revulet"
    )

    builder.adjust(1, 2, 1, 1)

    return builder.as_markup()


@dp.message(CommandStart())
async def start_handler(message: Message):

    # Temporary balance.
    # Database/API connect hone ke baad yahan real balance aayega.
    balance = 21.00

    text = (
        "👋 <b>Welcome, Proxy's Manager !!!</b>\n\n"
        f"💳 <b>Balance:</b> ₹{balance:.2f}\n"
        "🏷️ <b>Bot Status:</b> ✅ Wholesale Enabled"
    )

    await message.answer(
        text,
        reply_markup=start_keyboard()
    )


async def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing in .env")

    bot = Bot(BOT_TOKEN)

    print("🤖 Proxy Manager started...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
