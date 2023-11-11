import discord
from discord import app_commands
from discord import ui


intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

class Questionnaire(ui.Modal, title='Create Embed'):
    Title = ui.TextInput(label='Title')
    content = ui.TextInput(label='Content', style=discord.TextStyle.long)
    footer = ui.TextInput(label='Footer')

    async def on_submit(self, interaction: discord.Interaction):
        embed = discord.Embed(title=f"{self.Title}", description=f"{self.answer}", colour=discord.Colour.random())
        embed.set_footer(text = f"{self.footer}")
        await interaction.channel.send(embed=embed)
        await interaction.response.send_message(f'Embed Created', ephemeral=True)


@tree.command(name = "embed", description = "test", guild=discord.Object(id=1172581606687518750))
async def createEmbed(interaction: discord.Interaction): # title:str, description:str, footer:str)
    # embed = discord.Embed(title=f"{title}", description=f"{description}", colour=discord.Colour.random())
    # embed.set_footer(text = f"{footer}")
    # await interaction.channel.send(embed=embed)
    await interaction.response.send_modal(Questionnaire())
    # await interaction.response.send_message("done", ephemeral=True)
 
@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=1172581606687518750))
    print("Bot started")

client.run('BOT_TOKEN_HERE')
