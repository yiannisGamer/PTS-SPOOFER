import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
# main.py - δουλειά 100% για Railway (commands.Bot + !ticket command + ping)
import os
import asyncio
import discord
from discord.ext import commands
from discord.ui import View, Select, Button
import datetime

# ---------- Intents ----------
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

# ---------- Bot ----------
bot = commands.Bot(command_prefix="!", intents=intents)

# ---------- Config: βάλε τα δικά σου ----------
STAFF_ROLES = [1288087153997516913, 1289538235495878659, 1288090189255675944, 1288106262126657586]  # βάλτες εδώ τα role IDs σου
THUMBNAIL_URL = "https://media.discordapp.net/attachments/1432624239093092384/1433589942025715855/a_649a20666f8b2fc068485749f726efc6.webp?ex=69053e2c&is=6903ecac&hm=2ae0c7846b316afea4984854dab0cc43acf985b29e4c1e22fbdfa0e2690d75c9&=&animated=true"     # άλλαξε με τη δική σου εικόνα
EMBED_COLOR = discord.Color.red()
EMBED_TITLE = "**WELCOME TO PTS SUPPORT**🔥"
EMBED_DESCRIPTION = "📥 **please choose the one you would like**"

# ---------- Ready ----------
@bot.event
async def on_ready():
    print(f"✅ Συνδέθηκα ως {bot.user}")
 
    # Παίρνει το κείμενο από Railway env var
    activity_text = os.getenv("BOT_ACTIVITY_TEXT", "Pts On Top")
    
    # Ορίζει την παρουσία του bot (το "Παίζει ...")
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Game(name=activity_text)
    )
    
    print(f"🎮 Activity set: {activity_text}")

@bot.command()
async def sarck(ctx):
    embed = discord.Embed(
        title="💀 VOODOO ROLEPLAY 💀",  # Τίτλος
        description=(
            "👋 Καλωσήρθες στο **Voodoo Roleplay!** 💜\n\n"
            "🔥 Απόλαυσε το RP με φίλους!\n"
            "💬 Μπες στο voice, γνώρισε κόσμο και πέρασε καλά!\n\n"
            "⚡ **Server info:**\n"
            "• Custom cars 🚗\n"
            "• Jobs 💼\n"
            "• Realistic RP 🎭"
        ),
        color=discord.Color.red()
    )

    # 🔹 Εικόνα δεξιά (μικρή φωτογραφία)
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/tRN56-OkGTbhSk8nmgMEdk8ahLNo1Zkb2db3fFwczmg/https/cdn.wallpapersafari.com/77/21/0QwLjm.jpg?format=webp&width=1382&height=864")

    # 🔹 Εικόνα μεγάλη κάτω (αν θες)
    embed.set_image(url="https://media.discordapp.net/attachments/1288996430383677450/1289343395025784863/Screenshot_20240928_004928_Chrome.jpg?ex=69028c1c&is=69013a9c&hm=cf2ef2b31140a8ee32f572c2ed48f1eec99c429e45ae030a3ef02a124a98fea8&=&format=webp&width=1523&height=864")  # μπορεί να είναι και GIF
    
    await ctx.send(embed=embed)
    
