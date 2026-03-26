from discord.ext import commands


@commands.command()
async def sync(ctx):
    await commands.tree.sync()