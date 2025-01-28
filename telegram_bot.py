from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os
import logging

# Enable logging

logging.basicConfig(

    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO

)

# set higher logging level for httpx to avoid all GET and POST requests being logged

logging.getLogger("httpx").setLevel(logging.WARNING)


logger = logging.getLogger(__name__)

load_dotenv()
TOKEN = os.getenv("TOKEN")

application = Application.builder().token(TOKEN).build()

async def start(update, context):
    await update.message.reply_text("Hello RashmikaDK Here🤖!!! use /help to continue")

async def help_command(update, context):
    await update.message.reply_text(
        """
        /start -> Hello Rashmika is here😎
        /help -> How can I help?
        /content -> I can help you to learn programming
        /python -> Video to Learn Python 
        /sql -> Video to Learn SQL
        /java -> Video to Learn Java
        /contact -> Contact me using GitHub
        """
    )

async def content(update, context):
    await update.message.reply_text("We have various playlist and articles available")

async def python(update, context):
    await update.message.reply_text("Python tutorial link : https://youtu.be/ix9cRaBkVe0?si=1kNerHAeQsM-EDom")

async def sql(update, context):
    await update.message.reply_text("SQL tutorial link : https://youtu.be/5OdVJbNCSso?si=jlDscV_pHujnaxWp")

async def java(update, context):
    await update.message.reply_text("Java tutorial link : https://youtu.be/xk4_1vDrzzo?si=8Fb96iWd0Wl5T_XI")

async def contact(update, context):
    await update.message.reply_text("Contact me: https://github.com/RashmikaD2001")


application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("content", content))
application.add_handler(CommandHandler("python", python))
application.add_handler(CommandHandler("sql", sql))
application.add_handler(CommandHandler("java", java))
application.add_handler(CommandHandler("contact", contact))

if __name__ == "__main__":
    application.run_polling()
    logger.info("Bot is starting...")