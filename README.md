# **BigBrian Bot**

A multipurpose Discord bot.


## **Cloning the bot**
If you'd like to clone the bot you must make a `config.json` file in the root directory. This is what the file should look like:
```json
{
    "token": "<discord bot token>",
    "debug_guilds": [<debug guild id>, <debug guild id>, <debug guild id>],

    "openai_key": "<openai api key>"
}
```
- `token` is used to make the Discord bot
- `debug_guilds` are used to test the bot's slash commands
- `openai_key` is used to generate Photoshop ideas using AI



**You can use *[this link](https://discord.com/api/oauth2/authorize?client_id=823113494500605975&permissions=8&scope=bot%20applications.commands)* to invite Brian to your server**