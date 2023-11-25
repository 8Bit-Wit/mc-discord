import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

prefix = '%'

bot = commands.Bot(
    intents=discord.Intents.all(), command_prefix=prefix)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    #await message.channel.send(message.content.split(prefix))
    if message.content.split(prefix)[0] == '':
        #                                               ------- test
        if message.content.split(prefix)[1] == 'test':
            await message.channel.send("Testing...")

        #                                               ------- list
        if message.content.split(prefix)[1] == 'list':
            #rcon connect to server
            #grab current list of players
            #format data

            await message.channel.send("List Current Online Players")

        #                                               ------- whitelist
        if message.content.split(prefix)[1] == 'whitelist':
            #rcon connect
            #server command "whitelist add {player}"

            await message.channel.send("Whitelist Player")

        #                                               ------- msg
        if message.content.split(prefix)[1] == 'msg':
            #rcon connect
            #server command "msg {player}"

            await message.channel.send("Msg Player")


    


bot.run(TOKEN)