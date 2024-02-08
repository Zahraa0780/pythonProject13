pituus_cm = float(input("Syötä kuhan pituus senttimetreinä: "))
if pituus_cm < 37:
    puuttuvat_cm = 37 - pituus_cm
    print(f"Kuha on alamittainen. Puuttuvaa pituutta on {puuttuvat_cm:.2f} senttimetriä.")
else:
    print("Kuha on riittävän pitkä.")