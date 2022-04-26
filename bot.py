import discord
from discord.ext import commands
import json

bot_settingsGetItem = open("settings.json")
bot_settings = json.load(bot_settingsGetItem)
bot_settingsGetItem.close()

global activity

if bot_settings["botConfig"]["activity"]["activityType"] == "":
    activity = discord.Game(name=bot_settings["botConfig"]["activity"]["activityName"])
elif bot_settings["botConfig"]["activity"]["activityType"] == "playing":
    activity = discord.Game(name=bot_settings["botConfig"]["activity"]["activityName"])
elif bot_settings["botConfig"]["activity"]["activityType"] == "streaming":
    activity = discord.Streaming(name=bot_settings["botConfig"]["activity"]["activityName"], url=bot_settings["activity"]["activityURL"])
elif bot_settings["botConfig"]["activity"]["activityType"] == "listening":
    activity = discord.Activity(type=discord.ActivityType.listening, name=bot_settings["botConfig"]["activity"]["activityName"])
elif bot_settings["botConfig"]["activity"]["activityType"] == "watching":
    activity = discord.Activity(type=discord.ActivityType.watching, name=bot_settings["botConfig"]["activity"]["activityName"])
elif bot_settings["botConfig"]["activity"]["activityType"] is None:
    activity = discord.Game(name=bot_settings["botConfig"]["activity"]["activityName"])
     

bot = commands.Bot(command_prefix=bot_settings["botConfig"]["prefix"], activity=activity, status=discord.Status.idle)

@bot.event
async def on_ready():
    if bot_settings["botConfig"]["startBotMessage"] == True:    
        print("{} user is logged in!".format(bot.user.name))

if bot_settings["commands"]["clear"] == True:
    @bot.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, limit):
        await ctx.channel.purge(limit=int(limit + 1))
if bot_settings["commands"]["avatar"] == True:
    @bot.command()
    @commands.has_permissions(send_messages=True)
    async def avatar(ctx, user: discord.Member=None):
        if user is None:
            user = ctx.author
            await ctx.send(user.avatar_url)
        else:
            await ctx.send(user.avatar_url)

if bot_settings["commands"]["ban"] == True:
    @bot.command()
    @commands.has_permissions(ban_members=True)
    async def ban(ctx, member: discord.Member, * , reason):
        await member.ban(reason=reason)
        banEmbed = discord.Embed(
            title="Successful!",
            description="The person has been successfully banned!",
            color = discord.Color.blue()
        )
        banEmbed.add_field(name="Reason", value=reason, inline=False)
        banEmbed.add_field(name="Banned user", value=member, inline=True)
        banEmbed.add_field(name="Banned person", value=ctx.author, inline=True)
        await ctx.send(embed=banEmbed)

if bot_settings["commands"]["kick"] == True:
    @bot.command()
    @commands.has_permissions(kick_members=True)
    async def kick(ctx, member: discord.Member, *, reason):
        await member.kick(reason=reason)
        kickEmbed = discord.Embed(
            title="Successful!",
            description="The person has been successfully kicked!",
            color = discord.Color.blue()
        )
        kickEmbed.add_field(name="Reason", value=reason, inline=False)
        kickEmbed.add_field(name="Kicked user", value=member, inline=True)
        kickEmbed.add_field(name="Kicked person", value=ctx.author, inline=False)

        await ctx.send(embed=kickEmbed)

    
if bot_settings["commands"]["mute"]["muteCommand"] == True:
    @bot.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(ctx, member: discord.Member, * , reason):
        role = discord.utils.get(bot.get_guild(ctx.guild.id).roles, id=int(bot_settings["commands"]["mute"]["mutedRoleID"]))
        await member.add_roles(role)
        muteEmbed = discord.Embed(
            title="Successful",
            description="The person has been successfully muted!",
            color = discord.Color.blue()
        )
        muteEmbed.add_field(name="Reason", value=reason, inline=False)
        muteEmbed.add_field(name="Muted user", value=member, inline=True)
        muteEmbed.add_field(name="Muted person", value=ctx.author, inline=True)

        await ctx.send(embed=muteEmbed)



bot.run(bot_settings["botConfig"]["token"])
