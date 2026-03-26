from discord.ext import commands
from discord.ext.commands import Bot


class MordheimAction(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    mutations_list = {
        'Âme démoniaque': "Coût : 20 Couronnes d’Or. Un démon possède l’âme du mutant." +
            "Le démon confère une sauvegarde spéciale de 4+" +
            "contre les sorts ou les prières.",
        'Pince': "Coût : 50 Couronnes d’Or. " +
            "Un des bras du mutant se termine par une énorme" +
            "pince de crabe." +
            "Le mutant ne porte pas d’arme avec ce bras, mais" +
            "gagne une Attaque supplémentaire de Force+1 au" +
            "Corps à Corps."
    }

    @commands.hybrid_command()
    async def mutations(self, ctx):
        await ctx.send(', '.join(self.mutations_list.keys()))

    @commands.hybrid_command()
    async def mutation(self, ctx, mutation: str):
        try:
            mutation = self.mutations_list[mutation]
        except KeyError:
            await ctx.send(self.mutations_list[mutation])
            return

        await ctx.send(mutation)

async def setup(bot):
    await bot.add_cog(MordheimAction(bot))