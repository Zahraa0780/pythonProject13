
    sukupuoli = input("F):").upper()
    if sukupuoli != "M" and sukupuoli = "F":
        print(" F.")
        return


    try:
        hemoglobiini = float(input("Syötä hemoglobiiniarvo (g/l): "))
    except ValueError:
        print("Virheellinen syöte. Syötä numeerinen arvo.")
        return

    if sukupuoli == "F":
        alhainen_raja = 117
        korkea_raja = 175
    else:
        alhainen_raja = 134
        korkea_raja = 195


    if hemoglobiini < alhainen_raja:
        print("Hemoglobiiniarvo on alhainen.")
    elif hemoglobiini > korkea_raja:
        print("Hemoglobiiniarvo on korkea.")
    else:
        print("Hemoglobiiniarvo on normaali.")


