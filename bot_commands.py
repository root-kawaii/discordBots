# bot.py
from email import message
from http import client
import os
import random
from random import seed
from random import randint
import discord
from discord.ext import commands,tasks
import os
from dotenv import load_dotenv
import youtube_dl

import discord
from discord.ext import commands
from dotenv import load_dotenv

#from bot_one import YTDLSource


intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!',intents=intents)

def setup(bot: commands.Bot):
    bot.add_cog(Commands(bot))

class Commands(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @bot.command(name='yo',help='Say Hi!')
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

    @bot.command(name='join', help='Tells the bot to join the voice channel')
    async def join(self,ctx):
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
            return
        else:
            channel = ctx.message.author.voice.channel
        await channel.connect()

    @bot.command(name='leave', help='To make the bot leave the voice channel')
    async def leave(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("The bot is not connected to a voice channel.")

    @bot.command(name='plays', help='To play song')
    async def play(self,ctx,url):
        try :
            server = ctx.message.guild
            voice_channel = server.voice_client

            async with ctx.typing():
                filename = await YTDLSource.from_url(url, loop=bot.loop)
                voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
            await ctx.send('**Now playing:** {}'.format(filename))
        except:
            await ctx.send("The bot is not connected to a voice channel.")

    @bot.command(name='pause', help='This command pauses the song')
    async def pause(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("The bot is not playing anything at the moment.")
    
    @bot.command(name='resume', help='Resumes the song')
    async def resume(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("The bot was not playing anything before this. Use play_song command")

    @bot.command(name='stop', help='Stops the song')
    async def stop(self,ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("The bot is not playing anything at the moment.")

