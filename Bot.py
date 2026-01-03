import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import random

# --- WEB SERVER (UptimeRobot üçün) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive 😎"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

keep_alive()
# --------------------------------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- Auto-reply messages ---
greetings = ["Aleykum salam 😎", "Salam hacker 👋", "Sistem səni tanıdı 🕶️", "Hey! Nasılsan? 😏"]

# --- Users who already got a reply (anti-spam) ---
replied_users = set()

@bot.event
async def on_ready():
    print("🟢 BOT ONLINE:", bot.user)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()
    user_id = message.author.id

    # Auto-reply sistemi
    if content in ["sa", "salam", "hey"]:
        if user_id not in replied_users:
            reply = random.choice(greetings)
            await message.channel.send(reply)
            replied_users.add(user_id)
            print(f"[SYSTEM] Greeting detected from {message.author} | Response: {reply}")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("😏 Sistem aktivdir.")

# ← BURADA TOKENİ DAXİL ET
bot.run("BURAYA_TOKENINI_YAPISDIR")import discord
from discord.ext import commands
from flask import Flask
from threading import Thread
import random

# --- WEB SERVER (UptimeRobot üçün) ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive 😎"

def run_web():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_web)
    t.start()

keep_alive()
# --------------------------------------

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# --- Auto-reply messages ---
greetings = ["Aleykum salam 😎", "Salam hacker 👋", "Sistem səni tanıdı 🕶️", "Hey! Nasılsan? 😏"]

# --- Users who already got a reply (anti-spam) ---
replied_users = set()

@bot.event
async def on_ready():
    print("🟢 BOT ONLINE:", bot.user)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    content = message.content.lower()
    user_id = message.author.id

    # Auto-reply sistemi
    if content in ["sa", "salam", "hey"]:
        if user_id not in replied_users:
            reply = random.choice(greetings)
            await message.channel.send(reply)
            replied_users.add(user_id)
            print(f"[SYSTEM] Greeting detected from {message.author} | Response: {reply}")

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send("😏 Sistem aktivdir.")

# ← BURADA TOKENİ DAXİL ET
bot.run("MTQ1NzA1MDY2MDc1NDQyMzkxOQ.GWZs8q.d5207e_qlEjAGi-Jkkc8WL11LzWTeJAWQt4uRY")
