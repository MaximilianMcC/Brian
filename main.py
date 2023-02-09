import discord
from discord import app_commands
import json


class botClient(discord.Client):
    
    # Create the discord client
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False

    # When the bot loads
    async def on_ready(self):
        await self.wait_until_ready()

        # Check for if the bot is synced, if not then sync it
        if not self.synced:
            await command_tree.sync(guild=discord.Object(id=config["debug_guilds"][0]))
            print("Synced commands")



# Get all of the config info
config = json.load(open("./config.json", "r"))

# Get all of the guild ids and turn them into guilds
debug_guilds = []
for guild in config["debug_guilds"]:
    debug_guilds.append(discord.Object(id=guild))


# Make the client and command tree
client = botClient()
command_tree = app_commands.CommandTree(client)
6



# Test command
@command_tree.command(name="test", description="Development command", guilds=debug_guilds)
async def self(interaction: discord.Interaction):
    await interaction.response.send_message(":nerd: amo6")


# Hello command
@command_tree.command(name="hello", description="Development command", guilds=debug_guilds)
async def self(interaction: discord.Interaction, name: str):
    await interaction.response.send_message("Hello " + name)



# Run the bot
client.run(config["token"])