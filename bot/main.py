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

inpts = ""

def inpt():
  global inpts
  try:
    while True:
      print("Commands")
      print('  [s]top')
      inpts = input("bot> ")

      if inpts == "s":
        print("INFO: The app is stopped now!")
        quit()
  except KeyboardInterrupt:
      print("INFO: The app is stopped now!")
      quit()

servesx = Thread(None, serverStart, None, ())
servesx.start()
inputx = Thread(None, inpt, None, ())

rebootBot = False

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

client.run(token)