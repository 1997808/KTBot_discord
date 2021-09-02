import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
import requests, json

# client = discord.Client()
bot_prefix = '-'
bot = commands.Bot(command_prefix = bot_prefix)

load_dotenv()
TOKEN = os.getenv('TOKEN')
WEATHER_KEY = os.getenv('WEATHER_KEY')
BASE_WEATHER_URL = os.getenv('BASE_WEATHER_URL')

# def discord_box(args) {
#   data = args
#   return f'```{data}```'
# }

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
  await ctx.send((f'```Ping! {bot.latency * 1000} ms```'))

@bot.command(name='weather')
async def weather(ctx, arg1):
  complete_url = BASE_WEATHER_URL + "appid=" + WEATHER_KEY + "&q=" + arg1
  response = requests.get(complete_url)
  x = response.json()

  if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_feel = y["feels_like"]
    current_humidity = y["humidity"]
    z = x["weather"]
    weather_description = z[0]["description"]
    await ctx.send(f'```Temperature {round(current_temperature / 10, 2)} \nHumidity {current_humidity} \nFeel like {round(current_feel / 10, 2)} \nWeather {weather_description}```')
  
  else:
    await ctx.send('```Server ded lmao```')
  
bot.run(TOKEN)