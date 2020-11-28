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

client.load_extension('cogs.General')

try:
  client.run(token)
except KeyboardInterrupt:
  print("INFO: We quit now!")