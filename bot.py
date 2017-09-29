import discord
import asyncio
from discord.ext import commands

description = # Enter a description here in a string

bot = commands.Bot(description=description, command_prefix='>') #Bot's name is "bot", change the name if you want :D

@bot.event
async def on_ready():
      print('Logged in')
      print('Name : {}'.format(bot.user.name)) # this is stats (not live) when you start the bot
      print('ID : {}'.format(bot.user.id))
      print(discord.__version__)
      await bot.change_presence(game=discord.Game(name='')) #name = 'Whatever game you want the bot to display as playing'

@bot.command(pass_context = True)
async def Stats(ctx):
  await bot.say(f"Online, {ctx.message.author.mention}!") #USE PYTHON 3.6.1+

  


