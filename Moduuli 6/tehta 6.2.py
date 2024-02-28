import random

def heita_noppaa(tahkojen_maara):
    return random.randint(1, tahkojen_maara)

def main():
    maksimisilmaluku = int(input("Syötä nopan maksimisilmäluku: "))
    while True:
        silmaluku = heita_noppaa(maksimisilmaluku)
        print("Heitto:", silmaluku)
        if silmaluku == maksimisilmaluku:
            print("Sait maksimisilmäluvun! Heitto lopetetaan.")
            break

