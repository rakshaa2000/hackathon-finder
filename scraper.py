import requests
from bs4 import BeautifulSoup
from datetime import date
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = discord.Client()

URL = 'https://mlh.io/seasons/2022/events'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
new_results = soup.find_all('div',class_='container feature')
results = new_results[1].find_all('div',class_='row')
events = results[0].find_all('div', class_='event')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content=='!hf-mlh':
        for i in events:
            # list_events.append((name,dates_full)) 
            name = (i.find('h3',class_='event-name').text)
            dates_full = i.find('p',class_="event-date").text   
            link = i.find('a', class_="event-link")['href']
            msg = name + ": " + dates_full+ ", "+link
            await message.channel.send(msg)

client.run(TOKEN)