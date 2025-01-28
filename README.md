# Telegram Dictionary Bot

This is a simple Telegram bot that fetches word meanings from an online dictionary API and responds to user queries. The bot is built using the `python-telegram-bot` library.

## Link : https://t.me/test_telegram_2001_bot

## Features
- **Word Lookup**: Use `/meaning [word]` to fetch the definition, part of speech, and example usage of the word.
- **Commands**:
  - `/start`: Greet the user.
  - `/help`: Display available commands and usage instructions.
  - `/description`: Describe the bot's functionality.
  - `/contact`: Provide contact information (e.g., GitHub link).

## How It Works
1. Users send commands to the bot, such as `/meaning ant`.
2. The bot extracts the word from the command and queries an online dictionary API (e.g., [dictionaryapi.dev](https://dictionaryapi.dev)).
3. The API returns the word's meanings, part of speech, and example usage, which the bot formats and sends back to the user.

## Example Usage
### Commands
- **/start**
  ```
  Hello RashmikaDK Here🤖!!! use /help to continue
  ```

- **/help**
  ```
  /start -> Hello Rashmika is here😎
  /help -> How can I help?
  /description -> This bot will help you to find the meaning of the English words. Ask the meaning of the word
  /contact -> Contact me using GitHub
  ```

- **/meaning {word}**
  ```
  Meanings for word:
  Ex: /meaning ant
  1. (noun) A small insect typically having a sting and living in a complex social colony.
     Example: Ants are known for their cooperative behavior.
  ```

- **/contact**
  ```
  Contact me: https://github.com/RashmikaD2001
  ```

## Requirements
- Python 3.7+
- `python-telegram-bot` library
- `requests` library
- `.env` file containing the bot's Telegram API token:
  ```
  TOKEN=your_telegram_bot_token
  ```
## API Used
- [Dictionary API](https://dictionaryapi.dev): Free API to fetch word definitions.

## Notes
- The bot uses `parse_mode='Markdown'` for rich-text formatting.
- Handles invalid inputs and provides helpful error messages.
