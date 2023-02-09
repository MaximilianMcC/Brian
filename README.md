# **BigBrian Bot**

A multipurpose Discord bot.


## **Cloning the bot**
If you'd like to clone the bot you must make a `config.json` file in the root directory. This is what the file should look like:
```json
{
    "token": <discord bot token>,
    "debug_guilds": [<debug guild id>, <debug guild id>, <debug guild id>],

    "openai_key": <openai api key>
}
```
- `token` is used to make the Discord bot
- `debug_guilds` are used to test the bot's slash commands
- `openai_key` is used to generate art ideas using AI

This bot uses the many different libraries to work. Here are the commands needed to install them:
```sh
pip install discord.py
pip install json
pi install openai
```


**You can use *[this link](https://discord.com/api/oauth2/authorize?client_id=823113494500605975&permissions=8&scope=bot%20applications.commands)* to invite Brian to your server**

## **Running in the background as a process (on windows using pwsh)**
If you would like to run Brian without constantly having the console window open you can start it as a new process. To do this, open Powershell and go into the root directory. Once there, run this command:
```sh
pythonw.exe .\main.py
```
Brian will now be running as a process. To view this process you can use this command, or alternatively use Task Manager.
```sh
Get-Process pythonw
```
This command should show a large list of all of the different processes running on your computer. Scroll down until you find one called `pythonw`. You can also use the name as an argument as shown above. To stop Brian, you must get the `pid`(process id) of `pythonw`.

This is an example of what the line should look like. The pid is the second number to the left of the name. In this case, the pid is `16236`.
```sh
NPM(K)    PM(M)      WS(M)     CPU(s)      Id  SI ProcessName
------    -----      -----     ------      --  -- -----------
    31   391.55      51.07       0.28   16236   1 pythonw
```
To kill the process, you must run `taskkill.exe /pid <process id> /f`. Here is an example using the above process number:
```sh
taskkill.exe /pid 16236 /f
```
Once this command is ran the process should be stopped, meaning the bot will be offline. You can double check that the process is killed by running `Get-Process` again if you'd like. If it worked you should get an output like this:
```sh
SUCCESS: The process with PID 16236 has been terminated.
```

It is possible to kill the process by name, however this isn't a good thing to do because you could be running multiple things at the same time, and they will all have the name of `pythonw`.

Here is the total process of creating, then killing the process for if you're confused:
```sh
# Start the process
pythonw.exe .\main.py

# Find the process id
Get-Process pythonw

# Kill the process
taskkill.exe /pid <process id> /f
```