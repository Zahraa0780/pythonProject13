def main():
    correct_username = "python"
    correct_password = "rules"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        username = input("Syötä käyttäjätunnus: ")
        password = input("Syötä salasana: ")

        if username == correct_username and password == correct_password:
            print("Tervetuloa!")
            break
        else:
            print("Väärä käyttäjätunnus tai salasana. Yritä uudelleen.")
            attempts += 1

    if attempts == max_attempts:
        print("Pääsy evätty.")




