def main():
    syotetyt_nimet = set()

    while True:
        nimi = input("Syötä nimi(tyhjä lopettaa): ")
        if not nimi:
            break

        if nimi in syotetyt_nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi")
            syotetyt_nimet.add(nimi)

    print("\nSyötit seuraavat nimet:")
    for nimi in syotetyt_nimet:
        print(nimi)

