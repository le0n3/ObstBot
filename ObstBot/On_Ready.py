import On_Tasks

def Ready(client):
    @client.event
    async def on_ready():
        print("Ich habe mich angemeldet als {}".format(client.user))
        client.loop.create_task(On_Tasks.proben_check(client))
