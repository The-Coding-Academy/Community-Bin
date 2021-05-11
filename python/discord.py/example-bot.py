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
@commands.has_permissions(manage_messages=True)  # check for the correct perms
@commands.bot_has_permissions(manage_messages=True)
async def _purge(ctx, *, amount=1):  # set a default amount, which is 1
    """
    A command that clears messages
    """
    await ctx.channel.purge(limit=amount + 1)  # clear trigger msg too
    embed = discord.Embed(title="Done!",
                          description=f"Purged {amount} messages!")
    await ctx.send(embed=embed)


@commands.command(name="kick", aliases=['k'])
@commands.has_guild_permissions(kick_members=True)  # check for the correct perms
@commands.bot_has_guild_permissions(kick_members=True)
async def _kick(ctx, member:discord.Member=None,*, reason=None):
    """
    A command that kicks members
    """
    await member.send(f'You have been kicked from **{server.name}** for `{reason}`')
    await member.kick(reason=reason)  # This is the line that kicks the member
    embed = discord.Embed(
        title="Kicked Member", 
        description=f"{member.mention} has been kicked for `{reason}`")
    await ctx.send(embed=embed)


bot.add_command(_ping)
bot.add_command(_purge)
bot.add_command(_kick)


# you can uncomment the line below if you have the api-cog-example cog already
# bot.load_extension("api-cog-example")

if __name__ == "__main__":  # make sure the file isn't being imported
    bot.run("YOUR_TOKEN_HERE")  # put your own bot token in here
