#These are the modules imported for the script. DO NOT remove any of these, as the script won't run without them.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import platform

#different variables
token = "INSERT TOKEN HERE"
prefix = "PREFIX"

#This line defines the client variable which will be used a lot in coding commands. Enter your bot's description and prefix within the quotes.
client = Bot(description="BasicBot for rewrite created by Hades#6871", command_prefix=prefix, case_insensitive=True)

@client.event
async def on_ready():
    #This function sets the Playing status for your bot
    await client.change_presence(activity = discord.Game("<playing status here>"))
    #The following lines print some information about your bot to the console
    print("=" * 40 + "\n")
    print("Logged in as: {}".format(client.user.name))
    print("Bot's clientID: {}\n".format(client.user.id))
    print("Connected to {} guilds".format(len(client.guilds)))
    print("Connected to {} users\n".format(sum(1 for user in client.get_all_members())))
    print("Running discord.py version {}".format(discord.__version__))
    print("Running Python version {}\n".format(platform.python_version()))
    print("Invite your bot: https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8\n".format(client.user.id))
    print("="  * 40)
    #makes the help command go to dms by default
    client.help_command=commands.DefaultHelpCommand(dm_help=True)

#Basic ping command - if you type ping with your prefix, it'll respond
@client.command()
async def ping(ctx):
    await ctx.send(":ping_pong: **Pong!**\nDon't forget to modify the BasicBot code!")

#Every bot has a unique token - insert your bot's token within the quotation marks
client.run(token, bot=True)
