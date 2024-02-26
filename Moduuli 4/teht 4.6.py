import random

def laske_pi(arvottavien_pisteiden_maara):
    n = 0

    for _ in range(arvottavien_pisteiden_maara):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            n += 1

    pi_likiarvo = 4 * n / arvottavien_pisteiden_maara
    return pi_likiarvo

def main():
    while True:
        try:
            arvottavien_pisteiden_maara = int(input("Syötä arvottavien pisteiden määrä: "))
            if arvottavien_pisteiden_maara <= 0:
                raise ValueError
            break
        except ValueError:
            print("Syötteen tulee olla positiivinen kokonaisluku.")

    pi_likiarvo = laske_pi(arvottavien_pisteiden_maara)
    print(f"Piin likiarvo arvotuilla pisteillä on noin {pi_likiarvo}.")






