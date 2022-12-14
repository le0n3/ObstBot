import MySQLdb

try:
    connetion = MySQLdb.connect(
        #Your SQL Database
    )
    connetion.autocommit(True)

except:
    print("Bei der Verbindung mit der datenbank ist ein fehler aufgetreten ")


def NweUser(Username):
    try:
        UserExists = f"SELECT User_name FROM SocialCredit WHERE User_name = '{Username}';"
        with connetion.cursor() as SQL_Abfrage_New_User_Check:
            SQL_Abfrage_New_User_Check.execute(UserExists)
            all = SQL_Abfrage_New_User_Check.fetchall()
            SQL_Abfrage_New_User_Check.close()
        if len(all) != 0:
            return "Dich Gibt es bereits!!"
        else:
            UserAdd = f"INSERT INTO SocialCredit (User_name, SocialCredit) VALUES ('{Username}', 0);"
            with connetion.cursor() as SQL_Insert:
                SQL_Insert.execute(UserAdd)
                SQL_Insert.close()
            return "Du wurdes hinzugefügt!!"
    except:
        SQL_Abfrage_New_User_Check.close()
        SQL_Insert.close()
        return "Digga Fheler oder so frag Leon"


def SocialCreditUP(User):
    getcredit = f"SELECT SocialCredit FROM SocialCredit WHERE User_name = '{User}';"
    try:
        with connetion.cursor() as SQL_Abfrage:
            SQL_Abfrage.execute(getcredit)
            credit = SQL_Abfrage.fetchall()
            SQL_Abfrage.close()
        if len(credit) == 0:
            NweUser(User)
        else:
            try:
                credit = credit[0][0]
                credit += 10
                UpdateCredits = f"UPDATE SocialCredit SET SocialCredit = {credit} WHERE User_name = '{User}' "
                with connetion.cursor() as SQL_Insert:
                    SQL_Insert.execute(UpdateCredits)
                    SQL_Insert.close()
                return ""
            except:
                SQL_Insert.close()
                return "Datenbank Fehler versuche es später erneut"
    except Exception as e:
        SQL_Abfrage.close()

        return f"Error: {e}"


def SocialCreditDown(User):
    getcredit = f"SELECT SocialCredit FROM SocialCredit WHERE User_name = '{User}';"
    try:
        with connetion.cursor() as SQL_Abfrage:
            SQL_Abfrage.execute(getcredit)
            credit = SQL_Abfrage.fetchall()
            SQL_Abfrage.close()
        if len(credit) == 0:
            NweUser(User)
        else:
            try:
                credit = credit[0][0]
                credit -= 10
                UpdateCredits = f"UPDATE SocialCredit SET SocialCredit = {credit} WHERE User_name = '{User}' "
                with connetion.cursor() as SQL_Insert:
                    SQL_Insert.execute(UpdateCredits)
                    SQL_Insert.close()
                return ""
            except:
                SQL_Insert.close()
                return "Datenbank Fehler versuche es später erneut"
    except Exception as e:
        SQL_Abfrage.close()
        return f"Error: {e}"


def SocialCreditEdit(User, Credits):
    getcredit = f"SELECT SocialCredit FROM SocialCredit WHERE User_name = '{User}';"
    try:
        with connetion.cursor() as SQL_Abfrage:
            SQL_Abfrage.execute(getcredit)
            credit = SQL_Abfrage.fetchall()
            SQL_Abfrage.close()
        if len(credit) == 0:
            NweUser(User)
        else:
            try:
                credit = credit[0][0]
                credit += Credits
                UpdateCredits = f"UPDATE SocialCredit SET SocialCredit = {credit} WHERE User_name = '{User}' "
                with connetion.cursor() as SQL_Insert:
                    SQL_Insert.execute(UpdateCredits)
                    SQL_Insert.close()
                return ""
            except:
                SQL_Insert.close()
                return "Datenbank Fehler versuche es später erneut"
    except Exception as e:
        SQL_Abfrage.close()

        return f"Error: {e}"


def GetMyCredits(User):
    getcredit = f"SELECT SocialCredit FROM SocialCredit WHERE User_name = '{User}';"
    try:
        with connetion.cursor() as SQL_Abfrage:
            SQL_Abfrage.execute(getcredit)
            credit = SQL_Abfrage.fetchall()
            SQL_Abfrage.close()
        if len(credit) == 0:
            return f"{User} du bist noch nicht im Credet System Angemeldet"
        else:
            return f"{User} hat {credit[0][0]} SocialCredit in der Hosentasche"

    except Exception as e:
        SQL_Abfrage.close()
        return f"Error: {e}"


def TopThree():
    UserExists = "SELECT * FROM SocialCredit ORDER BY SocialCredit desc LIMIT 3;"
    try:
        with connetion.cursor() as SQL_Abfrage_TopThree:
            SQL_Abfrage_TopThree.execute(UserExists)
            all = SQL_Abfrage_TopThree.fetchall()
            SQL_Abfrage_TopThree.close()
            return f"1. Platz gewinnt {all[0][0]} mit {all[0][1]} Punkten !!!\n2. Platz gewinnt {all[1][0]} mit {all[1][1]} Punkten !!\n3. Platz gewinnt {all[2][0]} mit {all[2][1]} Punkten !"

    except Exception as e:
        SQL_Abfrage_TopThree.close()
        return f"Error: {e}"


def ConCheck():
    UserExists = "SELECT * FROM SocialCredit LIMIT 1;"
    try:
        with connetion.cursor() as SQL_Abfrage_Check:
            SQL_Abfrage_Check.execute(UserExists)
            _ = SQL_Abfrage_Check.fetchall()
            SQL_Abfrage_Check.close()
            return "OK"

    except Exception as e:
        SQL_Abfrage_Check.close()
        return f"Error: {e}"


def GetCredits(User):
    getcredit = f"SELECT SocialCredit FROM SocialCredit WHERE User_name = '{User}';"
    try:
        with connetion.cursor() as SQL_Abfrage:
            SQL_Abfrage.execute(getcredit)
            credit = SQL_Abfrage.fetchall()
            SQL_Abfrage.close()
        if len(credit) == 0:
            return f"{User} du bist noch nicht im Credet System Angemeldet"
        else:
            return credit[0][0]

    except Exception as e:
        SQL_Abfrage.close()
        return f"Error: {e}"