@bot.command()
async def apply(ctx):
    # 🔹 Δημιουργία embed
    embed = discord.Embed(
        title="💀 VOODOO ROLEPLAY 💀",
        description=(
            "👋 Καλωσήρθες στο **Voodoo Roleplay!** 💜\n\n"
            "Παρακάτω μπορείς να επιλέξεις και να κάνεις αίτηση για το σώμα που θέλεις:\n"
            "🚔 **Police** – Υπερασπίσου τη δικαιοσύνη\n"
            "🚑 **Ambulance** – Βοήθησε όσους έχουν ανάγκη\n"
            "💼 **Lawyer** – Πάλεψε για το δίκιο\n"
            "💣 **Army** – Προστάτευσε την πόλη\n"
            "🛠️ **Anticheat** – Κράτα το RP καθαρό\n"
            "💜 **Staff** – Γίνε μέρος της ομάδας μας!"
        ),
        color=discord.Color.purple()
    )

    # 🔹 Μικρή εικόνα πάνω αριστερά (λογότυπο)
    embed.set_author(
        name="Pts On Top",
        icon_url="https://images-ext-1.discordapp.net/external/tRN56-OkGTbhSk8nmgMEdk8ahLNo1Zkb2db3fFwczmg/https/cdn.wallpapersafari.com/77/21/0QwLjm.jpg?format=webp&width=1382&height=864"  # 🔸 Βάλε εδώ το link του λογοτύπου σου
    )

    # 🔹 Μεγάλη εικόνα κάτω (banner ή GIF)
    embed.set_image(url="https://media.discordapp.net/attachments/1431936689408053268/1433311007274438728/kkk.gif?ex=69043a65&is=6902e8e5&hm=4883c1d5ca4e78bdb7f54b5f4e4bcbbf7bf658e6f84f441be8459602ddd37339&=")

    # 🔹 Κουμπιά (links)
    view = discord.ui.View()
    view.add_item(discord.ui.Button(label="Mod", emoji="✅", url="https://youtu.be/TlapVJofCL4?si=Y9PK-lpPPEMxEOz4"))

    # 🔹 Στέλνει το embed με τα κουμπιά
    await ctx.send(embed=embed, view=view)
    
@commands.has_permissions(manage_messages=True)  # Για να μπορεί να σβήνει μηνύματα
async def clear(ctx, amount: int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Έσβησα {amount} μηνύματα!", delete_after=5)
    
@bot.command()
async def ping(ctx):
    await ctx.send("hh")

@bot.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, target: str, *, reason: str = None):
    # διαγραφή της εντολής αμέσως
    try:
        await ctx.message.delete()
    except:
        pass

    member = None

    # 1) Αν χρησιμοποιήθηκε mention -> ctx.message.mentions[0]
    if ctx.message.mentions:
        member = ctx.message.mentions[0]

    # 2) Αν όχι mention, δοκιμάζουμε αν είναι ID (μόνο digits)
    if not member:
        maybe_id = ''.join(ch for ch in target if ch.isdigit())
        if maybe_id:
            try:
                member = await ctx.guild.fetch_member(int(maybe_id))
            except:
                member = None

    # 3) Αν ακόμα όχι, δοκιμάζουμε ακριβές όνομα ή nickname
    if not member:
        # πρώτα ακριβές match name ή display_name
        for m in ctx.guild.members:
            if m.name == target or m.display_name == target or f"{m.name}#{m.discriminator}" == target:
                member = m
                break

    # 4) Αν δεν βρέθηκε, δοκιμάζουμε partial (case-insensitive)
    if not member:
        target_lower = target.lower()
        for m in ctx.guild.members:
            if target_lower in m.name.lower() or target_lower in m.display_name.lower():
                member = m
                break

    # Τελικός έλεγχος
    if not member:
        # δεν βρέθηκε στόχος -> δεν κάνουμε τίποτα (ή στείλε ephemeral reply αν θέλεις)
        return

    # Προστασία: μην κάνει ban τον εαυτό του ή το bot
    if member.id == ctx.author.id or member.id == bot.user.id:
        return

    # Εκτέλεση ban
    try:
        await member.ban(reason=reason or f"Banned by {ctx.author}")
    except:
        return

    # προσωρινή επιβεβαίωση και διαγραφή μετά 3s
    confirmation = await ctx.send(f'Από {ctx.author} ο χρήστης {member} έφαγε ban.')
    await asyncio.sleep(3)
    try:
        await confirmation.delete()
    except:
        pass

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        try:
            await ctx.message.delete()
        except:
            pass
        return

