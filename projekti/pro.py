import math
import sys
import mysql.connector
import random
import gmap
yhteys = mysql.connector.connect(
    host = '127.0.0.1',
    port= 3306,
    database = 'flight_game',
    user= 'root',
    password ='12345',
    autocommit = True
    )

def asKentta():
    numbers = input(int("Choose random numbers from 1 to 5!"))
    luku = numbers
    print("luku")
    print("Tähän random valinta Aasia nro [1].")  # kaikkiin kenttiin tarvitaan hakutoiminto, joka hakee tietokannasta
    print("Tähän random valinta Aasia nro [2].")  # satunnaisen kentän, jossa AIRPORT-CONTINENT pitää olla "AS"
    print("Tähän random valinta Aasia nro [3].")  # random.randrange(alku, loppu)
    print("Tähän random valinta Aasia nro [4].")
    print("Tähän random valinta Aasia nro [5].")

    valitseKentta = input("Valitse haluamasi lentokenttä: ")

    if valitseKentta == "1":
        print("Vaiheessa...")

    elif valitseKentta == "2":
        print("Vaiheessa...")

    elif valitseKentta == "3":
        print("Vaiheessa...")

    elif valitseKentta == "4":
        print("Vaiheessa...")

    elif valitseKentta == "5":
        print("Vaiheessa...")


def euKentta():
    print()
    print(
        "Tähän random valinta Eurooppa nro [1].")  # kaikkiin kenttiin tarvitaan hakutoiminto, joka hakee tietokannasta
    print("Tähän random valinta Eurooppa nro [2].")  # satunnaisen kentän, jossa AIRPORT-CONTINENT pitää olla "EU"
    print("Tähän random valinta Eurooppa nro [3].")  # random.randrange(alku, loppu)
    print("Tähän random valinta Eurooppa nro [4].")
    print("Tähän random valinta Eurooppa nro [5].")

    valitseKentta = input("Valitse haluamasi lentokenttä: ")

    if valitseKentta == "1":
        print("Vaiheessa...")

    elif valitseKentta == "2":
        print("Vaiheessa...")

    elif valitseKentta == "3":
        print("Vaiheessa...")

    elif valitseKentta == "4":
        print("Vaiheessa...")

    elif valitseKentta == "5":
        print("Vaiheessa...")


def afKentta():
    print()
    print("Tähän random valinta Afrikka nro [1].")  # kaikkiin kenttiin tarvitaan hakutoiminto, joka hakee tietokannasta
    print("Tähän random valinta Afrikka nro [2].")  # satunnaisen kentän, jossa AIRPORT-CONTINENT pitää olla "AF"
    print("Tähän random valinta Afrikka nro [3].")  # random.randrange(alku, loppu)
    print("Tähän random valinta Afrikka nro [4].")
    print("Tähän random valinta Afrikka nro [5].")

    valitseKentta = input("Valitse haluamasi lentokenttä: ")

    if valitseKentta == "1":
        print("Vaiheessa...")

    elif valitseKentta == "2":
        print("Vaiheessa...")

    elif valitseKentta == "3":
        print("Vaiheessa...")

    elif valitseKentta == "4":
        print("Vaiheessa...")

    elif valitseKentta == "5":
        print("Vaiheessa...")



def auKentta():
    print()
    print(
        "Tähän random valinta Australia nro [1].")  # kaikkiin kenttiin tarvitaan hakutoiminto, joka hakee tietokannasta
    print(
        "Tähän random valinta Australia nro [2].")  # satunnaisen kentän, jossa !!!AIRPORT-ISO_COUNTRRY!!! pitää olla "AS"
    print("Tähän random valinta Australia nro [3].")  # random.randrange(alku, loppu)
    print("Tähän random valinta Australia nro [4].")
    print("Tähän random valinta Australia nro [5].")

    valitseKentta = input("Valitse haluamasi lentokenttä: ")

    if valitseKentta == "1":
        print("Vaiheessa...")

    elif valitseKentta == "2":
        print("Vaiheessa...")

    elif valitseKentta == "3":
        print("Vaiheessa...")

    elif valitseKentta == "4":
        print("Vaiheessa...")

    elif valitseKentta == "5":
        print("Vaiheessa...")


