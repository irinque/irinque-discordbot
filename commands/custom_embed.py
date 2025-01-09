from discord.ui import TextInput, Modal, ChannelSelect, View
from discord.utils import get
from discord import Embed, TextStyle, Interaction, Colour, ChannelType, Interaction
from settings import COLOR_EMBED, label_title_post, label_description_post, label_mention_post, label_image_post, label_title

async def send_custom_embed(interaction: Interaction, role_id):
    async def select_callback(interaction: Interaction):
        channel_name = dropdown.values[0]
        channel = get(interaction.guild.channels, name=str(channel_name))
        class SendApplication(Modal, title=label_title):
            title_post = TextInput(label=label_title_post, style=TextStyle.short)
            description_post = TextInput(label=label_description_post, style=TextStyle.long, required=True)
            mention_post = TextInput(label=label_mention_post, style=TextStyle.short, required=True)
            image_post = TextInput(label=label_image_post, style=TextStyle.short, required=False)
            async def on_submit(self, interaction: Interaction):
                embed = Embed(title=self.title_post, description=self.description_post, colour=Colour.from_str(COLOR_EMBED))
                if self.image_post:
                    embed.set_image(url=self.image_post)
                role_user = get(interaction.guild.roles, id=role_id)
                if str(self.mention_post).lower() == "да":
                    await channel.send(content=f"{role_user.mention}", embed=embed)
                    await interaction.response.send_message(f"✅")
                    await interaction.delete_original_response()
                if str(self.mention_post).lower() == "нет":
                    await channel.send(embed=embed)
                    await interaction.response.send_message(f"✅")
                    await interaction.delete_original_response()
                await selection.delete()
        await interaction.response.send_modal(SendApplication())
    view = View()
    dropdown = ChannelSelect(channel_types=[ChannelType.text, ChannelType.news], min_values=1, max_values=1)
    dropdown.callback = select_callback
    view.add_item(dropdown)
    selection = await interaction.channel.send(view=view)
    await interaction.response.send_message(f"👇")
    await interaction.delete_original_response()