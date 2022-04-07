import discord
import os
import keep_alive
from discord.ext import commands

bot = commands.Bot(command_prefix='msg!') 
bot.load_extension('dispander')

@bot.event
async def on_ready():
    print('Bot is ready.')

keep_alive.keep_alive()
bot.run('OTYxMDkxNTExNzA4MTg0NjA3.Ykz8OA.ovVdc7CJCf-tjyn3f2xjHfK7o_Q') 
