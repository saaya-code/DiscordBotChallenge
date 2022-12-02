from dotenv import load_dotenv
from discord.ext import commands
import discord
import requests
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("=========================")
    print("Bot is ready")
    print(bot.user.id)
    print("=========================")

class SelectChangeOption(discord.ui.Select):
    def __init__(self):
        options = [
        discord.SelectOption(label="Changer la Coleur de l'arrière plan"),
        discord.SelectOption(label="Ajouter du Texte"),
        discord.SelectOption(label="Changer la Coleur du texte"),
        discord.SelectOption(label="Autre Options")
    ]
        super().__init__(placeholder="Choisir une option", max_values=1, min_values=1, options=options)

    async def callback(self, interaction : discord.Interaction):
        if self.values[0] == "Changer la Coleur de l'arrière plan":
            await interaction.response.send_modal(TextInputBackgroundColor())
        elif self.values[0] == "Ajouter du Texte":
            await interaction.response.send_modal(TextInputTextElement())
        else:
            await interaction.response.send_modal(TextInputTextColor())


class TextInputBackgroundColor(discord.ui.Modal, title= "Entrer une coleur"):
    answer = discord.ui.TextInput(label="La coleur peut etre (Hex or explicite):", placeholder="Ex: #FFFFFF | red")

    async def on_submit(self, interaction: discord.Interaction):
        data = {
            "background-color": self.answer.value.lower() 
        }
        response = requests.post("http://localhost:3000/" ,json=data)
        if response.status_code == 200:
            await interaction.response.send_message("La coleur a ete changé tu dois actualise la page")
        else:
            await interaction.response.send_message("La coleur que tu as ecrit est inconnu")


class TextInputTextColor(discord.ui.Modal, title= "Entrer une coleur"):
    answer = discord.ui.TextInput(label="La coleur peut etre (Hex or explicite):", placeholder="Ex: #FFFFFF | red")

    async def on_submit(self, interaction: discord.Interaction):
        data = {
            "TextColor": self.answer.value.lower() 
        }
        response = requests.post("http://localhost:3000/" ,json=data)
        if response.status_code == 200:
            await interaction.response.send_message("La coleur a ete changé tu dois actualise la page")
        else:
            await interaction.response.send_message("La coleur que tu as ecrit est inconnu")

class TextInputTextElement(discord.ui.Modal, title= "Entrer un texte"):
    answer = discord.ui.TextInput(label="Le texte à ajouter:", placeholder="Salut monde!")

    async def on_submit(self, interaction: discord.Interaction):
        data = {
            "addText": self.answer.value.lower() 
        }
        response = requests.post("http://localhost:3000/" ,json=data)
        if response.status_code == 200:
            await interaction.response.send_message("La coleur a ete changé tu dois actualise la page")
        else:
            await interaction.response.send_message("La coleur que tu as ecrit est inconnu")

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(SelectChangeOption())


@bot.command()
async def changer(ctx):
    await ctx.send("Que tu veux ajouter/changer dans le site web?", view=SelectView())

bot.run(TOKEN)

