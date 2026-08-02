import os
import discord
from discord import app_commands

class B401(discord.Client):
  def __init__(self, *, intents: discord.Intents):
    super().__init__(intents=intents)
    self.tree = app_commands.CommandTree(self)

intents = discord.Intents.all()
client = B401(intents=intents)

client.run(os.environ["TOKEN"])
