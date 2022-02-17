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


bot = commands.Bot(command_prefix='!')
log = []

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))

class Events(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user.name} has connected to Discord!')
        #await ctx.send('{client.user.name} has connected to Discord!')


    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.errors.CheckFailure):
            await ctx.send('You do not have the correct role for this command.')
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if "#play" in message.content:
            file = open('songsLog.txt', 'a')
            file.write("\n" + message.content + "\n")
            file.close()
            if(message.author.bot):
                return
            else:
                await message.channel.send('recorded...')
            

            