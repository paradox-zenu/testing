from aiogram import Bot, Dispatcher, types
import aiohttp
import os

API_TOKEN = '8047939325:AAFANFZJjF4ncrGvGsHB7kJyrkr38X7-8m8'
YOUTUBE_API_KEY = 'NxGBNexGenBots213770"'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['search'])
async def search_song(message: types.Message):
    query = message.get_args()
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q={query}&key={YOUTUBE_API_KEY}&maxResults=3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            data = await resp.json()
            results = []
            for item in data['items']:
                video_id = item['id']['videoId']
                title = item['snippet']['title']
                # Button to open WebApp with videoId
                results.append(types.InlineKeyboardButton(text=title, web_app=types.WebAppInfo(url=f"https://your-webapp-url.com/play/{video_id}")))
            keyboard = types.InlineKeyboardMarkup(row_width=1).add(*results)
            await message.reply("Select a song to play:", reply_markup=keyboard)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp)
