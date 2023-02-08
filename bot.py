
from khl import *

# init Bot
bot = Bot(token="token這裡")


@bot.on_message()
async def dc(msg:Message):
    print(msg.content)

@bot.on_startup
async def ready(bot:Bot):
    print("上線拉")

@bot.command(name='say',prefixes="!")
async def say(msg: Message,text):
    await msg.reply(text)

bot.run()
