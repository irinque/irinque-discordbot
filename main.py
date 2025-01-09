from discord import Member, Intents, Client, Interaction
from discord.ext import commands
from events.on_member_join import member_join
from events.on_voice_state_update import voice_state_update
from commands.information import send_information
from commands.custom_embed import send_custom_embed
from settings import CHANNEL_RULES_ID, CHANNEL_GREETINGS_ID, ROLE_USER_ID
from config import TOKEN

intents = Intents().all()
bot = commands.Bot(command_prefix="!", intents=Intents().all())
client = Client(intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.event
async def on_member_join(member: Member):
    await member_join(member=member, role_user_id=ROLE_USER_ID, channel_id=CHANNEL_GREETINGS_ID)

@bot.event
async def on_voice_state_update(member: Member, before, after):
    await voice_state_update(member=member, before_channel=before, after_channel=after)

@bot.tree.command(name="information")
async def information(interaction: Interaction):
    await send_information(interaction=interaction, channel_id=CHANNEL_RULES_ID)

@bot.tree.command(name="custom_embed")
async def custom_embed(interaction: Interaction):
    await send_custom_embed(interaction=interaction, role_id=ROLE_USER_ID)

if __name__ == "__main__":
    bot.run(token=TOKEN)