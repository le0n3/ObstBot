import On_Tasks

def Ready(client):
    @client.event
    async def on_ready():
        print(f"Ich habe mich angemeldet als {client.user}")
        client.loop.create_task(On_Tasks.proben_check(client))
