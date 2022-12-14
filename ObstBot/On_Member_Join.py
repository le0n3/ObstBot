import discord
import discord.utils


def member_Join(client):
    #region Join
    @client.event
    async def on_member_join(member):
        dm = await member.create_dm()
        await dm.send("Welche Aup Gruppe bist du (Cherry / Papaya / Avocado / Banana / Apple / Mango)")
        guild = client.get_guild(898521020766515210)
        role = discord.utils.get(guild.roles, id=907616310349938749)
        await member.add_roles(role)
    # endregion