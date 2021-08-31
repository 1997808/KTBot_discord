import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

# client = discord.Client()
bot_prefix = '-'
bot = commands.Bot(command_prefix = bot_prefix)

load_dotenv()
TOKEN = os.getenv('TOKEN')

@bot.event
async def on_ready():
  # channel = bot.get_channel(882179907608776704)
  # await channel.send("Just connected!?!")
  print("Bot connected to the server!")

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return

  if message.content.startswith('hello'):
    await message.channel.send("Hello")
    return

  if bot.user in message.mentions:
    await message.channel.send(f'My prefix is {bot_prefix}')
    return

  await bot.process_commands(message)
  
@bot.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send(f'Welcom to server {member}!')

@bot.command(name='ping')
async def ping(ctx):
  await ctx.send(f'Ping! {bot.latency * 1000} ms')

bot.run(TOKEN)