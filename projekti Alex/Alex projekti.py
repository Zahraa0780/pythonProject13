+def main():
    pisteet = 0

    print(
        "Olipa kerran pelaaja nimeltä Alex. Alex oli aina kiehtonut eurooppalaista kulttuuria, historiaa ja maantiedettä, ja hän päätti lähteä matkalle vieraillakseen 20 maassa Euroopassa.")
    print()

    # Saksa
    vastaus = input("Alex aloitti matkansa Saksasta, missä häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "berliini":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Berliini.")

    # Italia
    vastaus = input(
        "Seuraavaksi hän matkusti Italiaan, jossa häntä pyydettiin tunnistamaan kuuluisa italialainen kaupunki, joka tunnetaan kanavistaan ja gondoleistaan: ")
    if vastaus.lower() == "venetsia":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Venetsia.")

    # Ranska
    vastaus = input("Italiasta Alex lensi Ranskaan, missä häntä pyydettiin nimeämään virallinen kieli: ")
    if vastaus.lower() == "ranska":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Ranska.")

    # Norja
    vastaus = input(
        "Seuraavaksi hän matkusti Norjaan, 'keskyyön auringon maahan', jossa häntä pyydettiin nimeämään kolikko: ")
    if vastaus.lower() == "norjan kruunu":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Norjan kruunu.")

    # Slovakia
    vastaus = input("Sitten hän lensi Slovakiaan, jossa häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "bratislava":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Bratislava.")

    # Kroatia
    vastaus = input("Kroatiassa häntä pyydettiin nimeämään kuuluisa kaupunki Adrianmeren rannalla: ")
    if vastaus.lower() == "dubrovnik":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Dubrovnik.")

    # Espanja
    vastaus = input("Espanjassa häntä pyydettiin nimeämään kansallisurheilulaji: ")
    if vastaus.lower() == "jalkapallo":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Jalkapallo.")

    # Alankomaat
    vastaus = input("Alankomaissa häntä pyydettiin nimeämään maan kuuluisat kukkapellot: ")
    if vastaus.lower() == "tulppaanit":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Tulppaanit.")

    # Tsekki
    vastaus = input("Sitten hän matkusti Tšekkiin, missä häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "praha":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Praha.")

    # Itävalta
    vastaus = input("Itävallassa häntä pyydettiin nimeämään kuuluisa ruokalaji, josta maa on kuuluisa: ")
    if vastaus.lower() == "wiener schnitzel":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Wiener Schnitzel.")

    # Puola
    vastaus = input("Sitten hän lensi Puolaan, missä häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "varsova":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Varsova.")

    # Saksa (Schwarzwald)
    vastaus = input("Saksassa häntä pyydettiin nimeämään kuuluisa metsä, josta maa on kuuluisa: ")
    if vastaus.lower() == "schwarzwald":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Schwarzwald.")

    # Norja (vuonot)
    vastaus = input(
        "Sitten hän matkusti Norjaan, jossa häntä pyydettiin nimeämään kuuluisa luonnonkohde, josta maa on kuuluisa: ")
    if vastaus.lower() == "vuonot":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Vuonot.")

    # Belgia
    vastaus = input("Sitten hän lensi Belgiaan, jossa häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "bryssel":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Bryssel.")

    # Unkari
    vastaus = input("Unkarissa häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "budapest":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Budapest.")

    # Englanti
    vastaus = input("Englannissa häntä pyydettiin nimeämään kuuluisa jalkapallojoukkue maassa: ")
    if vastaus.lower() == "manchester united":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Manchester United.")

    # Sveitsi
    vastaus = input("Sitten hän lensi Sveitsiin, missä häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "bern":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Bern.")

    # Portugali
    vastaus = input("Sitten hän matkusti Portugaliin, jossa häntä pyydettiin nimeämään pääkaupunki: ")
    if vastaus.lower() == "lissabon":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Lissabon.")

    # Alankomaat (Vincent van Gogh)
    vastaus = input("Alankomaissa häntä pyydettiin nimeämään kuuluisa taidemaalari: ")
    if vastaus.lower() == "vincent van gogh":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Vincent van Gogh.")

    # Irlanti
    vastaus = input("Sitten Irlannissa, jossa häntä pyydettiin nimeämään virallinen kieli: ")
    if vastaus.lower() == "irlanti (gaeli)":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Irlanti (gaeli).")

    # Kreikka
    vastaus = input(
        "Lopuksi hän lensi Kreikkaan, missä häntä pyydettiin nimeämään kuuluisa muinainen filosofi maasta: ")
    if vastaus.lower() == "sokrates":
        pisteet += 1
        print("Oikea vastaus! Pisteitä:", pisteet)
    else:
        print("Väärin. Oikea vastaus oli Sokrates.")

    print(
        "\nAlexin matka oli ohi, ja hän oli ylpeä kaikista matkan varrella kerätyistä pisteistä. Hän oppi paljon eurooppalaisesta kulttuurista, historiasta ja maantiedosta, eikä malttanut odottaa seuraavaa seikkailuaan.")


if __name__ == "__main__":
    main()
