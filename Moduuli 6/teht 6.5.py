def karsi_parittomat(lista):
    karsittu_lista = [x for x in lista if x % 2 == 0]
    return karsittu_lista


def main():
    alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu = karsi_parittomat(alkuperainen_lista)

    print("Alkuperäinen lista:", alkuperainen_lista)
    print("Karsittu lista (ilman parittomia lukuja):", karsittu)



