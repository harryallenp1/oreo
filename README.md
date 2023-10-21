# Discord Bot: Oreo

This is a simple Discord bot named "Oreo" that responds to specific commands and welcomes new members when they join a server.

## Requirements:
- Python 3.x
- `discord.py` library with app commands

## Setup:

1. **Token**:
    Before running the bot, you need to have a Discord token. This token should be saved in a file named `token.txt`. The first line of this file should be the token itself.
   
2. **Installing required packages**:
   Use pip to install the required packages:
   ```
   pip install discord.py
   ```

## Features:

1. **Startup**: 
    - When the bot starts, it will print "Bot is up and ready :)".
    - It will then attempt to sync its slash commands with Discord, and print the number of synced commands.

2. **Commands**:
   
   - `!hello`: 
       The bot responds with a greeting and mentions the user.
       Example:
       ```
       User: !hello
       Oreo: Hello @User! my name is Oreo.....Nice to meet you.....:)))
       ```
   
   - `!say <message>`:
       The bot will respond saying the message as if it was said by the user.
       Example:
       ```
       User: !say I love ice cream
       Oreo: User said: 'I love ice cream'
       ```

3. **Member Welcome**:
    Whenever a new member joins the server, the bot will send a welcome message in the specified channel with the ID `1117138124133367872`.

## Running the Bot:

Simply execute the provided Python script:
```
python <filename>.py
```

Replace `<filename>` with the name you've saved the provided code under.

**Note**: Ensure you replace the channel ID in the `on_member_join` function with the ID of your desired welcome channel if it's different. Also, always ensure to keep your token secret.
