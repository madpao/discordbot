import discord
import os
import keep_alive
from discord.ext import commands

from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def main():
    return 'Bot is aLive!'
def run():
    app.run(host="0.0.0.0", port=8080)
def keep_alive():
    server = Thread(target=run)
    server.start()

bot = commands.Bot(command_prefix='msg!') 
bot.load_extension('dispander')

@bot.event
async def on_ready():
    print('Bot is ready.')

keep_alive.keep_alive()
bot.run('OTYxMDkxNTExNzA4MTg0NjA3.Ykz8OA.ovVdc7CJCf-tjyn3f2xjHfK7o_Q') 
