import discord
from discord import app_commands
from discord.ext import commands 
import datetime as dt
import requests
import json
import sys
import time
from time import sleep


with open('token.txt', 'r') as token_file:
    token = token_file.readline()
    

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!' , intents=intents) 
@bot.event
async def on_ready():
    print("Bot is up and ready :) ")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands(s)")
    except Exception as e:
        print(e)
        
@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello {interaction.user.mention}! my name is Oreo.....Nice to meet you.....:)))" )
    
@bot.tree.command(name="say")
@app_commands.describe(things_to_say = "Ask me what should I say")
async def say(interaction: discord.Interaction, things_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said: '{things_to_say}'")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1117138124133367872)
    await channel.send(f"Welcome {member.mention}!")
    
    
@bot.tree.command(name="weather")
@app_commands.describe(current_city = "Which city's weather would you like to know ? ")
async def weather(interaction: discord.Interaction, current_city: str):
    CITY = current_city
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    API_KEY = 'd6f53fb159ce46b3378efa390cf0b7fb'

    def kelvin_to_celcius_fahrenheit(kelvin):
        celcius = kelvin - 273.15
        fahrenheit = celcius * (9/5) + 32
        return celcius, fahrenheit

    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    temp_kelvin = response['main']['temp']
    temp_celcius, temp_fahrenheit = kelvin_to_celcius_fahrenheit(temp_kelvin)

    feels_like_kelvin = response['main']['feels_like']
    feels_like_celcius, feels_like_fahrenheit = kelvin_to_celcius_fahrenheit(feels_like_kelvin) 

    wind_speed = response['wind']['speed']
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise']+ response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset']+ response['timezone'])


    await interaction.response.send_message(f'''Temprature in {current_city}: {temp_celcius:.2f} C or {temp_fahrenheit: } F
                                          Feels like : {feels_like_celcius: .2f} or {feels_like_fahrenheit: .2f} F
                                          Humidity in {current_city}: {humidity}% 
                                          Wind Speed in {current_city}: {wind_speed}m/s
                                          General Weather in {current_city}: {description}
                                          Sun Rises in {current_city}: {sunrise_time} local time 
                                          Sun Sets in {current_city}: {sunset_time} local time ''')

bot.run(token)








