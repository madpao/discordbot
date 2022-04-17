import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='msg!') 
bot.load_extension('dispander')

@bot.event
async def on_ready():
    print('Bot is ready.')

bot.run('TOKEN') 
#TOKENには自分のTOKENを入力
