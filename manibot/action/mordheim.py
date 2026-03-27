from discord.ext import commands
from discord.ext.commands import Bot, group


class MordheimAction(commands.Cog):

    def __init__(self, bot: Bot):
        self.bot = bot

    mutations_list = {
        'Âme démoniaque': "Coût : 20 Couronnes d’Or.\n Un démon possède l’âme du mutant." +
            "Le démon confère une sauvegarde spéciale de 4+" +
            "contre les sorts ou les prières.",
        'Pince': "Coût : 50 Couronnes d’Or. " +
            "Un des bras du mutant se termine par une énorme" +
            "pince de crabe." +
            "Le mutant ne porte pas d’arme avec ce bras, mais" +
            "gagne une Attaque supplémentaire de Force+1 au" +
            "Corps à Corps."
    }

    @commands.group(name='mordheim')
    async def mordheim(self, ctx):
        pass

    @mordheim.command(name="mutations")
    async def mutations(self, ctx: str) -> None:
        """Liste les mutations disponibles"""
        await ctx.send(', '.join(self.mutations_list.keys()))

    @mordheim.command()
    async def mutation(self, ctx, mutation: str) -> None:
        try:
            mutation = self.mutations_list[mutation]
        except KeyError:
            await ctx.send(self.mutations_list[mutation])
            return

        await ctx.send(mutation)

async def setup(bot):
    await bot.add_cog(MordheimAction(bot))