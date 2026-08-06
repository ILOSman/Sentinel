import asyncio
import cv2
from aiogram import Bot, Dispatcher
from tok import tok # token file
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from datetime import datetime

TOKEN = tok
dp = Dispatcher()

# Handler for the /start command
@dp.message(CommandStart())
async def start_on_command(message: Message):
    cap = cv2.VideoCapture(0) # Open the default(0) webcam
    ret, frame = cap.read() # Capture one frame
    cap.release()
    
    if ret:
        cv2.imwrite("1.jpg", frame)
        photo = FSInputFile("./1.jpg")
        await message.answer_photo(photo, caption=datetime.now().strftime("%Y-%m-%d %I:%M:%S:%p"))
    else:
        await message.answer("Oh, a problem has occured.")

# Start the bot
async def main():
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)

# Entry
if __name__ == "__main__":
    asyncio.run(main())