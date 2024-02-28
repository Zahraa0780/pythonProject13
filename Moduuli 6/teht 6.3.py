def gallonat_litroiksi(gallona_maara):
    litra_maara = gallona_maara * 3.785
    return litra_maara

def main():
    while True:
        gallona_maara = float(input("Syötä bensiinin määrä gallonoina (negatiivinen lopettaa ohjelman): "))
        if gallona_maara < 0:
            print("Ohjelma lopetetaan.")
            break
        litra_maara = gallonat_litroiksi(gallona_maara)
        print(f"{gallona_maara} gallonaa on {litra_maara:.2f} litraa.")

