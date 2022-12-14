import SQL_Connector


def On_reationen(client):
    @client.event
    async def on_reaction_add(reaction, user):
        log_chanele = client.get_channel(978647339998785536)

        if str(reaction) == '<:socialCredit_n:953230479388205076>':
            er = str(SQL_Connector.SocialCreditDown(reaction.message.author))
            if er != "":
                await log_chanele.send(er, delete_after=15)
            else:
                await log_chanele.send(f"{reaction.message.author}hat -10 Punkte bekommen")

        if str(reaction) == '<:socialCredit_p:953230479321092096>':
            er = str(SQL_Connector.SocialCreditUP(reaction.message.author))
            if er != "":
                await log_chanele.send(er, delete_after=15)
            else:
                await log_chanele.send(f"{reaction.message.author} hat +10 Punkte bekommen")

