import discord
import urllib.request
import json
import re

token = ""
client = discord.Client()
@client.event
async def on_ready():
    print('Start-> {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/neko'):
        await message.channel.send('nyaaaaa')

    if message.content.startswith('/inu'):
        await message.channel.send('wanwan')


# wather
citycode = '016010'
resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
resp = json.loads(resp.decode('utf-8'))


client.run(token)