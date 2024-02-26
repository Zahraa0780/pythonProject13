def main():
    while True:
        tuumat = float(input("Syötä tuumamäärä (negatiivinen luku lopettaa): "))

        if tuumat < 0:
            print("Ohjelma lopetetaan.")
            break

        senttimetrit = tuumat * 2.54
        print(f"{tuumat} tuumaa on {senttimetrit:.2f} senttimetriä.")



