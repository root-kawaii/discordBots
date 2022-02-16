# bot.py
from email import message
from http import client
import os
import random
from random import seed
from random import randint

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
bot.load_extension("bot_events")
bot.load_extension("bot_commands")


#client.run(TOKEN)
bot.run(TOKEN)


