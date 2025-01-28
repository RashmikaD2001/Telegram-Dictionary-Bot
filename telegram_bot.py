from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os
import logging
from dictionary import get_word_meanings

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# Set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")

# Initialize the Telegram bot application
application = Application.builder().token(TOKEN).build()

# Command handlers
async def start(update, context):
    await update.message.reply_text("Hello RashmikaDK Here🤖!!! Use /help to continue.")

async def help_command(update, context):
    await update.message.reply_text(
        """
        /start -> Hello Rashmika is here😎
        /help -> How can I help?
        /description -> This bot will help you to find the meaning of English words. Ask the meaning of any word.
        /meaning [word] -> Get the meaning of a word (e.g., /meaning hello)
        /contact -> Contact me using GitHub
        """
    )

async def contact(update, context):
    await update.message.reply_text("Contact me: https://github.com/RashmikaD2001")

async def description(update, context):
    await update.message.reply_text("This bot will help you to find the meaning of English words. Ask the meaning of any word.")

async def meaning(update, context):
    # Get the word from the user's message
    if not context.args:
        await update.message.reply_text("Please provide a word. Usage: /meaning [word] example: /meaning ant")
        return
    
    word = context.args[0]
    logger.info(f"Fetching meaning for: {word}")
    
    # Fetch the meaning of the word
    meanings = get_word_meanings(word)
    if isinstance(meanings, list):
        reply = f"Meanings for *{word}*:\n"
        for idx, meaning in enumerate(meanings, 1):
            reply += f"{idx}. ({meaning['partOfSpeech']}) {meaning['definition']}\n"
            reply += f"   Example: {meaning['example']}\n"
    else:
        reply = meanings  # Error message from `get_word_meanings`

    # Send the reply
    await update.message.reply_text(reply, parse_mode="Markdown")

# Add command handlers
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("description", description))
application.add_handler(CommandHandler("contact", contact))
application.add_handler(CommandHandler("meaning", meaning))

# Run the bot
if __name__ == "__main__":
    logger.info("Bot is starting...")
    application.run_polling()
