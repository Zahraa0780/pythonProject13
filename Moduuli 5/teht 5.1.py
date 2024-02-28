import random


def main():
    try:
        num_dice = int(input("Syötä arpakuutioiden lukumäärä: "))
        if num_dice < 1:
            raise ValueError("Arpakuutioiden lukumäärän tulee olla vähintään 1.")

        total_sum = 0

        for _ in range(num_dice):
            roll = random.randint(1, 6)  # Arvotaan silmäluku 1-6
            total_sum += roll

        print("Arvottujen arpakuutioiden silmälukujen summa:", total_sum)

    except ValueError as e:
        print("Virheellinen syöte:", e)


