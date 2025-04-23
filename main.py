import discord
from discord.ext import commands
import os # Para manejar archivos y directorios
import random # Para generar números aleatorios

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

@bot.command()
async def sumar(ctx, num1: str, num2: str):
    try:
        # Convertimos los argumentos a enteros
        num1 = int(num1)
        num2 = int(num2)
        
        # Realizamos la suma
        resultado = num1 + num2
        await ctx.send(f'La suma de {num1} y {num2} es: {resultado}')
    except ValueError:
        # Si no se pueden convertir a enteros, enviamos un mensaje de error
        await ctx.send('Por favor, asegúrate de ingresar números válidos.')

@bot.command()
async def mem1(ctx):
    with open('imagenes/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def mem2(ctx):
    with open('imagenes/mem2.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def mem3(ctx):
    with open('imagenes/mem3.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def mem4(ctx):
    with open('imagenes/mem4.jpg', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def meme_aleatorio(ctx):
    
    img_name = random.choice(os.listdir('imagenes'))
    
    with open(f'imagenes/{img_name}', 'rb') as file:
        
        picture = discord.File(file)
        
        await ctx.send(file=picture)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('perro')
async def perro(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_dog_image_url'''
    image_url = get_dog_image_url()
    await ctx.send(image_url)

#https://randomfox.ca/

def get_fox_image_url():    
    url = 'https://randomfox.ca/'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('zorro')
async def zorro(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_fox_image_url'''
    image_url = get_fox_image_url()
    await ctx.send(image_url)




token = ""

bot.run(token)


