import discord
from discord.ext import commands


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

@bot.command()
async def saludo(ctx,*, mensaje: str):
    
    mensaje = mensaje.lower().strip()
    if "hola" in mensaje:
        await ctx.send('Hola como estas?')

    elif "causa" in mensaje:
        await ctx.send('Adios, que tengas un buen dia!')

    else:
        await ctx.send('No entiendo tu saludo, pero hola!')

@bot.command()
async def pregunta(ctx,*, mensaje: str):
    
    mensaje = mensaje.lower().strip()
    if "quien te creo" in mensaje:
        await ctx.send('mi creador es Uriel, alias Dreams!')

    elif "¿quien te creo?" in mensaje:
        await ctx.send('mi creador es Uriel, alias Dreams!')

    else:
        await ctx.send('No entiendo tu pregunta, pero soy un bot creado por Uriel!')

@bot.command()
async def despedida(ctx,*, mensaje: str):
    
    mensaje = mensaje.lower().strip()
    if "chao" in mensaje:
        await ctx.send('cuidate mucho!, nos vemos en la proxima!')

    elif "adios" in mensaje:
        await ctx.send('cuidate mucho!, nos vemos en la proxima!')

    elif "bye" in mensaje:
        await ctx.send('cuidate mucho!, nos vemos en la proxima!')

    elif "cuidate" in mensaje:
        await ctx.send('cuidate mucho!, nos vemos en la proxima!')

    else:
        await ctx.send('No entiendo tu pregunta, pero cuidate mucho!')

@bot.command()
async def funcion(ctx,*, mensaje: str):
    
    mensaje = mensaje.lower().strip()
    if "que puedes hacer" in mensaje:
        await ctx.send('Soy un bot creado por Uriel, puedo ayudarte a responder preguntas y hacer algunas cosas divertidas!')

    elif "que haces" in mensaje:
        await ctx.send('Soy un bot creado por Uriel, puedo ayudarte a responder preguntas y hacer algunas cosas divertidas!')

    elif "cual es tu funcion" in mensaje:
        await ctx.send('mi función es ayudarte a responder preguntas y hacer algunas cosas divertidas!')

    elif "como me puedes ayudar" in mensaje:
        await ctx.send('te puedo ayudar a responder preguntas y hacer algunas cosas divertidas!')

    else:
        await ctx.send('No entiendo tu pregunta, pero espero ayudarte en algo más!')



token = ""

bot.run(token)


