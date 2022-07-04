
from discord import utils
from random import sample, shuffle
from string import ascii_letters, digits
from discord.ext import commands

class Verification(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
        self.codes = {}

    @commands.Cog.listener()
    async def on_member_join(self, member):
        code = self.generate_code()
        await member.send(f"Your code is `{code}`")
        self.codes[member.id] = code
        
    @commands.command()
    async def verify(self, ctx, *, token: str):
        author = ctx.message.author
        role = ctx.guild.get_role(993310313011232768) # get verified role
        if role in author.roles:
            await ctx.send("You are already verified!")
            return

        if author.id not in self.codes:
            self.codes[author.id] = self.generate_code()
            author.send(f"Your code is {self.codes[author.id]}")

        code = self.codes[author.id]
        print(token == code)
        if token == code:
            await author.add_roles(role) # add the role to the user
            await ctx.send("You have successfully verified your account!") # send verification message
        else:
            await ctx.send("That is an invalid code!")

    @verify.error
    async def on_command_error(self, ctx, error):
        author = ctx.message.author
        role = ctx.guild.get_role(993310313011232768) # get verified role
        if role in author.roles:
            await ctx.send("You are already verified!")
            return

        if author.id not in self.codes:
            self.codes[author.id] = self.generate_code()
            await author.send(f"Your code is {self.codes[author.id]}")

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You must specify a code!")

    def generate_code(self):
        letters = sample(ascii_letters, 8)
        numbers = sample(digits, 8)

        code = letters + numbers
        shuffle(code)
        return ''.join(code)


def setup(bot):
    bot.add_cog(Verification(bot))