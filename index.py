
from os import listdir, getenv
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands, tasks

load_dotenv()

description = "A bot!"

intents = Intents.default()
intents.members = True

# make prefix configurable
bot = commands.Bot(command_prefix='-', description=description, intents=intents)

# load extensions
for file in listdir("./cogs"): # lists all the cog files
    if file.endswith('.py'): # ensure file ends with '.py'
        name = file[:-3] # get rid of .py
        bot.load_extension(f"cogs.{name}")

@bot.event
async def on_command_error(ctx, error): # get rid of CommandNotFound
    if isinstance(error, commands.CommandNotFound):
        return

bot.run(getenv('BOT_TOKEN'))