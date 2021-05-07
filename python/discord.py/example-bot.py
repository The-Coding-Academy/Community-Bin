# This is an example of a very basic discord bot in python
import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=".", description="A basic discord bot")


@bot.event
async def on_ready():
    print("I'm online!")


@commands.command(name="ping")
async def _ping(ctx):
    latency = bot.latency * 1000  # convert to ms

    embed = discord.Embed(
        title="Pong!",  # make an embed to send
        description=f"My latency is {latency:.2f}ms",
        )

    await ctx.send(embed=embed)


@commands.command(name="purge", aliases=['clear'])
async def _purge(ctx, *, amount=1):  # set a default amount, which is 1
    """
    A command that clears messages
    """
    await ctx.channel.purge(limit=amount + 1).  # clear trigger msg too
    embed = discord.Embed(title="Done!",
                          description=f"Purged {amount} messages!")
    await ctx.send(embed=embed)


bot.add_command(_ping)
bot.add_command(_purge)


if __name__ == "__main__":  # make sure the file isn't being imported
    bot.run("YOUR_TOKEN_HERE")  # put your own bot token in here
