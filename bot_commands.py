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

def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))

class Commands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.command(name='yo')
    async def greet(self,ctx):
        await ctx.send('Hello Homie, What it do !!!')

    @bot.command(name='roll_dice', help='Simulates rolling dice.')
    async def roll(self,ctx, number_of_dice: int, number_of_sides: int):
        dice = [
            str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)
        ]
        await ctx.send(', '.join(dice))

    @bot.command(name='create_room', help='Create new room.')
    async def create_channel(self,ctx, channel_name):
        guild = ctx.guild
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if not existing_channel:
            print(f'Creating a new channel: {channel_name}')
            await guild.create_voice_channel(channel_name)

    @commands.command(name="ping",help='Retrieve webscoket ping')
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket latency."""
        await ctx.send(f"Pong! {round(self.bot.latency * 1000)}ms")
