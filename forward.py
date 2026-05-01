import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

import datetime

class Forward(commands.Cog):
    """Forward a message!"""

    def __init__(self, bot):
        self.bot = bot

    @checks.thread_only()
    @checks.has_permissions(PermissionLevel.SUPPORTER)

    @commands.command()
    async def rename(self, ctx, *, msg):
      try:
          channel = await bot.fetch_channel(1277792057632493591)

          files = []
          for attachment in ctx.message.attachments:
              file = await attachment.to_file()
              files.append(file)

          await channel.send(msg, files=files)

          await ctx.message.add_reaction("✅")
      except Exception as e:
          await ctx.message.add_reaction("❌")
          await ctx.reply(e)

async def setup(bot):
    await bot.add_cog(Forward(bot))
