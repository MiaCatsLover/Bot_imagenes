import discord
from discord.ext import commands
import os, random
import requests
intents = discord.Intents.default()
intents.message_content = True
print(os.listdir('5 clase\imagenes'))
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'Ha iniciado sesión como {bot.user}')
def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

def happy_dog_url():
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']

#PATO
@bot.command('duck')
async def duck(ctx):
    '''Cada vez que se llama a la solicitud de pato, el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

#MEMES
@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('5 clase\imagenes'))
    with open(f'5 clase\imagenes/{img_name}', 'rb') as f:
        picture = discord.File(f)
 
    await ctx.send(file=picture)

#PERROS
@bot.command('happy_dog')
async def happy_dog(ctx):
    '''Cada vez que se llama a la solicitud de dog, el programa llama a la función happy_dog_url'''
    image_url = happy_dog_url()
    await ctx.send(image_url)

#GATOS

@bot.command()
async def kiss(ctx):
    img_name = random.choice(os.listdir('5 clase/imagenes/kiss cat'))
    with open(f'5 clase/imagenes/kiss cat/{img_name}', 'rb') as f:
        picture = discord.File(f)
    mensaje = random.randint(0, 2)
    if mensaje == 1:
        await ctx.send("miau miau 😺 (con gusto!) ^^💕")
    if mensaje == 2:
        await ctx.send("miau😽 (alguien quiere un beso? :3) ❤️")
    else:
        await ctx.send("miau!!😽😽 (un gran beso para ti!) 🐈 ")
    await ctx.send(file=picture)

@bot.command()
async def dance(ctx):
    img_name = random.choice(os.listdir('5 clase/imagenes/dancing cat'))
    with open(f'5 clase/imagenes/dancing cat/{img_name}', 'rb') as f:
        picture = discord.File(f)
        mensaje = random.randint(0, 2)
    if mensaje == 1:
        await ctx.send("miau miau!! 😼🎶 (que buen ritmo!!) 🎶📻")
    if mensaje == 2:
        await ctx.send("miau😸!! (subanle volumen a la musica!!!) 🎶🎶")
    else:
        await ctx.send("miau miau miau😼😼! (mostrare mis mejores pasos de baile!) 🐈🎶 ")
    await ctx.send(file=picture)

@bot.command()
async def angry(ctx):
    img_name = random.choice(os.listdir('5 clase/imagenes/angry cat'))
    with open(f'5 clase/imagenes/angry cat/{img_name}', 'rb') as f:
        picture = discord.File(f)
    mensaje = random.randint(0, 2)
    if mensaje == 1:
        await ctx.send("MIAUU! 😾😾 (>:(!)")
    if mensaje == 2:
        await ctx.send("miau...😾 (ugh..=.=)")
    else:
        await ctx.send("miau. (no quiero hablar ahora.(¬_¬ ) )")
    await ctx.send(file=picture)

