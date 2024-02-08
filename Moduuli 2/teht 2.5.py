leiviskat = float(input("Anna leiviskät 20: "))
naulat = float(input("Anna naulat 32: "))
luodit = float(input("Anna luodit 1000: "))

kokonaismassa_kg = leiviskat * 20 * 32 * 13.3 / 1000  # 1 leiviska = 20 naulaa, 1 naula = 32 luotia, 1 luoti = 13.3 grammaa
kokonaismassa_g = kokonaismassa_kg * 1000
kokonaismassa_kg = int(kokonaismassa_kg)
kokonaismassa_g = round((kokonaismassa_g - kokonaismassa_kg * 1000), 2)

print("Massa nykymittojen mukaan:")
print(f"{kokonaismassa_kg} kilogrammaa ja {kokonaismassa_g} grammaa.")