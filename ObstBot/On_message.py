import random
import discord
import discord.utils
import datetime
import On_Tasks
import SQL_Connector
import Games
import re


def messages(client):
    # region client event on message
    @client.event
    async def on_message(nachricht):

        # region Variable

        # Quotes Chanelle
        zitate = client.get_channel(960856580654510121)
        # Archive with Teacher Quotes
        lehrer_zitate_archiv = client.get_channel(953989554321371146)
        # Archive with Student Quotes
        schueler_zitate_archiv = client.get_channel(961508892607676416)
        # Archive with company quotes
        betribs_zitate_archiv = client.get_channel(994539048368611418)
        # The Chanell in which performance records are announced
        proben_chanelle = client.get_channel(941288501712932864)
        # The Chanell in which votes are held
        abstimmung_chanelle = client.get_channel(978181949636112405)
        # Here info about the bot becomes visible for the admins
        log_chanelle = client.get_channel(978647339998785536)
        # Beautiful words to describe things
        schoene_woerter = ["toll", "super", "schön", "fabelhaft", "nett", "einzigartig", "wunderbar", "cool"]
        # Saves the current message in lowercase
        content = str(nachricht.content).lower()

        # endregion

        # region DM

        # Replies to direct messages
        if not nachricht.guild:
            await nachricht.channel.send('Was ist dein Anligen!?!? ')
        #endregion

        # region Commands Finden

        # Writes a teacher quote in the quotes Chanelle
        if content == "!LZ".lower():
            await command_LZ(nachricht, log_chanelle, zitate)

        # Writes a teacher quote in the archive
        if content.startswith("!LZAdd".lower()):
            await command_LZAdd(nachricht, log_chanelle, lehrer_zitate_archiv)

        # Writes a student quote in the quotes Chanelle
        if content == "!SZ".lower():
            await command_SZ(nachricht, log_chanelle, zitate)

        # Writes a student quote in the archive
        if content.startswith("!SZAdd".lower()):
            await command_SZAdd(nachricht, log_chanelle, schueler_zitate_archiv)

        # Writes an operating quote in the quotes Chanelle
        if content == "!BZ".lower():
            await command_BZ(nachricht, log_chanelle, zitate)

        # Writes an operating quote in the archive
        if content.startswith("!BZAdd".lower()):
            await command_BZAdd(nachricht, log_chanelle, betribs_zitate_archiv)

        # Poses request for quote editing
        if content.startswith("!Zrep".lower()):
            await command_Zrep(nachricht, log_chanelle)

        # Adds a performance record to the performance record chanelle
        if content.startswith("!Padd".lower()):
            await command_PAdd(nachricht, log_chanelle, proben_chanelle)

        # Displays the help
        if content == ("!help".lower()) or content == ("!h".lower()):
            await command_help(nachricht, log_chanelle)

        # Triggers the Scherg ester egg
        if "scherg" in content and not content.startswith("!"):
            await command_ser(nachricht, log_chanelle)

        # Triggers the Baumgärtel ester egg
        if "baumgärtel" in content and not content.startswith("!"):
            await command_baum(nachricht, log_chanelle, schoene_woerter)

        # Displays a random RGB color
        if content == "!randrgb".lower():
            await command_randrgb(nachricht, log_chanelle)

        # Displays a random hexadecimal  color
        if content == "!randhexcolor".lower():
            await command_randhex(nachricht, log_chanelle)

        # Converts a number into the binary system
        if content.startswith("!tobin".lower()):
            await command_tobin(nachricht, log_chanelle)

        # Converts a number into the hexadecimal  system
        if content.startswith("!tohex".lower()):
            await command_tohex(nachricht, log_chanelle)

        # gives out infos about the ISS
        if content == "!iss".lower():
            await command_iss(nachricht, log_chanelle)

        # gives out info about the weather
        if nachricht.content == "!wetter".lower():
            await command_wetter(nachricht, log_chanelle)

        # Writes a joke
        if nachricht.content == "!joke":
            await command_joke(nachricht, log_chanelle)

        # Triggers the Chirstopher easter egg
        if "christoph" in content and not content.startswith("!"):
            await command_cristofenr(nachricht, log_chanelle)

        # Triggers the voting command
        if nachricht.channel == abstimmung_chanelle and nachricht.author != client.user:
            await command_abstimmung(nachricht, log_chanelle)

        # Adds you to the Socal Credit system
        if content == "!AddTooSystem".lower():
            await command_addtosystem(nachricht, log_chanelle)

        # Outputs your Socal Credit
        if content == "!MyCredits".lower():
            await command_getcredits(nachricht, log_chanelle)

        # Displays a ranking list
        if content == "!rang".lower():
            await command_rang(nachricht, log_chanelle)

        # Outputs the games info
        if content == "!games".lower():
            await command_gameinf(nachricht, log_chanelle)

        # Starts the game Hi or Low
        if content.startswith("!HiOrLow".lower()):
            await command_hiorlow(nachricht, log_chanelle)

        # Starts the game All in
        if content == "!AllIn".lower():
            await command_allin(nachricht, log_chanelle)

        if content == "LOL".lower():
            await nachricht.channel.send("LOL !?!?")


        # endregion

    # endregion

    # region command Functionen don't look at this crap :)

    async def command_LZ(nachricht, log_test_chanelle, zitate):
        await log_test_chanelle.send(f"Info: Lehrer Zitat von {nachricht.author} Abgefragt")
        await nachricht.delete()
        await zitate.send(await On_Tasks.lehrerzitate(client))

    async def command_LZAdd(nachricht, log_test_chanelle, lehrer_zitate_archiv):
        await log_test_chanelle.send(f"Info: Lehrer Zitat  von {nachricht.author} hinzugefügt")
        await nachricht.delete()
        zitat = str(nachricht.content)
        pattern = re.compile("!LZadd", re.IGNORECASE)
        zitat = pattern.sub("", zitat)
        zitat = zitat.lstrip()
        await lehrer_zitate_archiv.send(zitat)

    async def command_BZ(nachricht, log_test_chanelle, zitate):
        await log_test_chanelle.send(f"Info: Lehrer Zitat von {nachricht.author} Abgefragt")
        await nachricht.delete()
        await zitate.send(await On_Tasks.betribs_zitate(client))

    async def command_BZAdd(nachricht, log_test_chanelle, betribs_zitate_archiv):
        await log_test_chanelle.send(f"Info: Lehrer Zitat  von {nachricht.author} hinzugefügt")
        await nachricht.delete()
        zitat = str(nachricht.content)
        pattern = re.compile("!BZadd", re.IGNORECASE)
        zitat = pattern.sub("", zitat)
        zitat = zitat.lstrip()
        await betribs_zitate_archiv.send(zitat)

    async def command_SZ(nachricht, log_test_chanelle, zitate):
        await log_test_chanelle.send(f"Info: Schüler Zitat von {nachricht.author} Abgefragt")
        await nachricht.delete()
        await zitate.send(await On_Tasks.schueler_zitate(client))

    async def command_SZAdd(nachricht, log_test_chanelle, schueler_zitate_archiv):
        await log_test_chanelle.send(f"Info: Schüler Zitat von {nachricht.author} hinzugefügt")
        await nachricht.delete()
        zitat = str(nachricht.content)
        pattern = re.compile("!SZadd", re.IGNORECASE)
        zitat = pattern.sub("", zitat)
        zitat = zitat.lstrip()
        await schueler_zitate_archiv.send(zitat)

    async def command_Zrep(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: Schüler Zitat replays anfrage von {nachricht.author}")
        await nachricht.channel.send(
            "Melde dich bei leon323#6586 um ein zitat zu Endern. Er entscheidet ob ihr würdig seid", delete_after=10)

    async def command_PAdd(nachricht, log_test_chanelle, proben_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: Eine Probe wurde von {nachricht.author} hinzugefügt")
        mess = str(nachricht.content)
        mess = mess.replace("!Padd", "")
        mess = mess.lstrip()
        counter = mess.count("|")
        if counter == 2:
            messsplit = mess.split("|")
            try:
                _ = datetime.datetime.strptime(messsplit[2].lstrip(), "%d.%m.%Y")
                await proben_chanelle.send(mess)
            except:
                await nachricht.channel.send("Datum nicht richtig (Bsp. 12.06.2022)", delete_after=10)
        else:
            await nachricht.channel.send("Bitte baue deine angabe wie folgt auf: Fach | Stoff | Datum ",
                                         delete_after=10)

    async def command_help(nachricht, log_test_chanelle):
        await log_test_chanelle.send(f"Info: Help wurde von {nachricht.author} ausgelöst")
        await nachricht.delete()
        await nachricht.channel.send(
            "__Hilfe zum Obst-Bot.__\n**Diese Nachricht löscht sich in 30 Ticks.**\n\nLehrerzitate:\n- !LZ: Schreibt ein random Lehrer Zitat in Zitate.\n- !LZadd: Fügt das Zitat in das Lehrerzitate-Archiv hinzu.\n\nSchülerzitate:\n- !SZ: Schreibt ein random Schüler Zitat in Zitate.\n- !SZadd: Fügt das Zitat in das Schülerzitate-Archiv hinzu.\n- !Zrep: Bei Problemen in einem zitat \n\nSocialCredit System\n- !MyCredits: Zeigt dir deinen verdienten Credits\n- !AddTooSystem: fügt dich dem SocialCredit System hinzu\n- !games: listet aller spiele auf\n- !rang: zeigt die 3 besten Spieler an\n\nProben:\n- der Bot schreibt 1 Tag vor der Probe eine Nachricht um 18 Uhr was sie lernen solltest\n- !Padd: Fügt ein Leistungsnachweis hinzu (Fach | Stoff | Datum)\n\nRandom:\n- !randrgb\n- !randhexcolor\n- !tobin (zahl)\n- !tohex (zahl)\n- !iss\n- !wetter\n- !joke\n\nGeheime Funktionen:\nDieser Bot antwortet auf bestimmte Wörterkombinationen.",
            delete_after=30)

    async def command_ser(nachricht, log_test_chanelle, schoene_woerter):
        if nachricht.author != client.user:
            s = On_Tasks.s_Counter()
            if s % 5 == 0:
                await log_test_chanelle.send(f"Info: Scherg PNG wurde von {nachricht.author} ausgelöst")
                await nachricht.channel.send(file=discord.File("img/red.png"), delete_after=40)

            scherg = False
            for woert in schoene_woerter:
                if woert in str(nachricht.content).lower():
                    scherg = True
            if scherg:
                await log_test_chanelle.send(f"Info: Scherg wurde von {nachricht.author} ausgelöst")
                await nachricht.channel.send("NEIN!!!!")
                scherg = False

    async def command_baum(nachricht, log_test_chanelle, schoene_woerter):
        if nachricht.author != client.user:
            baum = False
            for woert in schoene_woerter:
                if woert in str(nachricht.content).lower():
                    baum = True
            if baum:
                await log_test_chanelle.send(f"Info: Baumgätel wurde von {nachricht.author} ausgelöst")
                await nachricht.channel.send("JA!!!!")
                baum = False

    async def command_randrgb(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: randrgb wurde von {nachricht.author} ausgelöst")
        await nachricht.channel.send(str(On_Tasks.Random_rgb()), delete_after=30)

    async def command_randhex(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: randhexcolor wurde von {nachricht.author} ausgelöst")
        await nachricht.channel.send(str(On_Tasks.random_hex_color()), delete_after=30)

    async def command_tobin(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: tobin wurde von {nachricht.author} ausgelöst")
        mess = str(nachricht.content).replace("!tobin", "")
        try:
            dec = int(mess)
            await nachricht.channel.send(str(On_Tasks.dec_to_bin(dec)), delete_after=30)
        except:
            await nachricht.channel.send("Du brauchst ein int", delete_after=30)

    async def command_tohex(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: tohex wurde von {nachricht.author} ausgelöst")
        mess = str(nachricht.content).replace("!tohex", "")
        try:
            dec = int(mess)
            await nachricht.channel.send(str(On_Tasks.dec_to_hex(dec)), delete_after=30)
        except:
            await nachricht.channel.send("Du brauchst ein int", delete_after=30)

    async def command_iss(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: ISS wurde von {nachricht.author} ausgelöst")
        await nachricht.channel.send(On_Tasks.iss(), delete_after=40)

    async def command_wetter(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: Wetter wurde von {nachricht.author} ausgelöst")
        await nachricht.channel.send(On_Tasks.wether(), file=discord.File("img/sky.jpg"), delete_after=40)

    async def command_joke(nachricht, log_test_chanelle):
        await nachricht.delete()
        await log_test_chanelle.send(f"Info: Joke wurde von {nachricht.author} ausgelöst")
        await nachricht.channel.send(On_Tasks.joke())

    async def command_cristofenr(nachricht, log_test_chanelle):
        if nachricht.author != client.user:
            r = random.randint(1, 3)
            if r == 1:
                await log_test_chanelle.send(f"Info: Christop wurde von {nachricht.author} ausgelöst")
                await nachricht.channel.send("Chillig Chillig Chillig", delete_after=40)

    async def command_abstimmung(nachricht, log_test_chanelle):
        x = '\U0000274C'
        check = '\U00002705'
        await nachricht.add_reaction(x)
        await nachricht.add_reaction(check)
        await log_test_chanelle.send(f"Info: Abstümung wurde ausgelöst")

    async def command_addtosystem(nachricht, log_test_chanelle):
        jn = SQL_Connector.NweUser(str(nachricht.author))
        await  nachricht.delete()
        if jn.startswith("Error: "):
            await log_test_chanelle.send(jn)
        else:
            await log_test_chanelle.send(f"Info: AddTooSystem wurde von {nachricht.author} ausgelöst")
            await nachricht.channel.send(jn, delete_after=15)

    async def command_getcredits(nachricht, log_test_chanelle):
        credits = SQL_Connector.GetMyCredits(str(nachricht.author))
        await  nachricht.delete()
        if credits.startswith("Error: "):
            await log_test_chanelle.send(credits)
        else:
            await log_test_chanelle.send(f"Info: MyCredits wurde von {nachricht.author} ausgelöst")
            await nachricht.channel.send(credits, delete_after=15)

    async def command_rang(nachricht, log_test_chanelle):
        mess = SQL_Connector.TopThree()
        await nachricht.delete()
        await nachricht.channel.send(mess, delete_after=15)
        await log_test_chanelle.send(f"Info: Rang wurde von {nachricht.author} ausgelöst")

    async def command_gameinf(nachricht, log_test_chanelle):
        await nachricht.delete()
        await nachricht.channel.send(
            "Games:\n - !HiOrLow (Wie viele Credits möchtest du Einsetzen)|(High -> h; Low -> l)\n - !AllIn Setze alle deine Credits und verdopple oder verliere alles.",
            delete_after=30)
        await log_test_chanelle.send(f"Info: Help Games wurde von {nachricht.author} ausgelöst")

    async def command_hiorlow(nachricht, log_test_chanelle):
        await  nachricht.delete()
        mess = str(nachricht.content)
        mess = mess.replace("!HiOrLow", "")
        mess = mess.lstrip()
        counter = mess.count("|")
        if counter == 1:
            messsplit = mess.split("|")
            try:
                info = Games.HiOrLow(str(nachricht.author), int(messsplit[0]), str(messsplit[1]).strip())
                await nachricht.channel.send(info, delete_after=30)
                await log_test_chanelle.send(f"Info: HiOrLow wurde von {nachricht.author} gespielt")
            except:
                await nachricht.channel.send("Fheler bei der angabe der daten")

    async def command_allin(nachricht, log_test_chanelle):
        await  nachricht.delete()
        mess = Games.AllIn(str(nachricht.author))
        await nachricht.channel.send(mess, delete_after=30)
        await log_test_chanelle.send(f"Info: All In wurde von {nachricht.author} gespielt")

    # endregion
