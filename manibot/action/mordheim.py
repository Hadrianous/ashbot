from discord.ext import commands
from discord.ext.commands import Bot, Cog


class MordheimAction(commands.Cog):

    def __init__(self, bot: Bot):
        self.bot = bot
        self.mutation_message_ids = set()

    mutations_list = {
        'Âme démoniaque': "Coût : 20 Couronnes d'Or.\n Un démon possède l'âme du mutant. " +
            "Le démon confère une sauvegarde spéciale de 4+ contre les sorts ou les prières.",
        'Pince': "Coût : 50 Couronnes d'Or.\n " +
            "Un des bras du mutant se termine par une énorme pince de crabe. " +
            "Le mutant ne porte pas d'arme avec ce bras, mais gagne une Attaque supplémentaire de Force+1 au Corps à Corps."
    }

    mutation_emojis = {
        'Âme démoniaque': '👿',
        'Pince': '🦀',
    }

    @commands.group(name='mordheim')
    async def mordheim(self, ctx):
        pass

    @mordheim.command(name="mutations")
    async def mutations(self, ctx) -> None:
        """Liste les mutations disponibles"""
        lines = [f"{self.mutation_emojis[name]} — {name}" for name in self.mutations_list]
        msg = await ctx.send('\n'.join(lines))
        self.mutation_message_ids.add(msg.id)
        for emoji in self.mutation_emojis.values():
            await msg.add_reaction(emoji)

    @mordheim.command()
    async def mutation(self, ctx, mutation: str) -> None:
        try:
            description = self.mutations_list[mutation]
        except KeyError:
            await ctx.send(f"Mutation '{mutation}' introuvable.")
            return
        await ctx.send(description)

    @Cog.listener()
    async def on_raw_reaction_add(self, payload) -> None:
        if payload.user_id == self.bot.user.id:
            return
        if payload.message_id not in self.mutation_message_ids:
            return
        emoji = str(payload.emoji)
        for name, e in self.mutation_emojis.items():
            if e == emoji:
                channel = self.bot.get_channel(payload.channel_id) or await self.bot.fetch_channel(payload.channel_id)
                await channel.send(self.mutations_list[name])
                return

async def setup(bot):
    await bot.add_cog(MordheimAction(bot))
