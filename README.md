# Discord Bot: Oreo

Oreo is a simple Discord bot with basic functionalities. It can greet users, echo messages, welcome members when they join, and provide current weather information for a given city.

## Features

1. **Greeting**: The bot can greet users.
2. **Echo**: The bot can repeat what you ask it to say.
3. **Welcome**: The bot sends a welcome message to new members when they join the server.
4. **Weather**: Users can get the current weather for a given city.

## Commands

1. `!hello`: Greets the user.
2. `!say [message]`: The bot will echo back the message.
3. `!weather [city_name]`: Fetches the weather for the given city.

## Prerequisites

- Python
- Discord.py library
- An OpenWeatherMap API key

## Installation and Setup

1. **Token Setup**:
   Save your Discord bot token in a file named `token.txt`.

2. **API Key Setup**:
   Replace the existing API key in the `weather` function with your OpenWeatherMap API key.

3. **Python Libraries**:
   Install the required libraries using pip:

   ```bash
   pip install discord.py requests
   ```

4. **Run the Bot**:
   Simply run the provided python script to start the bot:

   ```bash
   python [filename].py
   ```

## Known Issues

- Ensure your bot has the necessary permissions to read messages and send messages in the channel.
- The weather command fetches the weather using OpenWeatherMap. Ensure you use a valid and active API key, or the command will fail.

## Future Work

- Add more detailed error handling for edge cases, such as when the city is not found or the API limit is reached.
- Expand bot functionality with more useful and interactive commands.

## Contributing

Contributions are always welcome. Ensure you follow the standard coding conventions and comment on your changes adequately.

## License

This project is open-source and available to anyone. Ensure to mention the original author when using or modifying this bot for your purposes.
