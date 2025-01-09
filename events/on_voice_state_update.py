from discord.utils import get
from settings import CHANNEL_CREATEVOICE_ID, CATEGORY_VOICE_ID, VOICES_WHITELIST


async def voice_state_update(member, before_channel, after_channel):
    category = get(member.guild.categories, id=CATEGORY_VOICE_ID)
    if after_channel.channel and after_channel.channel.id == CHANNEL_CREATEVOICE_ID:
        channel = await member.guild.create_voice_channel(name=f'{member.name}', category=category)
        await channel.set_permissions(member, connect=True, mute_members=False, move_members=False, manage_channels=True)
        await member.move_to(channel)
    if before_channel.channel and len(before_channel.channel.members) == 0 and before_channel.channel.id not in VOICES_WHITELIST:
        await before_channel.channel.delete()