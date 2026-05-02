from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class Forward(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send_forward(self, ctx, msg):
        if ctx.channel.id != 1437884513702248519:
            return
        channel = self.bot.get_channel(1277792057632493591)

        files = []
        for attachment in ctx.message.attachments:
            file = await attachment.to_file()
            files.append(file)
        await channel.send(msg, files=files)
        await ctx.message.add_reaction("✅")

    @commands.command(name="forward")
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def forward(self, ctx, *, msg):
        await self.send_forward(ctx, msg)

    @commands.command(name="f")
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def f(self, ctx, *, msg):
        await self.send_forward(ctx, msg)

    @commands.command(name="i")
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def i(self, ctx):
        files = []
        for attachment in ctx.message.attachments:
            file = await attachment.to_file()
            files.append(file)
        channel = self.bot.get_channel(1277792057632493591)
        await channel.send(files=files)
        await ctx.message.add_reaction("✅")


async def setup(bot):
    await bot.add_cog(Forward(bot))
