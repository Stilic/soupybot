# basics modules
import os
from threading import Thread

# server modules
import http.server
import socketserver

# discord modules
import discord
from discord.ext import commands

def serverStart():
  handler = http.server.SimpleHTTPRequestHandler
  try:
    with socketserver.TCPServer(("", 8000), handler) as httpd:
      print("INFO: Server started")
      httpd.serve_forever()
  except OSError:
    print("ERROR: The default port is already taked!")
    quit()

servesx = Thread(None, serverStart, None, ())


client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("Listening to .help"))
    print("INFO: Bot is online")

@client.command()
async def ping(ctx) :
    await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx) :
    await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount=3) :
    await ctx.channel.purge(limit=amount)

try:
  client.run(token)
except KeyboardInterrupt:
  print("INFO: The app is stopped now!")
  quit()