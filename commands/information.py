from discord.utils import get
from discord import Embed, Colour, Interaction
from settings import title_rules_ru, title_rules_en, description_rules_ru, description_rules_en, color_embed

async def send_information(interaction: Interaction, channel_id):
    channel = get(interaction.guild.channels, id=channel_id)
    embed_ru = Embed(title=title_rules_ru, description=description_rules_ru, colour=Colour.from_str(color_embed))
    embed_en = Embed(title=title_rules_en, description=description_rules_en, colour=Colour.from_str(color_embed))
    await channel.send(embed=embed_ru)
    await channel.send(embed=embed_en)
    await interaction.response.send_message("✅")
    await interaction.delete_original_response()