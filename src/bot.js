// Import stuff and JSON settings
const { Client, Collection, Events, GatewayIntentBits } = require('discord.js');
const fileSystem = require("fs");
const path = require("path");
const { token } = require("../config.json");

// Make a new discord bot client
const client = new Client({
	intents: [GatewayIntentBits.Guilds]
});

// Store all of the commands
client.commands = new Collection();

// update commands (stolen from guide)
const foldersPath = path.join(__dirname, 'commands');
console.log(`Reading commands from: ${foldersPath}`);
const commandFolders = fileSystem.readdirSync(foldersPath);

for (const folder of commandFolders) {
	const commandsPath = path.join(foldersPath, folder);
	if (!fileSystem.statSync(commandsPath).isDirectory()) {
		console.log(`[SKIPPING] ${commandsPath} is not a directory`);
		continue;
	}
	console.log(`Processing directory: ${commandsPath}`);
	const commandFiles = fileSystem.readdirSync(commandsPath).filter(file => file.endsWith('.js'));
	for (const file of commandFiles) {
		const filePath = path.join(commandsPath, file);
		console.log(`Loading command file: ${filePath}`);
		const command = require(filePath);
		if ('data' in command && 'execute' in command) {
			client.commands.set(command.data.name, command);
			console.log(`Registered command: ${command.data.name}`);
		} else {
			console.log(`[WARNING] The command at ${filePath} is missing a required "data" or "execute" property.`);
		}
	}
}

// When the client is ready
console.log("Loading...");
client.once(Events.ClientReady, readyClient => {
	console.log(`Done! logged in as ${readyClient.user.username} (${readyClient.user.tag})\n`);
});

// When a user sends a command to the bot
client.on(Events.InteractionCreate, async interaction => {
	// Get the command
	if (!interaction.isChatInputCommand()) return;
	console.log(`Received command: ${interaction.commandName}`);
	const command = interaction.client.commands.get(interaction.commandName);

	// idk stolen from guide again
	try {
		if (!command) {
			console.error(`Command not found: ${interaction.commandName}`);
			await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
			return;
		}
		await command.execute(interaction);
	} catch (error) {
		console.error(error);
		if (interaction.replied || interaction.deferred) {
			await interaction.followUp({ content: 'There was an error while executing this command!', ephemeral: true });
		} else {
			await interaction.reply({ content: 'There was an error while executing this command!', ephemeral: true });
		}
	}
});

// Login and actually run the bot
client.login(token);