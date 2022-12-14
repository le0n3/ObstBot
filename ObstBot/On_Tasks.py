import asyncio
import random
import discord
import datetime
import json
import urllib.request
import googletrans
import requests
import SQL_Connector

s = 0


async def lehrerzitate(client):
    zitate_id = list()
    zitate_archive = client.get_channel(953989554321371146)
    for mess in await zitate_archive.history(limit=200).flatten():
        zitate_id.append(mess.content)

    return random.choice(zitate_id)


async def schueler_zitate(client):
    zitate = list()
    zitate_archive = client.get_channel(961508892607676416)
    for mess in await zitate_archive.history(limit=200).flatten():
        zitate.append(mess.content)

    return random.choice(zitate)


async def betribs_zitate(client):
    zitate = list()
    zitate_archive = client.get_channel(994539048368611418)
    for mess in await zitate_archive.history(limit=200).flatten():
        zitate.append(mess.content)

    return random.choice(zitate)


async def status_task(client):
    while True:
        await client.change_presence(activity=discord.Game('Der Obst Bot'), status=discord.Status.online)
        await asyncio.sleep(30)
        await client.change_presence(activity=discord.Game('Hüter des Hauses'), status=discord.Status.online)
        await asyncio.sleep(30)
        await client.change_presence(activity=discord.Game('!help / !h'), status=discord.Status.online)
        await asyncio.sleep(30)


async def proben_check(client):
    generel = client.get_channel(898521020766515213)
    Log_test_Chanell = client.get_channel(978647339998785536)
    probejn = False
    while True:
        pruefzeit = datetime.time(12, 35)
        jetzt = datetime.datetime.now()
        await asyncio.sleep(30)
        check = SQL_Connector.ConCheck()
        if check != "OK":
            await Log_test_Chanell.send(check)

        if pruefzeit.strftime("%H:%M") == jetzt.strftime("%H:%M"):
            proben = client.get_channel(941288501712932864)
            for Probe in await proben.history(limit=200).flatten():
                probe = str(Probe.content)
                probe = probe.split('|')
                probeziet = datetime.datetime.strptime(probe[2].lstrip(), "%d.%m.%Y")

                morgen = jetzt + datetime.timedelta(days=1)

                if probeziet.strftime("%d.%m.%Y") == morgen.strftime("%d.%m.%Y"):
                    probejn = True
                    await generel.send(
                        f"@everyone,\nWir schreiben Morgen {probe[0].lstrip()}du solltest {probe[1].lstrip()} Lehrnen")
                elif probeziet.strftime("%d.%m.%Y") == jetzt.strftime("%d.%m.%Y"):
                    print(f"{probe[0].lstrip()} wurde gelöscht")
                    await Probe.delete()
        if probejn:
            probejn = False
            await asyncio.sleep(60)


def Random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    sgb = "RGB: (" + str(r) + ", " + str(g) + ", " + str(b) + ")"
    return "```" + sgb + "```"


def random_hex_color():
    r = lambda: random.randint(0, 255)
    return "```HEX: " + '#%02X%02X%02X' % (r(), r(), r()) + "```"


def dec_to_hex(dec):
    num = hex(dec)
    num = str(num).replace("0x", "")
    return "```hex(" + num + ")```"


def dec_to_bin(dec):
    dec = bin(dec)
    dec = str(dec).replace("0b", "")
    return "```bin(" + str(dec) + ")```"


def iss():
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    url2 = "http://api.open-notify.org/astros.json"
    response2 = urllib.request.urlopen(url2)
    result2 = json.loads(response2.read())

    asto = result2["number"]
    people = result2["people"]

    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    mess = f"ISS:\n   Position:\n   {str(lat)},  {str(lon)}\n \nAstronouts({str(asto)}):\n"

    for name in people:
        mess += ("    " + name["name"] + " on: " + name["craft"] + "\n")
    return "```" + mess + "```"


def wether():
    key = "Your OPWM Key"
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=49.94075694090485&lon=11.598245891210388&appid={key}"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())

    # Checking If there is no error and the status code is 200
    if data['cod'] == 200:
        Übersetzrt = googletrans.Translator()
        # getting the temperature from the json data
        tempk = (data['main']['temp'])
        tempc = round(tempk - 273.15, 2)
        # getting the pressure from the json data
        pressure = data['main']['pressure']
        # getting the humidity from the json data
        humidity = data['main']['humidity']
        # getting the description from the json data
        descr = data['weather'][0]['description']
        test = Übersetzrt.translate(descr, dest='de', src='en').text
        wind = data['wind']['speed']
        # Displaying all the data
        vis = data["visibility"]
        return f"Das Wetter:\n\nDie Wetterlage ist {test} (keine Garantie auf richtige übersetzung)\nDie Temperatur beträgt {str(tempc)} °C\nDer Luftdruck beträgt {pressure} hPa\nDie Luftfeuchtigkeit beträgt {humidity}  %\nDie Windgeschwindigkeit beträgt momentan {wind} m/s\nDu kannst {vis}m weit aus dem fenster schuen"
    else:
        # If any error occured then print this
        return "Ahhh Fehler !!!!"


def s_Counter():
    global s
    s += 1
    return s


def joke():
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=49.94075694090485&lon=11.598245891210388&appid=00e17795f9682c6f7972dc966e1bf2f9"

    url = "https://dad-jokes.p.rapidapi.com/random/joke"

    headers = {
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com",
        "X-RapidAPI-Key": "7f5c921148msh25939e18d39a476p1ae2e2jsn1f8d550c87d8"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.content)
    mess1 = data['body'][0]['setup']
    mess2 = data['body'][0]['punchline']
    return mess1 + "\n" + mess2
