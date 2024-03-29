import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "42:TOKEN"


bot = Bot(TOKEN, parse_mode="HTML")
dispatcher = Dispatcher(bot)


@dispatcher.message_handler(commands=["start"])
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>")


@dispatcher.message_handler()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward received message back to the sender

    By default, message handler will handle all message types (like text, photo, sticker and etc.)
    """
    try:
        # Send copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dispatcher, skip_updates=True)
