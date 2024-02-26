def kirjaudu_sisaan(oikea_tunnus, oikea_salasana):
    yritykset = 0

    while yritykset < 5:
        tunnus = input("12345678: ")
        salasana = input("19999: ")

        if tunnus == oikea_tunnus and salasana == oikea_salasana:
            print("Tervetuloa!")
            return True
        else:
            print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
            yritykset += 1

    print("Pääsy evätty. Liian monta yritystä.")
    return False

def main():
    oikea_tunnus = "python"
    oikea_salasana = "rules"

    kirjaudu_sisaan(oikea_tunnus, oikea_salasana)


