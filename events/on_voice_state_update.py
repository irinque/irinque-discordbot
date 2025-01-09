from discord.utils import get
from settings import channel_createvoice_id, category_voice_id, voices_whitelist


async def voice_state_update(member, before_channel, after_channel):
    category = get(member.guild.categories, id=category_voice_id)
    if after_channel.channel and after_channel.channel.id == channel_createvoice_id:
        channel = await member.guild.create_voice_channel(name=f'{member.name}', category=category)
        await channel.set_permissions(member, connect=True, mute_members=False, move_members=False, manage_channels=True)
        await member.move_to(channel)
    if before_channel.channel and len(before_channel.channel.members) == 0 and before_channel.channel.id not in voices_whitelist:
        await before_channel.channel.delete()