@bot.command(name='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, target: str):
    try:
        await ctx.message.delete()
    except:
        pass

    # Δημιουργούμε λίστα banned χρηστών
    banned_entries = [entry async for entry in ctx.guild.bans()]
    member_user = None

    # Προσπαθούμε με ID
    maybe_id = ''.join(ch for ch in target if ch.isdigit())
    if maybe_id:
        for entry in banned_entries:
            if str(entry.user.id) == maybe_id:
                member_user = entry.user
                break

    # Αν όχι, ψάχνουμε username#discriminator
    if not member_user:
        for entry in banned_entries:
            user = entry.user
            if f"{user.name}#{user.discriminator}" == target:
                member_user = user
                break

    # Προαιρετικά: partial match στο username
    if not member_user:
        target_lower = target.lower()
        for entry in banned_entries:
            user = entry.user
            if target_lower in user.name.lower():
                member_user = user
                break

    if not member_user:
        await ctx.send("Δεν βρέθηκε banned χρήστης με αυτά τα στοιχεία.", delete_after=5)
        return

    # Εκτέλεση unban
    await ctx.guild.unban(member_user)

    confirmation = await ctx.send(f'Ο χρήστης {member_user} έγινε unban από {ctx.author}.')
    await asyncio.sleep(3)
    try:
        await confirmation.delete()
    except:
        pass

@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("❌ Πρέπει να αναφέρεις ποιον θέλεις να κάνεις kick!", delete_after=5)
        return

    # Διαγραφή μηνύματος εντολής
    await ctx.message.delete()

    try:
        # Προσπάθεια αποστολής DM ΠΡΙΝ το kick
        try:
            await member.send(f"❌You were kicked by {ctx.author.name} from the server **{ctx.guild.name}**.\n⚠️**If you do it again, the next one will be a ban!!**")
        except:
            pass  # Αν δεν μπορεί να στείλει DM, απλά συνεχίζει

        # Κάνει kick τον χρήστη
        await member.kick(reason="Kick από moderator")

        # Μήνυμα επιβεβαίωσης στο κανάλι
        msg = await ctx.send(f" Ο {member.mention} έγινε kick από τον server.", delete_after=3)

    except discord.Forbidden:
        await ctx.send("❌ Δεν έχω δικαίωμα να κάνω kick αυτόν τον χρήστη.", delete_after=5)
    except Exception as e:
        await ctx.send(f"⚠️ Παρουσιάστηκε σφάλμα: {e}", delete_after=5)

@bot.command()
@commands.has_permissions(moderate_members=True)
async def timeout(ctx, member: discord.Member = None):
    if member is None:
        await ctx.send("❌ Πρέπει να αναφέρεις ποιον θέλεις να κάνεις timeout!", delete_after=5)
        return

    # Χρόνος timeout: 5 λεπτά
    duration = datetime.timedelta(minutes=5)

    try:
        # Προσπάθεια αποστολής DM
        try:
            await member.send("🚫**You have been put in a 5-minute timeout. Don't do it again!**")
        except:
            pass  # Αν δεν μπορεί να στείλει DM, απλώς προχωράμε

        # Εφαρμόζουμε timeout
        await member.timeout(duration, reason="Timeout από moderator")

        # Διαγράφουμε το μήνυμα εντολής
        await ctx.message.delete()

        # Μήνυμα επιβεβαίωσης στο κανάλι
        msg = await ctx.send(f" Ο {member.mention} μπήκε σε timeout για 5 λεπτά.", delete_after=3)

    except discord.Forbidden:
        await ctx.send("❌ Δεν έχω δικαιώματα να κάνω timeout αυτόν τον χρήστη.", delete_after=5)
    except Exception as e:
        await ctx.send(f"⚠️ Παρουσιάστηκε σφάλμα: {e}", delete_after=5)
        
@bot.command()
@commands.has_permissions(manage_roles=True)
async def add(ctx, user_input, *, role_input):
    # 🔹 Προσπάθησε να βρει τον χρήστη είτε από mention είτε από ID
    try:
        if user_input.isdigit():
            member = await ctx.guild.fetch_member(int(user_input))
        else:
            member = await commands.MemberConverter().convert(ctx, user_input)
    except:
        msg = await ctx.send("❌ Δεν βρήκα αυτόν τον χρήστη.")
        await msg.delete(delay=5)
        await ctx.message.delete(delay=1)
        return

    # 🔹 Προσπάθησε να βρει τον ρόλο είτε από ID είτε από όνομα
    role = None
    if role_input.isdigit():
        role = ctx.guild.get_role(int(role_input))
    else:
        role = discord.utils.find(lambda r: r.name.lower() == role_input.lower(), ctx.guild.roles)

    if role is None:
        msg = await ctx.send("❌ Δεν βρήκα ρόλο με αυτό το όνομα ή ID.")
        await msg.delete(delay=5)
        await ctx.message.delete(delay=1)
        return

    # 🔹 Δίνει τον ρόλο
    await member.add_roles(role)

    # 🔹 Στέλνει επιβεβαίωση
    confirm_msg = await ctx.send(f"✅ Ο ρόλος **{role.name}** δόθηκε στον {member.mention}!")

    # 🔹 Διαγράφει την εντολή και το μήνυμα
    await ctx.message.delete(delay=1)
    await confirm_msg.delete(delay=5)
    
@bot.command()
@commands.has_permissions(manage_roles=True)
async def remove(ctx, user_input, *, role_input):
    # 🔹 Προσπάθησε να βρει τον χρήστη είτε από mention είτε από ID
    try:
        if user_input.isdigit():
            member = await ctx.guild.fetch_member(int(user_input))
        else:
            member = await commands.MemberConverter().convert(ctx, user_input)
    except:
        msg = await ctx.send("❌ Δεν βρήκα αυτόν τον χρήστη.")
        await msg.delete(delay=5)
        await ctx.message.delete(delay=1)
        return

    # 🔹 Προσπάθησε να βρει τον ρόλο είτε από ID είτε από όνομα
    role = None
    if role_input.isdigit():
        role = ctx.guild.get_role(int(role_input))
    else:
        role = discord.utils.find(lambda r: r.name.lower() == role_input.lower(), ctx.guild.roles)

    if role is None:
        msg = await ctx.send("❌ Δεν βρήκα ρόλο με αυτό το όνομα ή ID.")
        await msg.delete(delay=5)
        await ctx.message.delete(delay=1)
        return

    # 🔹 Αφαιρεί τον ρόλο
    await member.remove_roles(role)

    # 🔹 Επιβεβαίωση
    confirm_msg = await ctx.send(f"✅ Ο ρόλος **{role.name}** αφαιρέθηκε από τον {member.mention}!")

    # 🔹 Διαγράφει την εντολή και το μήνυμα
    await ctx.message.delete(delay=1)
    await confirm_msg.delete(delay=5)

import random

# Λίστα με 47 “αστεία memes” – εικόνα + λεζάντα
fun_memes = [
    {"url": "https://i.imgflip.com/1bij.jpg", "caption": "Όταν προσπαθείς να φας υγιεινά αλλά βλέπεις πίτσα 🍕"},
    {"url": "https://i.imgflip.com/26am.jpg", "caption": "Μέρα Δευτέρα... όλοι καταλαβαίνουμε 😅"},
    {"url": "https://i.imgflip.com/1otk96.jpg", "caption": "Όταν λες ‘μία μικρή ανάπαυση’ και κοιμάσαι 3 ώρες 😴"},
    {"url": "https://i.imgflip.com/4t0m5.jpg", "caption": "Όταν η καφεΐνη δεν δουλεύει πια ☕😵"},
    {"url": "https://i.imgflip.com/39t1o.jpg", "caption": "Μαθαίνω κώδικα: Τι σφάλμα είναι αυτό;;; 🤯"},
    {"url": "https://i.imgflip.com/1h7in3.jpg", "caption": "Όταν λες ‘θα το κάνω αύριο’ και το κάνεις μήνες μετά ⏳"},
    {"url": "https://i.imgflip.com/2fm6x.jpg", "caption": "Όταν η ομάδα σου ζητάει κάτι last minute 😤"},
    {"url": "https://i.imgflip.com/3si4.jpg", "caption": "Όταν βρίσκεις επιτέλους το bug που ψάχνεις 🐛✅"},
    {"url": "https://i.imgflip.com/1g8my4.jpg","caption": "Προσπαθώ να καταλάβω τους μαθηματικούς τύπους 🤓"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Δεν είμαι τεμπέλης… είμαι σε power saving mode 😎"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Μέσα μου ξέρω ότι θα φάω όλο το παγωτό 🍦😈"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Σκέφτομαι σοβαρά να γίνω νίντζα και να εξαφανιστώ από το σπίτι"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Προσοχή: Είμαι σοβαρά αστείος, εγώ προειδοποιώ!"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Σήμερα είμαι 100% καφές, 0% άνθρωπος ☕️😵"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Είμαι σε δίαιτα… από αύριο 😅"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Το μόνο τρέξιμο που κάνω είναι προς το ψυγείο 🏃‍♂️🍕"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Μαμά, είπαμε 'θα κοιμηθώ νωρίς'… ψέματα! 😴"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Το wifi έπεσε… η ζωή μου τελείωσε 📶😭"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Μου αρέσει να σκέφτομαι ότι είμαι ενήλικας… αλλά όχι πολύ σοβαρά 😎"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Ο σκύλος μου έχει πιο πολλά followers από μένα 🐶📸"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Καφέ + σοκολάτα = η μόνη λογική μου 💖"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Γυμναστήριο; Σκέφτομαι να πάω… νοερά 🏋️‍♂️😅"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Ο ήλιος με βλέπει και λέει 'καλή τύχη σήμερα' ☀️😂"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Μου αρέσει να μιλάω μόνος μου… οι καλύτερες συζητήσεις γίνονται έτσι 😎"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Σοκολάτα: 1 – Σήμερα: 0 🍫😈"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Οι μαγικές λέξεις: pizza, σοκολάτα, Netflix 🍕🍫📺"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Αγαπώ τον ύπνο… περισσότερο από τους ανθρώπους 😴❤️"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Ο καφές μου με κοιτάει σαν να ξέρει τα πάντα ☕️👀"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Αν ήμουν ήρωας, θα ήμουν 'Lazy Man' 😎🛋️"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Το πρόβλημα δεν είναι η δουλειά… είναι η έλλειψη σοκολάτας 🍫😅"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Δεν είμαι ακατάστατος, απλά δημιουργώ τέχνη χάους 🎨😂"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Ο ήλιος καίει, εγώ λιώνω 🌞🔥"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Γατάκια > Άνθρωποι 😼💖"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Αν ήμουν φαγητό, θα ήμουν παγωτό 🍦😎"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Το Netflix με καταλαβαίνει καλύτερα από όλους 📺❤️"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Προσοχή! Ακολουθεί επαγγελματίας αναβάτης… στον καναπέ 🛋️😂"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Δεν τεμπελιάζω, απλά απολαμβάνω την τεμπελιά μου 😎"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Το φαγητό μου με αγαπάει περισσότερο από όλους 🍕💖"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Η ζωή είναι μικρή, φάε την πίτσα 🍕😈"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Καφές: ο μόνος λόγος που ξυπνάω ☕️😵"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Είμαι σοβαρός… μόνο όταν κοιμάμαι 😴😂"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Μου αρέσει να σκέφτομαι ότι έχω σχέδιο… αλλά δεν έχω 😎"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Η σοκολάτα λύνει όλα τα προβλήματα 🍫😎"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Μην ανησυχείς, ο καφές είναι εδώ ☕️💖"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Οι κακές μέρες χρειάζονται καλή σοκολάτα 🍫😌"},
    {"url": "https://i.imgflip.com/4t0n1.jpg", "caption": "Αν το Netflix ήταν χώρα, θα ήμουν πολίτης 😎📺"},
]

@bot.command()
async def meme(ctx):
    item = random.choice(fun_memes)
    await ctx.send(f"{item['caption']}\n{item['url']}")

# ---------- Ticket command ----------
@bot.command()
async def ticket(ctx):
    class TicketSelect(Select):
        def __init__(self):
            options = [
                discord.SelectOption(label="🛒Buy A Product", description="☝️ If you have a problem with a product, click here", value="**🛒Welcome to the store, what product do you want to get? Ticket 🎫**"),
                discord.SelectOption(label="📞Support", description="☝️ If you have a problem with a product, click here", value="**📞Welcome to support, what problem are you having? Ticket 🎫**"),
            ]
            super().__init__(placeholder="click here for whatever you want", options=options)
            
        async def callback(self, interaction: discord.Interaction):
            user = interaction.user
            guild = interaction.guild

            # Παίρνουμε το label που επέλεξε ο χρήστης
            ticket_type = self.values[0]
            ticket_label = next(o.label for o in self.options if o.value == ticket_type)

            # --- Μήνυμα στο ίδιο κανάλι (όπως στη φωτό) ---
            if ticket_label == "📞Support":
                await interaction.response.send_message(
                    f"✅ **You opened a Support ticket**",  
                    ephemeral=True
                )
            elif ticket_label == "🛒Buy A Product":
                await interaction.response.send_message(
                    f"✅ **An Buy A Product ticket is being opened for you..**",
                    ephemeral=True
                )
                
            else:
                await interaction.response.send_message(
                    f"🎫 {interaction.user.mention}, άνοιξες ένα γενικό ticket.",
                    ephemeral=True
                )
                
            # Δημιουργούμε prefix ανάλογα με το label
            if ticket_label == "📞Support":
                channel_prefix = "📞Support"
            elif ticket_label == "🛒Buy A Product":
                channel_prefix = "🛒Buy A Product"
            else:
                channel_prefix = "🎫ticket"

            # Δημιουργούμε ασφαλές όνομα χρήστη
            safe_name = "".join(c for c in user.name if c.isalnum() or c in "-_").lower()
            if not safe_name:
                safe_name = f"user{user.id}"

            # Φτιάχνουμε το όνομα του καναλιού
            channel_name = f"{channel_prefix}-{safe_name}"

            # Αν υπάρχει ήδη, προσθέτουμε αριθμό στο τέλος
            i = 1
            while discord.utils.get(guild.channels, name=channel_name):
                channel_name = f"{channel_prefix}-{safe_name}-{i}"
                i += 1

            # Παίρνουμε το value που επέλεξε ο χρήστης
            ticket_type = self.values[0]

            # Βρίσκουμε το label του
            ticket_label = next(o.label for o in self.options if o.value == ticket_type)

            # Δημιουργούμε ή βρίσκουμε κατηγορία με βάση το label (π.χ. 📞Support)
            category_name = ticket_label
            category = discord.utils.get(guild.categories, name=category_name)
            if category is None:
                category = await guild.create_category(category_name)
            
            # --- Δημιουργία ονόματος καναλιού ανάλογα με την επιλογή ---
            ticket_type = self.values[0]  # παίρνει την επιλογή από το dropdown (π.χ. "owner", "general", "ban" κλπ)

            # Λεξικό για αντιστοίχιση τύπων σε prefix
            prefixes = {
                "🛒Welcome to the store, what product do you want to get?": "🛒Welcome to the store, what product do you want to get?",
            }

            # Αν δεν υπάρχει τύπος, βάζει "ticket"
            prefix = prefixes.get(ticket_type, "📞Support")
     
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
                    
            ticket_channel = await guild.create_text_channel(channel_name, category=category, overwrites=overwrites, topic=f"Ticket για {user}")

            # embed που στέλνει μέσα
            embed = discord.Embed(
                title=f"{self.values[0]}",
                description=f"❤️‍🔥**Welcome to the team**❤️‍🔥{user.mention}\n\n**Welcome to the team what would you like**❤️‍🔥\n\n**If you want the ticket closed, click here ⛔ Delete Ticket**",
                color=EMBED_COLOR
            ) 
            embed.set_thumbnail(url=THUMBNAIL_URL)
            
            from datetime import datetime
            import pytz

            # Ζώνη ώρας Ελλάδας
            greece_tz = pytz.timezone("Europe/Athens")

            # Παίρνει την τωρινή ώρα Ελλάδας
            current_time = datetime.now(greece_tz)

            # Μορφοποιεί σωστά την ώρα (χωρίς 0 μπροστά και με AM/PM)
            time_str = current_time.strftime("%I:%M %p").lstrip("0")

            embed.set_footer(
                text=f"{user.name} | Today at {time_str}",
                icon_url=user.display_avatar.url
            )

            # κουμπί διαγραφής
            delete_button = Button(label="⛔ Delete Ticket", style=discord.ButtonStyle.red)
            
            async def delete_cb(btn_interaction: discord.Interaction):
                # ✅ Κάνουμε defer για να ΜΗΝ δείχνει "αλληλεπίδραση απέτυχε"
                await btn_interaction.response.defer(thinking=False)

                # Δημιουργούμε embed
                close_embed = discord.Embed(
                    title="**Saving file**",
                    description="**The ticket will close in 10 seconds.**",
                    color=discord.Color.blue()
                )
                import datetime

                greece_tz = pytz.timezone("Europe/Athens")
                current_time = datetime.datetime.now(greece_tz)
                time_str = current_time.strftime("%I:%M %p").lstrip("0")

                close_embed.set_footer(
                    text=f"{btn_interaction.user.name} | Today at {time_str}",
                    icon_url=btn_interaction.user.display_avatar.url        
                )

                # Στέλνουμε το embed απάντηση στο τελευταίο μήνυμα
                last_message = None
                async for msg in ticket_channel.history(limit=1):
                    last_message = msg

                if last_message:
                    await last_message.reply(embed=close_embed)
                else:
                    await ticket_channel.send(embed=close_embed)

                # Περιμένει 10 δευτερόλεπτα και μετά διαγράφει το κανάλι
                await asyncio.sleep(10)
                try:
                   await ticket_channel.delete()
                except Exception as e:
                    print(f"⚠️ Σφάλμα κατά τη διαγραφή του ticket: {e}")

            delete_button.callback = delete_cb
            view = View()
            view.add_item(delete_button)
            
            await ticket_channel.send(content=f"{user.mention}", embed=embed, view=view)
    
    class TicketView(View):
        def __init__(self):
            super().__init__(timeout=None)
            self.add_item(TicketSelect())

    embed = discord.Embed(title=EMBED_TITLE, description=EMBED_DESCRIPTION, color=EMBED_COLOR)
    embed.set_author(
    name="Pts On Top Ticket System",
    icon_url="https://media.discordapp.net/attachments/1432624239093092384/1433589942025715855/a_649a20666f8b2fc068485749f726efc6.webp?ex=69053e2c&is=6903ecac&hm=2ae0c7846b316afea4984854dab0cc43acf985b29e4c1e22fbdfa0e2690d75c9&=&animated=true"
)

    embed.set_thumbnail(url=THUMBNAIL_URL)
    await ctx.send(embed=embed, view=TicketView())

# ---------- Run (Railway expects token in env var DISCORD_TOKEN) ----------
bot.run(os.getenv("DISCORD_TOKEN"))

TOKEN = os.getenv("DISCORD_TOKEN")
client.run(TOKEN)
