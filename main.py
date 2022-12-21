import discord, json, random, openai, requests
from datetime import datetime

# Get the config data
config = json.load(open("./config.json", "r"))



# Make brian
brian = discord.Bot(debug_guilds=config["debug_guilds"])


# Set the open ai key
openai.api_key = config["openai_key"]


# When Brian is ready
@brian.event
async def on_ready():
    print(f"Brain is online!")


# Test command
@brian.slash_command(description="test")
async def test(ctx):
    await ctx.respond(f"Roundtrip ping latency {brian.latency}🤓")



# Info command
@brian.slash_command(description="Get information about Brian")
async def info(ctx):

    # Information embed
    description = """
    Brian is a multipurpose Discord bot. There isn't really a set theme or idea for the bot. Whenever I think of a command I just add it to Brian.

    You can use the `/github` command to view Brian's Github repository
    """
    embed = discord.Embed(title="Brian Information", description=description)
    embed.color = 0xeda711

    # Send the embed
    await ctx.respond(embed=embed)


# Github command
@brian.slash_command(description="View Brain's github repo")
async def github(ctx):

    # Make the embed
    description = """
    Brian is an open source Discord bot. This means people can read all of Brian's code.

    Click the button below to visit the repo.
    """
    embed = discord.Embed(title="GitHib link", description=description)
    embed.color = 0xeda711
    embed.set_thumbnail(url="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png")

    # Make a button with the github link
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="GitHub Repo Link", url="https://github.com/MaximilianMcC/Brian", row=0))

    # Send the embed
    await ctx.respond(embed=embed, view=view)


# Coin flip command
@brian.slash_command(description="Flip a coin and get heads or tails")
async def coinflip(ctx):

    # Flip the coin
    flip = random.choice(["Heads", "Tails"])

    embed = discord.Embed(title=f"The answer is **{flip}**!")
    embed.color = 0xeda711
    embed.set_image(url="https://media.tenor.com/tewn7lzVDgcAAAAC/coin-flip-flip.gif")

    await ctx.respond(embed=embed)


# Random number command
@brian.slash_command(description="Get a random number")
async def random_number(ctx, min: int, max: int):
    await ctx.respond(random.randrange(min, max))


# Art prompt generator
@brian.slash_command(description="Generate an art prompt using AI")
async def art_prompt(ctx):

    # Get the prompt
    prompt = "Generate a short prompt in Photoshop. This must include theme subject place and media type. The media type could be something like movie poster,billboard advertisement,album cover,etc..."

    # Ask OpenAI the question
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=2000
    )

    # Parse the output
    output = response["choices"][0]["text"].strip()

    # Put it in an embed
    description = f"Your prompt is...\n***{output}***"
    embed = discord.Embed(title="Art prompt result:", description=description)
    embed.color = 0xeda711
    embed.set_footer(text="🚨🚨⚠️Please do not spam this command. It was generated using AI and is expensive to run🤓")
    await ctx.respond(embed=embed)


# Day command
@brian.slash_command(description="Get a gif about the current day")
async def day(ctx):

    # Settings
    # TODO: Get my own key not the tutorial one
    key = "LIVDSRZULELA"
    results = 4
    prompt = datetime.now().strftime("%A") + " day"

    # Get the gif
    request = requests.get(f"https://g.tenor.com/v1/search?q={prompt}&key={key}&limit={results}")
    gif_json = json.loads(request.content)
    gif = gif_json["results"][random.randrange(1, results)]["url"]

    await ctx.respond(gif)


# Start Brian
print("Loading...")
brian.run(config["token"])