def naKentta():
    print()
    print(
        "Tähän random valinta Pohjois-Amerikka nro [1].")  # kaikkiin kenttiin tarvitaan hakutoiminto, joka hakee tietokannasta
    print(
        "Tähän random valinta Pohjois-Amerikka nro [2].")  # satunnaisen kentän, jossa AIRPORT-CONTINENT pitää olla "NA"
    print("Tähän random valinta Pohjois-Amerikka nro [3].")  # random.randrange(alku, loppu)
    print("Tähän random valinta Pohjois-Amerikka nro [4].")
    print("Tähän random valinta Pohjois-Amerikka nro [5].")

    valitseKentta = input("Valitse haluamasi lentokenttä: ")

    if valitseKentta == "1":
        print("Vaiheessa...")

    elif valitseKentta == "2":
        print("Vaiheessa...")

    elif valitseKentta == "3":
        print("Vaiheessa...")

    elif valitseKentta == "4":
        print("Vaiheessa...")

    elif valitseKentta == "5":
        print("Vaiheessa...")


def saKentta():
    print()
    print(
        "Tähän random valinta Etelä-Amerikka nro [1].")  # kaikkiin kenttiin tarvitaan hakutoiminto, joka hakee tietokannasta
    print("Tähän random valinta Etelä-Amerikka nro [2].")  # satunnaisen kentän, jossa AIRPORT-CONTINENT pitää olla "SA"
    print("Tähän random valinta Etelä-Amerikka nro [3].")  # random.randrange(alku, loppu)
    print("Tähän random valinta Etelä-Amerikka nro [4].")
    print("Tähän random valinta Etelä-Amerikka nro [5].")

    valitseKentta = input("Valitse haluamasi lentokenttä: ")

    if valitseKentta == "1":
        print("Vaiheessa...")

    elif valitseKentta == "2":
        print("Vaiheessa...")

    elif valitseKentta == "3":
        print("Vaiheessa...")

    elif valitseKentta == "4":
        print("Vaiheessa...")

    elif valitseKentta == "5":
        print("Vaiheessa...")


def valinta():
    print("Tervetuloa Helsinki-Vantaan lentokentälle. Mille mantereelle haluaisit lentää seuraavaksi?")
    print(
        "[1] Aasia, [2] Eurooppa, [3] Afrikka, [4] Australia ,[5] Pohjois-Amerikka,[6] Etelä-Amerikka, [P] Palaa valikkoon, [Q] Lopeta peli")
    valitse = input("Valitse haluamasi toiminto: ")

    if valitse == "1":
        asKentta()

    elif valitse == "2":
        euKentta()

    elif valitse == "3":
        afKentta()

    elif valitse == "4":
        auKentta()

    elif valitse == "5":
        naKentta()

    elif valitse == "6":
        saKentta()

    elif valitse == "p" or valitse == "P":
        menu()

    elif valitse == "q" or valitse == "Q":
        sys.exit()

    else:
        print("Jokin meni pieleen, yritä uudelleen.")
        valinta()


def menu():
    print()
    print("Aloita uusi peli [U] \nOhjeet [O] \nLopeta peli [Q]\n")
    print()
    toiminto = input("Valitse vaihtoehto: ")

    if toiminto == "U" or toiminto == "u":
        valinta()

    elif toiminto == "P" or toiminto == "p":
        menu()

    elif toiminto == "O" or toiminto == "o":
        print()
        print(
            "Ohjeet: \nPelin tavoitteena on käydä jokaisella mantereella: Aasia , Afrikka, Australia, Etelä-Amerikka, Eurooppa, Pohjois-Amerikka.")
        print(
            "Aloitat pelin Helsinki-Vantaan lentokentältä, vaikka se sijaitseekin Euroopassa, sinun tulee käydä jossain toisessa Euroopan maassa.")
        print(
            "Peli tarjoaa sinulle ensiksi valittavaksi seuraavan mantereen ja satunnaisesti halutulta mantereelta viisi eri lentokenttää.")
        print(
            "Sinun tavoitteena on yrittää päästä mahdollisimman pienin päästöin peli lävitse. Pelin komennot ovat suluissa ja sinun tulee valita kirjain tai numero ja edetä sen jälkeen painamalla enteriä. ")
        print()
        menu()

    elif toiminto == "Q" or toiminto == "q":
        sys.exit()
    else:
        print("Jotain meni pieleen, yritä uudelleen.")
        menu()


def aloitus():  # syötä nimimerkin kohdalle toiminto joka vie
    aloitaPeli = input("[S]yötä nimimerkki, voit lopettaa pelin painamalla [Q]: ")  # nimimerkin tietokantaan
    # mitä jos nimimerkki on jo käytössä?
    if aloitaPeli == "S" or aloitaPeli == "s":  # luodaanko uusi id?
        input("Syötä käyttäjätunnus: ")
        print()
        menu()

    elif aloitaPeli == "Q" or aloitaPeli == "q":
        print("Lopetetaan peli...")
        sys.exit()

    else:
        print("Jotain meni pieleen, yritä uudelleen...")
        aloitus()
        if__name__=='__main__':
              main()