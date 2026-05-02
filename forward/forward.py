from discord.ext import commands

class Forward(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def f(self, ctx, *, msg):
        if ctx.channel.id != 1437884513702248519:
            return

        try:
            channel = await self.bot.fetch_channel(1277792057632493591)

            files = []
            for attachment in ctx.message.attachments:
                file = await attachment.to_file()
                files.append(file)

            await channel.send(msg, files=files)

            await ctx.message.add_reaction("✅")

        except Exception as e:
            await ctx.message.add_reaction("❌")
            await ctx.reply(str(e))


async def setup(bot):
    await bot.add_cog(Forward(bot))
