from http import client

import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# Set up discord client
class Client(discord.Client):
    """A custom Discord client serving as the main bot instance."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.logger = logging.getLogger('discord')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
        handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
        self.logger.addHandler(handler)

    async def on_ready(self):
        """Event handler called when the bot is ready."""
        self.logger.info(f'Logged in as {self.user} (ID: {self.user.id})')
        self.logger.info('------')

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = Client(intents=intents)
client.run(token)

"""
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

bot.run(token, log_handler=handler, log_level=logging.DEBUG)
"""
