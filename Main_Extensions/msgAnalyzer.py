from discord.ext import commands

import sys
sys.path.append("..")
from Database.db import SqliteDataBase

class CommandExtension(commands.Cog):

    def __init__(self, bot) -> None:

        self.bot = bot
        self.message_database = SqliteDataBase()

def setup(bot) : bot.add_cog(CommandExtension(bot))