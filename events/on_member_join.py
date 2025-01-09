from discord.utils import get
from discord import Embed, Colour
from settings import COLOR_EMBED, title_member_join, description_member_join

async def member_join(member, role_id, channel_id):
    role = get(member.guild.roles, id=role_id)
    channel = get(member.guild.channels, id=channel_id)
    embed = Embed(title=title_member_join, description=description_member_join, colour=Colour.from_str(COLOR_EMBED))
    embed.set_thumbnail(url=member.avatar.url)
    await member.add_roles(role)
    await channel.send(embed=embed)