import discord
import On_message
import On_Ready
import On_reaction_add

def main():
    print("Ich Starte")
    intents = discord.Intents.default()
    intents.members = True
    client = discord.Client(intents=intents)

    On_Ready.Ready(client)
    On_message.messages(client)
    On_reaction_add.On_reationen(client)



    client.run('Demmo Key')  # Obst bot

main()


