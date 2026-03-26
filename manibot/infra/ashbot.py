import discord
from discord.ext import commands

from manibot.action.mordheim import MordheimAction
from manibot.action.dice import DiceAction
from manibot.infra.config import TOKEN


class Ashbot:
    __slots__ = ('bot',)

    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        self.bot = commands.Bot(command_prefix="!", intents=intents)

    async def add_actions(self):
        await self.bot.add_cog(MordheimAction(bot=self.bot))
        await self.bot.add_cog(DiceAction(bot=self.bot))

    def run(self) -> None:
        self.bot.setup_hook = self.add_actions
        self.bot.run(TOKEN)