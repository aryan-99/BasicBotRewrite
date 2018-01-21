#These are the modules imported for the script. DO NOT remove any of these, as the script won't run without them.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

#This line defines the client variable which will be used a lot in coding commands. Enter your bot's description and prefix within the quotes.
client = Bot(description = "BasicBot for rewrite created by Hades#6871", command_prefix = "Enter a prefix")

@client.event
async def on_ready():
    #This function sets the Playing status for your bot
    await client.change_presence(game = discord.Game(name = "Enter the playing status for your bot"))
    #The following lines print some information about your bot to the console
    print("~" * 40)
    print("Logged in as: {}".format(client.user.name))
    print("Bot's ClientID: {}\n".format(client.user.id))
    print("Connected to {} guilds".format(len(client.guilds)))
    print("Connected to {} users\n".format(sum(1 for user in client.get_all_members())))
    print("Running discord.py version {}".format(discord.__version__))
    print("Running Python version {}\n".format(platform.python_version()))
    print("Invite the bot with administrator permissions using https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8".format(client.user.id))
    print("-"  * 40)
    
@client.command()
async def ping(ctx):
    await ctx.send(":ping_pong: **Pong!**\nDon't forget to modify the BasicBot code!")

#Every bot has a unique token - insert your bot's token within the quotation marks
client.run("Insert your token here")
