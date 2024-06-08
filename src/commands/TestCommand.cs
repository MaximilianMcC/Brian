using DSharpPlus.Commands;

public class TestCommand
{
	[Command("test")]
	public static async Task ExecuteAsync(CommandContext context)
	{
		// Flick back the ping
		await context.RespondAsync($"{context.Client.Ping}ms");
	}
}
