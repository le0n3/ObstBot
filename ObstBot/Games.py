import random
import SQL_Connector

def HiOrLow(User, Credits, HiOrLow):
    ok = False
    credits = SQL_Connector.GetCredits(User)
    if credits >= Credits:
        ok = True
    else:
        return "Du hast nicht genug Chredits"
    if ok:
        Number = random.randint(0,10)
        win = False
        if Number <= 5:
            if HiOrLow == "l":
                win = True
        else:
            if HiOrLow == "h":
                win = True

        if win:
            SQL_Connector.SocialCreditEdit(User, Credits * 2)
            return f"Die zhal wahr {Number}.\n{User} hat {Credits * 2} Gewonnwn"
        else:
            SQL_Connector.SocialCreditEdit(User, (Credits - (Credits * 2)))
            return f"Die zhal wahr {Number}.\n{User} hat {Credits} Verloren"

def AllIn(User):
    Number = random.randint(0,1)
    Credits = SQL_Connector.GetCredits(User)
    if Credits > 0:
        if Number == 0:
                SQL_Connector.SocialCreditEdit(User, (Credits - (Credits * 2)))
                return f"{User} hat alle seine Credits Verloren"

        if Number == 1:
                SQL_Connector.SocialCreditEdit(User, Credits * 2)
                return f"{User} hat seine Credits Verdoppelt "
        else:
            return f"{User} hat nicht genug Credits für All In"

