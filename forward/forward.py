import discord
from discord.ext import commands
from core import checks
from core.models import PermissionLevel

class Forward(commands.Cog):
    """Forwarding module for Novision Support"""
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

    @commands.command(name="forward", help="Forward a message + files(optional)", usage="<message> & .forward <message> + <files>")
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def forward(self, ctx, *, msg):
        await self.send_forward(ctx, msg)

    @commands.command(name="f", help="Forward a message + files(optional)", usage="<message> & .forward <message> + <files>")
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def f(self, ctx, *, msg):
        await self.send_forward(ctx, msg)

    @commands.command(name="i", help="Forward just files with no message.", usage="<file/s>")
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def i(self, ctx):
        files = []
        for attachment in ctx.message.attachments:
            file = await attachment.to_file()
            files.append(file)
        channel = self.bot.get_channel(1277792057632493591)
        await channel.send(files=files)
        await message.add_reaction("✅")

    async def public(self, message):
        embed = discord.Embed(description=message.content)
        embed.set_author(name=message.author.name, icon_url=message.author.display_avatar.url)
        embed.set_footer(text=str(message.id))
        files = []
        for attachment in message.attachments:
            file = await attachment.to_file()
            files.append(file)
        channel = self.bot.get_channel(1437157847229009931)
        if channel is None:
            channel = await self.bot.fetch_channel(1437157847229009931)
        await channel.send(files=files, embed=embed)
        

    async def private(self, message):
        files = []
        for attachment in message.attachments:
            file = await attachment.to_file()
            files.append(file)
        ref = message.reference
        if ref is None:
            channel = self.bot.get_channel(1277792057632493591)
            return await channel.send(message.content, files=files)

        if ref and ref.message_id:
            try:
                replied = await message.channel.fetch_message(ref.message_id)
            except discord.NotFound:
                replied = None

        embed = replied.embeds[0]
        rep_id = int(embed.footer.text)
        channel = self.bot.get_channel(1277792057632493591)
        msg2 = await channel.fetch_message(rep_id)
        await msg2.reply(message.content, files=files)
        

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.channel.id == 1277792057632493591:
            await self.public(message)
        elif message.channel.id == 1437157847229009931:
            await self.private(message)
            await message.add_reaction("✅")

        # IMPORTANT if you still want commands to work
        await self.bot.process_commands(message)


async def setup(bot):
    await bot.add_cog(Forward(bot))
