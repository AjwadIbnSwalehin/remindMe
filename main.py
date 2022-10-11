import discord, asyncio, datetime
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

def time_conversion(hour, minute, second):
    time = (hour * 3600) + (minute * 60) + second
    return time

def find_time(hours, minutes):
    now = datetime.datetime.now()
    then = now + datetime.timedelta(days = 1)
    then = now.replace(hour = int(hours), minute = int(minutes))
    return now, then

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game("Reminding since 2022!"))
    print(f"We have logged in as Remind Me!")

@bot.command()
async def sync(ctx):
    await ctx.send(f"Syncing...")
    await bot.tree.sync()
    await bot.tree.sync(guild = discord.Object(id=000000000000000000000000))
    await ctx.send(f"Syncing Complete!")

@bot.command()
async def remind(ctx, message:str, hour:int, minute: int, second:int):
    wait = time_conversion(hour, minute, second)
    await asyncio.sleep(wait)
    await ctx.send(f"{ctx.author.mention}, Reminder: {message}")

@bot.command()
async def embed(ctx, member:discord.Member = None):
    if member == None:
        member = ctx.author

    name = member.display_name
    pfp = member.display_avatar

    embed = discord.Embed(title = "Remind Me!", description="Commands:", colour = discord.Colour.random())
    embed.set_author(name = f"{name}", icon_url = "https://i.pinimg.com/originals/5e/a2/fc/5ea2fc59e9d958e0eac64909f38eabc4.jpg")
    embed.set_thumbnail(url=f"{pfp}")
    embed.add_field(name = "!remind", value = "Sets a reminder")
    embed.set_footer(text=f"{name} Made this Embed")

    await ctx.send(embed = embed)

@bot.command()
async def timeremind(ctx, hours, minutes, daily_reminder):
    now, then = find_time(hours, minutes) 
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)
    await ctx.send(daily_reminder)

bot.run("Bot Token")
