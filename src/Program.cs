using System.Text.Json;
using System.Text.Json.Serialization;
using DSharpPlus;
using DSharpPlus.Commands;
using DSharpPlus.Commands.Processors.TextCommands;
using DSharpPlus.Commands.Processors.TextCommands.Parsing;
using DSharpPlus.Entities;

class Program
{
	public static async Task Main(string[] args)
	{
		// Open the config file and get everything we need
		string configFile = File.ReadAllText("./config.json");
		Config config = JsonSerializer.Deserialize<Config>(configFile);

		// Make the Discord client (bot)
		DiscordClientBuilder clientBuilder = DiscordClientBuilder.CreateDefault(config.Token, DiscordIntents.All);
		DiscordClient client = clientBuilder.Build();

		// Say that we're using commands or something
		CommandsExtension commandsExtension = client.UseCommands(new CommandsConfiguration()
		{
			DebugGuildId = config.DebugGuildId
		});

		
		// Register all the commands
		//? I think that this assembly thing means I don't need to manually register each one
		commandsExtension.AddCommands(typeof(Program).Assembly);
		Console.WriteLine("If the slash commands aren't registering then you need to reload (close then open) the Discord client.\nYou can also do ctrl+r\n");

		// Set a status
		DiscordActivity status = new DiscordActivity("Doing the debugulations rn", DiscordActivityType.Custom);

		// Start the bot, then make the current thread run forever
		// so that the bot doesn't kill itself immediately
		await client.ConnectAsync(status, DiscordUserStatus.Online);
		await Task.Delay(-1);
	}



	// Config json outline thingy idk
	class Config
	{
		[JsonPropertyName("token")]
		public string Token { get; set; }

		[JsonPropertyName("debugGuildId")]
		public ulong DebugGuildId { get; set; }
	}
}