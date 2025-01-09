from discord.ui import TextInput, Modal, ChannelSelect, View
from discord.utils import get
from discord import Embed, TextStyle, Interaction, Colour, ChannelType, Interaction
from settings import color_embed

async def send_custom_embed(interaction: Interaction, role_id):
    async def select_callback(interaction: Interaction):
        channel_name = dropdown.values[0]
        channel = get(interaction.guild.channels, name=str(channel_name))
        class SendApplication(Modal, title="📝 EMBED"):
            message_title = TextInput(label="🎴 ЗАГОЛОВОК", style=TextStyle.short)
            description = TextInput(label="🀄 ОПИСАНИЕ", style=TextStyle.long, required=True)
            mention = TextInput(label="📣 УПОМИНАНИЕ(Да/Нет)", style=TextStyle.short, required=True)
            image = TextInput(label="🌄 КАРТИНКА", style=TextStyle.short, required=False)
            async def on_submit(self, interaction: Interaction):
                embed = Embed(title=self.message_title, description=self.description, colour=Colour.from_str(color_embed))
                if self.image:
                    embed.set_image(url=self.image)
                role_user = get(interaction.guild.roles, id=role_id)
                if str(self.mention).lower() == "да":
                    await channel.send(content=f"{role_user.mention}", embed=embed)
                    await interaction.response.send_message(f"✅")
                    await interaction.delete_original_response()
                if str(self.mention).lower() == "нет":
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