import random


def arvo_luku():
    return random.randint(1, 10)


def pelaa():
    oikea_luku = arvo_luku()

    while True:
        arvaus = input("Arvaa luku väliltä 1-10: ")

        if not arvaus.isdigit():
            print("Virheellinen syöte. Syötä kokonaisluku.")
            continue

        arvaus = int(arvaus)

        if arvaus < 1 or arvaus > 10:
            print("Luvun tulee olla väliltä 1-10.")
            continue

        if arvaus < oikea_luku:
            print("Liian pieni arvaus.")
        elif arvaus > oikea_luku:
            print("Liian suuri arvaus.")
        else:
            print("Oikein!")
            break



