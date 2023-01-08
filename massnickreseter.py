import discord
from discord.ext import commands;
import json

with open('config.json') as f:
    config = json.load(f)

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix = config["prefix"],intents = intents)



@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.command()
async def unnickall(ctx):


    if ctx.author.guild_permissions.manage_nicknames:

        embed = discord.Embed(title=f"Starting... 🔃",description="Initiating mass unnick", color=0x000000)
        await ctx.send(embed=embed)

        amount = 0

        async for member in ctx.guild.fetch_members(limit=None):
            
            amount+=1

            try:
                await member.edit(nick=None)
            except (discord.Forbidden, discord.HTTPException) as error:
                amount-=1

                embed = discord.Embed(title=f"Error {error}",description=f"With User: {member.name}#{member.discriminator}", color=0x000000)
                await ctx.send(embed=embed)
                continue
        
        embed = discord.Embed(title=f"Success! ✅",description=f"Unnicked {amount} of users!", color=0x000000)
        await ctx.send(embed=embed)
        return

    embed = discord.Embed(title="Invalid Permissions",description=f"{ctx.author.mention} does not have the MANAGE_NICKNAMES permission in the guild", color=0x000000)

    await ctx.send(embed=embed)
    return
    
    
        

client.run(config["token"])
