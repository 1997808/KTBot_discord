import discord
import os
from dotenv import load_dotenv

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send("Hello")

@client.event
async def on_connect():
  print("Bot connected to the server!")

client.run(TOKEN)