lentoasemat = {}

def lisaa_lentoasema():
    icao_koodi = input("Syötä lentoaseman ICAO-koodi: ").strip().upper()
    nimi = input("Syötä lentoaseman nimi: ").strip()
    lentoasemat[icao_koodi] = nimi
    print(f"Lentoasema {nimi} lisätty ICAO-koodilla {icao_koodi}.")

def hae_lentoasema():
    icao_koodi = input("Syötä haettavan lentoaseman ICAO-koodi: ").strip().upper()
    if icao_koodi in lentoasemat:
        print(f"Lentoaseman nimi: {lentoasemat[icao_koodi]}")
    else:
        print("Lentoasemaa ei löytynyt annetulla ICAO-koodilla.")

def main():
    while True:
        print("\nValitse toiminto:")
        print
