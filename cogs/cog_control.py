from discord.ext import commands
from discord.ext.commands import NotOwner, MissingRequiredArgument

class CogControl(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx, *, name: str): # self always required
        try:
            self.bot.reload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'"**{name}**" Cog reloaded')

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, name: str):
        try:
            self.bot.unload_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'"**{name}**" Cog unloaded')
    
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, name: str):
        try:
            self.bot.load_extension(f"cogs.{name}")
        except Exception as e:
            return await ctx.send(e)
        await ctx.send(f'"**{name}**" Cog loaded')

    @load.error
    @unload.error
    @reload.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, NotOwner):
            await ctx.send("You must be the bot's owner to do that!")
        if isinstance(error, MissingRequiredArgument):
            await ctx.send("You must specify a cog!")

def setup(bot):
    bot.add_cog(CogControl(bot))