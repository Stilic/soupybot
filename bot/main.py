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
    
  with socketserver.TCPServer(("", 8000), handler) as httpd:
    httpd.serve_forever()

servesx = Thread(None, serverStart, None, ())
servesx.start()

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")

@client.event
async def on_ready() :
  await client.change_presence(status = discord.Status.idle, activity = discord.Game("For help: type .help"))
  print("INFO: Bot is online\nINFO: For quit, press Ctrl+C")

@client.command()
async def ping(ctx):
  """I am fast or no?"""
  await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

@client.command(name="whoami")
async def whoami(ctx):
  """Shows what guy have send this command"""
  await ctx.send(f"You are {ctx.message.author.name}")

@client.command()
async def clear(ctx, amount):
  """Clear a number of messages you specify (by default 3) or alls if you specify this"""
  if amount == "all":
    await ctx.channel.purge()
  else:
    try:
      await ctx.channel.purge(limit=amount)
    except ValueError:
      await ctx.send("Sorry but that's don't work! Please retry!")

@client.command()
async def randomimg(ctx):
  """Sends a random image (they uses https://picsum.photos for this)"""
  await ctx.send("https://picsum.photos/300/300")

try:
  client.run(token)
except KeyboardInterrupt:
  print("INFO: We quit now!")

finally:
  os._quit(1)