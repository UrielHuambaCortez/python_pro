import discord
from discord.ext import commands
import os 
import random 
import requests



intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Tú Bot {bot.user} esta en linea!')
@bot.command()
async def kodland(ctx):
    await ctx.send('\U0001F642')
@bot.command()
async def repetir(ctx,*, mensaje:str):
    await ctx.send(mensaje)

lista = [
    "Lima es una de las ciudades más contaminadas de América Latina en cuanto a calidad del aire. En varias zonas supera los límites recomendados por la OMS para partículas finas, que son dañinas para la salud respiratoria y cardiovascular.",
]

@bot.command()
async def dime(ctx,*, mensaje: str):
    
    mensaje = mensaje.lower().strip()

    if "preocupante" in mensaje:
        await ctx.send(lista[0])

    else:
        await ctx.send('No entiendo tu pregunta, pero la contaminación en Lima es un problema serio!')

lista_extraño = [
    "Más del 70% de la contaminación del aire en Lima proviene del transporte, especialmente de vehículos antiguos que usan diésel de baja calidad. El parque automotor informal y poco regulado agrava el problema.",
    "Lima tiene un clima árido y muy pocas precipitaciones, lo que impide que las partículas contaminantes sean limpiadas del aire. Además, su geografía con cerros que rodean la ciudad dificulta la dispersión de contaminantes.",
    "Algunas zonas de Lima enfrentan problemas de contaminación del agua por vertidos industriales y aguas residuales sin tratar, especialmente en ríos como el Rímac.",
    "Lima genera más de 8,000 toneladas de residuos sólidos al día, pero una gran parte no es adecuadamente tratada. Muchos residuos terminan en botaderos informales o contaminan ríos y suelos.",
    "La contaminación del aire en Lima está asociada con miles de muertes prematuras al año. También se relaciona con un aumento de enfermedades respiratorias, especialmente en niños y adultos mayores.",
]

@bot.command()
async def cuentame(ctx,*, mensaje: str):
    
    mensaje = mensaje.lower().strip()
    if "extraño" in mensaje:
        respuesta = random.choice(lista_extraño)
        await ctx.send(respuesta)

token = ""

bot.run(token)
