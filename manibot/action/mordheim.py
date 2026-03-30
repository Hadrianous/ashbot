from discord.ext import commands
from discord.ext.commands import Bot, Cog

AILES_CO = '**Ailes : 45 CO**'
PEAU_ECAILLEUSE_CO = '**Peau écailleuse : 60 CO**'
QUEUE_PREHENSILE_CO = '**Queue préhensile : 50 CO**'
MORSURE_VENIMEUSE_CO = '**Morsure venimeuse : 50 CO**'
BRUTE_EPAISSE_CO = '**Brute épaisse : 50 CO**'
CORPS_CRISTALLIN_CO = '**Corps cristallin : 60 CO**'
HIDEUX_CO = '**Hideux : 40 CO**'
BRAS_SUPPLEMENTAIRE_CO = '**Bras supplémentaire : 40 CO**'
QUEUE_DE_SCORPION_CO = '**Queue de scorpion : 40 CO**'
EPINES_CO = '**Épines : 35 CO**'
SANG_ACIDE_CO = '**Sang acide : 30 CO**'
SABOTS_FENDUS_CO = '**Sabots fendus : 40 CO**'
TENTACULE_CO = '**Tentacule : 35 CO**'
PINCE_CO = '**Pince : 50 CO**'
DEMONIAQUE_CO = '**Âme démoniaque : 20 CO**'


class MordheimAction(commands.Cog):

    def __init__(self, bot: Bot):
        self.bot = bot
        self.mutation_message_ids = set()

    mutations_list = {
        DEMONIAQUE_CO: "\nUn démon possède l'âme du mutant. " +
            "Le démon confère une sauvegarde spéciale de 4+ contre les sorts ou les prières.",
        PINCE_CO: "\n" +
            "Un des bras du mutant se termine par une énorme pince de crabe. " +
            "Le mutant ne porte pas d'arme avec ce bras, mais gagne une Attaque supplémentaire de Force+1 au Corps à Corps.",
        TENTACULE_CO: "\n" +
            "Un des bras du mutant se termine par un tentacule. " +
            "Le mutant peut agripper ses adversaires au Corps à Corps et leur faire perdre 1 Attaque, jusqu’à un minimum de 1. Le mutant peut décider quelle Attaque perd l’adversaire.",
        SABOTS_FENDUS_CO: "\nLe guerrier gagne +1 en Mouvement.",
        SANG_ACIDE_CO: "\nSi le mutant subit une blessure au Corps à Corps, les figurines en contact subissent une touche de Force 3 (pas de Coups Critiques) à cause des éclaboussures.",
        EPINES_CO: "\nToute figurine en contact avec le mutant subit automatiquement une touche de Force 1 au début de chaque phase de Corps à Corps. Les épines ne provoquent jamais de Coups Critiques.",
        QUEUE_DE_SCORPION_CO: "\nLe mutant possède une longue queue épineuse avec un dard empoisonné. Cette queue autorise une Attaque supplémentaire de Force 5, à chaque phase de Corps à Corps. Si la figurine touchée est immunisée au poison, la Force de la touche est réduite à 2.",
        BRAS_SUPPLEMENTAIRE_CO: "\nLe mutant peut utiliser n’importe quelle arme à une main avec son bras supplémentaire, ce qui lui donne donc une Attaque supplémentaire au Corps à Corps. Il peut également utiliser un bouclier ou une rondache. Si un mutant choisit cette option, il gagne une Attaque supplémentaire, mais ne peut pas porter d’arme supplémentaire.",
        HIDEUX_CO: "\nLe mutant est si laid qu’il provoque la peur. Voir le chapitre Psychologie pour plus de détails.",
        CORPS_CRISTALLIN_CO: "\nLe corps du mutant devient du cristal vivant, à la fois dur et cassant. L’Endurance du mutant passe à 6 et ses Points de Vie à 1. Aucune de ces caractéristiques ne peut être modifiée par l'expérience ou par une autre mutation. Si un jet de progression tombe sur l’augmentation de l’Endurance ou des PV, relancez jusqu'à ce qu'une augmentation de caractéristique différente soit obtenue.",
        BRUTE_EPAISSE_CO: "\nLa puissance du Chaos confère à ce guerrier une force surhumaine. Tandis que sa masse musculaire double de volume, étirant sa peau sous la pression, sa vivacité d’esprit s’amenuise. Le guerrier ajoute +2 à sa Force, mais subit un malus de -4 en Cd.",
        MORSURE_VENIMEUSE_CO: "\nLe mutant développe de petits crocs qui peuvent sécréter un puissant poison. À moins que le guerrier n'ait déjà une Attaque de morsure, il gagne une Attaque supplémentaire au Corps à Corps. La morsure venimeuse est une Attaque de Force 5, mais elle est réduite à Force 2 si la cible est immunisée aux poisons. Si le mutant possède déjà une Attaque de morsure, elle est simplement améliorée pour inclure cet effet.",
        QUEUE_PREHENSILE_CO: "\nUne queue préhensile pousse sur le mutant. À moins qu’il n'ait déjà une Attaque de queue, le mutant gagne une Attaque supplémentaire au Corps à Corps. Cette queue préhensile lui permet de tenir et d’utiliser une arme à une main, un bouclier ou une rondache s’ils sont disponibles dans sa liste d’équipement. Les guerriers incapables d’utiliser des armes le reste donc. Si le mutant possède plusieurs queues, au début de chaque phase de Corps à Corps, il doit choisir laquelle sera utilisée.",
        PEAU_ECAILLEUSE_CO: "\nUne fine couche d'écailles reptiliennes recouvre la chair du guerrier. Atteint par la distorsion mutagène, il reçoit une protection naturelle lui conférant une sauvegarde d’armure de 5+. Les malus de sauvegarde ne peuvent pas modifier celle-ci au-delà de 6+, mais un résultat aucune sauvegarde sur le tableau des Coups Critiques l’annulera. Les armures légères ajoutent +1 à la sauvegarde d’armure, comme toute autre protection.",
        AILES_CO: "\nLe mutant développe une paire d'ailes, à plumes comme celles d’un oiseau ou de cuir comme celles d’une chauve-souris. Ces ailes ne sont pas assez puissantes pour permettre au mutant de voler à proprement parler, mais elles lui permettent de planer à partir d'une position élevée. Si le mutant se trouve sur une plate-forme surélevée – comme un toit, une passerelle ou une falaise – il peut planer vers le bas : pour 1ps de chute, le mutant avance de 2ps horizontalement.",
    }

    mutation_emojis = {
        DEMONIAQUE_CO: '👿',
        PINCE_CO: '🦀',
        TENTACULE_CO: '🐙',
        SABOTS_FENDUS_CO: '🦶',
        SANG_ACIDE_CO: '🧪',
        EPINES_CO: '🌵',
        QUEUE_DE_SCORPION_CO: '🦂',
        BRAS_SUPPLEMENTAIRE_CO: '💪',
        HIDEUX_CO: '👹',
        CORPS_CRISTALLIN_CO: '💎',
        BRUTE_EPAISSE_CO: '🦍',
        MORSURE_VENIMEUSE_CO: '🐍',
        QUEUE_PREHENSILE_CO: '🐒',
        PEAU_ECAILLEUSE_CO: '🦎',
        AILES_CO: '🦇',
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
        await ctx.send(mutation + "\n" + description)

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
                await channel.send(name + " " + self.mutations_list[name])
                return

async def setup(bot):
    await bot.add_cog(MordheimAction(bot))
