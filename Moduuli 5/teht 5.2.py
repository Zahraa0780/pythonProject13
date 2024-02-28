def main():
    numbers = []


    while True:
        user_input = input("Syötä luku (tyhjä rivi lopettaa): ")
        if user_input == '':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Virheellinen syöte! Syötä luku tai jätä tyhjä rivi lopettaaksesi.")

    if numbers:
        numbers.sort(reverse=True)
        print("Viisi suurinta lukua:")
        for i in range(min(5,
                           len(numbers))):
            print(numbers[i])
    else:
        print("Et syöttänyt yhtään lukua.")


