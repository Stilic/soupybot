from discord.ext import commands as client

class TestCog:

    def __init__(self, bot):
        self.bot = bot

    @client.command()
    async def ping(ctx):
      """I am fast or no?"""
      await ctx.send(f"🏓 Pong with {str(round(client.latency, 2))}")

    @client.command(name="whoami")
    async def whoami(ctx):
      """Shows what guy have send this command"""
      await ctx.send(f"You are {ctx.message.author.name}")

    @client.command()
    async def clear(ctx, amount=3):
      """Clear a number of messages you specify (by default 3)"""
      await ctx.channel.purge(limit=amount)

def setup(bot):
    client.add_cog(TestCog(bot))