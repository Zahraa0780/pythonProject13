def määritä_vuodenaika(kuukausi):
    vuodenajat = {
        "kevät": (3, 4, 5),
        "kesä": (6, 7, 8),
        "syksy": (9, 10, 11),
        "talvi": (12, 1, 2)
    }

    for vuodenaika, kuukaudet in vuodenajat.items():
        if kuukausi in kuukaudet:
            return vuodenaika
    return "Tuntematon kuukausi"

def main():
    kuukausi = int(input("Syötä kuukauden numero (1-12): "))
    vuodenaika = määritä_vuodenaika(kuukausi)
    print(f"Kuukauden {kuukausi} vuodenaika on {vuodenaika}.")
