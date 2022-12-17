import discord, json

# Get the config data
config = json.load(open("./config.json", "r"))



# Make brian
brian = discord.Bot(debug_guilds=config["debug_guilds"])



# When Brian is ready
@brian.event
async def on_ready():
    print(f"Brain is online!")


# Test command
@brian.slash_command(description="test")
async def test(ctx):
    await ctx.respond(f"Roundtrip ping latency {brian.latency}🤓")



# Start Brian
print("Loading...")
brian.run(config["token"])