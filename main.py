import asyncio


from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message
from modules import get_response
from config import TOKEN



bot = Bot(token = TOKEN)
dp = Dispatcher()
router = Router()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi')

@router.message(Command('ai'))
async def channel_handler(message: types.Message, command: CommandObject):

    answer = command.args
    response = await get_response(answer)
    await message.reply(response)

@router.message(Command("Credits"))
async def channel_handler(message: types.Message):
    if message.user.ID == TG_ID:
        responce = await get_credits()
        await message.reply(responce)



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
    



