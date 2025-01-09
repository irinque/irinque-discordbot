from discord import Member, Intents, Client, Interaction
from discord.ext import commands
from events.on_member_join import member_join
from events.on_voice_state_update import voice_state_update
from commands.send_information import send
from commands.custom_embed import send_custom_embed
from config import TOKEN
from settings import channel_rules_id, channel_greetings_id, role_user_id

intents = Intents().all()
bot = commands.Bot(command_prefix="!", intents=Intents().all())
client = Client(intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()

@bot.event
async def on_member_join(member: Member):
    await member_join(member=member, role_user_id=role_user_id, channel_id=channel_greetings_id)

@bot.event
async def on_voice_state_update(member, before, after):
    await voice_state_update(member=member, before_channel=before, after_channel=after)

@bot.tree.command(name="send_information", description="Send embeds with infomation")
async def send_information(interaction: Interaction):
    await send(interaction=interaction, channel_id=channel_rules_id)

@bot.tree.command(name="custom_embed", description="Embed to channel")
async def custom_embed(interaction: Interaction):
    await send_custom_embed(interaction=interaction, role_id=role_user_id)

if __name__ == "__main__":
    bot.run(token=TOKEN)