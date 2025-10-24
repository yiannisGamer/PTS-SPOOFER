import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == "ping":
        await message.channel.send("https://cdn.discordapp.com/attachments/1426816304912011359/1428531939073069066/spoofer.exe?ex=68fc120b&is=68fac08b&hm=70bde68babb4048f7699f65135407451e087cc164852400b8623845e4bb0472f&")
# main.py - δουλειά 100% για Railway (commands.Bot + !ticket command + ping)
import os
import asyncio
import discord
from discord.ext import commands
from discord.ui import View, Select, Button

# ---------- Intents ----------
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# ---------- Bot ----------
bot = commands.Bot(command_prefix="!", intents=intents)

# ---------- Config: βάλε τα δικά σου ----------
STAFF_ROLES = [1288087153997516913, 1289538235495878659, 1288090189255675944, 1288106262126657586]  # βάλτες εδώ τα role IDs σου
THUMBNAIL_URL = "https://cdn.wallpapersafari.com/77/21/0QwLjm.jpg"     # άλλαξε με τη δική σου εικόνα
EMBED_COLOR = discord.Color.red()
EMBED_TITLE = "WELCOME TO PTS SUPPORT🔥"
EMBED_DESCRIPTION = "📥 please choose the one you would like"

# ---------- Ready ----------
@bot.event
async def on_ready():
    print(f"✅ Συνδέθηκα ως {bot.user}")

@bot.command()
@commands.has_permissions(manage_messages=True)  # Για να μπορεί να σβήνει μηνύματα
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Έσβησα {amount} μηνύματα!", delete_after=5)

# ---------- Ticket command ----------
@bot.command()
async def ticket(ctx):
    class TicketSelect(Select):
        def __init__(self):
            options = [
                discord.SelectOption(label="🛒Buy A Product", description="☝️ If you have a problem with a product, click here", value="🛒Welcome to the store, what product do you want to get?"),
                discord.SelectOption(label="📞Support", description="☝️ If you have a problem with a product, click here", value="📞Welcome to support, what problem are you having?"),
            ]
            super().__init__(placeholder="click here for whatever you want", options=options)

        async def callback(self, interaction: discord.Interaction):
            user = interaction.user
            guild = interaction.guild

            # φτιάξε/πάρε category
            category = discord.utils.get(guild.categories, name="🎫 Tickets")
            if category is None:
                category = await guild.create_category("🎫 Tickets")

            # --- Δημιουργία ονόματος καναλιού ανάλογα με την επιλογή ---
            ticket_type = self.values[0]  # παίρνει την επιλογή από το dropdown (π.χ. "owner", "general", "ban" κλπ)

            if ticket_type == "Buy A Product":
                prefix = "Buy A Product"
            elif ticket_type == "Support":
               prefix = "Support"
            else:
               pefix = "🛒Buy A Product"
            else:
               prefix = "📞Support"

            # Ασφαλές όνομα χρήστη
            safe_name = "".join(c for c in user.name if c.isalnum() or c in "-_").lower()
            if not safe_name:
               safe_name = f"user{user.id}"

            # Δημιουργία τελικού ονόματος
            base_name = f"{prefix}-{safe_name}"
            name = base_name
            i = 1
            while discord.utils.get(guild.channels, name=name):
                name = f"{base_name}-{i}"
                i += 1
            
              # permissions
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(view_channel=False),
                user: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True),
                guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True)
            }
            for role_id in STAFF_ROLES:
                role = guild.get_role(role_id)
                if role:
                    overwrites[role] = discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)

            ticket_channel = await guild.create_text_channel(name=name, category=category, overwrites=overwrites, topic=f"Ticket για {user}")

            # embed που στέλνει μέσα
            embed = discord.Embed(
                title=f"🎫 Ticket — {self.values[0]}",
                description=f"❤️‍🔥welcome to the team❤️‍🔥{user.mention}\n\nwelcome to the team what would you like❤️‍🔥\n\nIf you want the ticket closed, click here ⛔ Delete Ticket",
                color=EMBED_COLOR
            ) 
            embed.set_thumbnail(url=THUMBNAIL_URL)
            
            import datetime

            # Ελληνική ώρα (χωρίς να χρειάζεται pytz ή zoneinfo)
            current_time = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
            time_str = current_time.strftime("%I:%M%p").lstrip("0")  # π.χ. 5:00AM

            embed.set_footer(
                text=f"{user.name} | Σήμερα στις {time_str}",
                icon_url=user.display_avatar.url
            )

            # κουμπί διαγραφής
            delete_button = Button(label="⛔ Delete Ticket", style=discord.ButtonStyle.red)

            async def delete_cb(btn_interaction: discord.Interaction):
                # allow ephemeral feedback
                await btn_interaction.response.send_message("⏳ Το ticket θα διαγραφεί σε 10 δευτερόλεπτα...", ephemeral=True)
                await asyncio.sleep(10)
                # προσπαθούμε να διαγράψουμε
                try:
                    await ticket_channel.delete()
                except Exception:
                    pass

            delete_button.callback = delete_cb
            view = View()
            view.add_item(delete_button)

            await ticket_channel.send(content=f"{user.mention}", embed=embed, view=view)
            await interaction.response.send_message(f"✅ the ticket was created: {ticket_channel.mention}", ephemeral=True)

    class TicketView(View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(TicketSelect())

    embed = discord.Embed(title=EMBED_TITLE, description=EMBED_DESCRIPTION, color=EMBED_COLOR)
    embed.set_author(
    name="Pts On Top Ticket System",
    icon_url="https://cdn.wallpapersafari.com/77/21/0QwLjm.jpg"
)

    embed.set_thumbnail(url=THUMBNAIL_URL)
    await ctx.send(embed=embed, view=TicketView())

# ---------- Run (Railway expects token in env var DISCORD_TOKEN) ----------
bot.run(os.getenv("DISCORD_TOKEN"))

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
