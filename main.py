from discord import channel
import discord
from discord.ext import commands
import time as t 

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='$',intents=intents)
