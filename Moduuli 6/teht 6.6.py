import math

def laske_yksikkohinta(halkaisija_cm, hinta_eur):
    säde_m = halkaisija_cm / 200
    pinta_ala_m2 = math.pi * säde_m ** 2
    yksikkohinta_eur_m2 = hinta_eur / pinta_ala_m2
    return yksikkohinta_eur_m2

def main():

    halkaisija1 = float(input("Syötä ensimmäisen pizzan halkaisija (cm): "))
    hinta1 = float(input("Syötä ensimmäisen pizzan hinta (€): "))


    halkaisija2 = float(input("Syötä toisen pizzan halkaisija (cm): "))
    hinta2 = float(input("Syötä toisen pizzan hinta (€): "))

   
    yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
    yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

    # Vertaillaan ja tulostetaan parempi vaihtoehto
    if yksikkohinta1 < yksikkohinta2:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikkohinta2 < yksikkohinta1:
        print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizzat antavat saman vastineen rahalle.")

if __name__ == "__main__":
    main()
