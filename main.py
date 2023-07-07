import discord
from discord import app_commands
from PIL import Image, ImageDraw, ImageFont
import json, requests
from io import BytesIO


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




# Test command
@command_tree.command(name="test", description="Development command", guilds=debug_guilds)
async def self(interaction: discord.Interaction):
	await interaction.response.send_message(":nerd:")


# esmBot style caption command
@command_tree.command(name="caption", description="Add a meme caption to an image", guilds=debug_guilds)
@app_commands.describe(image_url = "The image that you want to add the caption to")
@app_commands.describe(caption = "The caption text that will be added to the image")
async def self(interaction: discord.Interaction, image_url: discord.Attachment , caption: str):

	# Get the image
	response = requests.get(image_url)
	image = Image.open(BytesIO(response.content))

	# Add the header thingy to the image
	old_width, old_height = image.size
	padding = 20
	new_width = old_width
	caption_height = (old_height // 10) + padding
	new_height = old_height + caption_height
	new_image = Image.new("RGB", (new_width, new_height), 0xffffff)
	draw = ImageDraw.Draw(new_image)
	new_image.paste(image, (0, caption_height))

	# Get the text and font
	text = "Hello, world!"
	font_size = old_height // 10
	font = ImageFont.truetype("./Futura Extra Bold Condensed.otf", font_size)
	
	# Calculate the position for the text
	# TODO: Add word wrap
	text_width = font.getsize(text)[0]
	text_height = font.getsize(text)[1]
	image_width = image.width
	text_x = (image_width - text_width) / 2
	text_y = (caption_height - text_height) / 2

	# Add the text to the image
	draw.text((text_x, text_y), text, font=font, fill=0x000000)

	# Send the image in discord
	new_image.show()

	await interaction.response.send_message(f"{caption} {image}")


# Run the bot
client.run(config["token"])