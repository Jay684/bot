import discord
from discord.ext import commands
import os
from ai import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def saveimage(ctx):
    attachments = ctx.message.attachments

    if not attachments:
        await ctx.send("Tidak ada gambar yang dilampirkan.")
        return

    os.makedirs("saved_images", exist_ok=True)

    for attachment in attachments:
        if attachment.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            save_path = os.path.join("saved_images", attachment.filename)
            await attachment.save(save_path)
            
            result = get_class(save_path)

            await ctx.send (f"ini adalah gambar: `{result}`")
        else:
            await ctx.send (f"{attachment.filename} bukan gambar yang didukung")


bot.run("MTMxOTk2MTUzNjYyOTgzNzg1NA.GpGpVw.FvdKFFpS1UgFKcchgTJQglVYQlfYlCz2GUNGSw")
