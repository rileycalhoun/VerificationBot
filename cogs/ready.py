from discord.ext import commands

class Ready(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Logged in as {0.user}!".format(self.bot))



def setup(bot):
    print("Registering Ready Handler")
    bot.add_cog(Ready(bot))

def teardown(bot):
    print("Taking down Ready Handler")