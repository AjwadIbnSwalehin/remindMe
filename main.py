import discord, asyncio, datetime
from discord.ext import commands

# Setting the Bot prefix to "!"
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all()) 


# Converting hours and minutes to seconds
def time_conversion(hour, minute, second):
    time = (hour * 3600) + (minute * 60) + second
    return time


# Finding the time difference between now and set time
def find_time(hours, minutes):
    now = datetime.datetime.now()
    then = now + datetime.timedelta(days = 1)
    then = now.replace(hour = int(hours), minute = int(minutes))
    return now, then


@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game("Reminding since 2022!"))
    await bot.tree.sync(guild=None)
    print(f"We have logged in as Remind Me!")

# Remind function to remind after a given amount of time
@bot.command()
async def remind(ctx, message:str, hour:int, minute: int, second:int):
    wait = time_conversion(hour, minute, second)
    await asyncio.sleep(wait)

    remindembed = discord.Embed(
        colour = discord.Colour.yellow()
    )
    remindembed.set_author(name = "Reminder:", icon_url = "https://i.pinimg.com/originals/5e/a2/fc/5ea2fc59e9d958e0eac64909f38eabc4.jpg")
    remindembed.add_field(name = f"Reminder from {wait} seconds ago:", value = f"{message}")
    
    await ctx.send(ctx.author.mention, embed = remindembed)


# Remind function to remind after a given time
@bot.command()
async def timeremind(ctx, hours, minutes, daily_reminder):
    now, then = find_time(hours, minutes) 
    wait_time = (then-now).total_seconds()
    await asyncio.sleep(wait_time)

    remindembed = discord.Embed(
        colour = discord.Colour.yellow()
    )
    remindembed.set_author(name = "Reminder:", icon_url = "https://i.pinimg.com/originals/5e/a2/fc/5ea2fc59e9d958e0eac64909f38eabc4.jpg")
    remindembed.add_field(name = f"Reminder from {wait_time} seconds ago", value = f"{daily_reminder}")

    await ctx.send(ctx.author.mention, embed = remindembed)

# Sets the bot token (Not showing because it allows people to have access to the bot)
bot.run("Bot Token")
