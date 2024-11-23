correcte_getallen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




#    print(ontbrekend_getal([2, 3, 4, 5, 6, 7, 8, 9, 10]))   # 1
#    print(ontbrekend_getal([5, 3, 8, 9, 10, 4, 1, 6, 7]))   # 2
#    print(ontbrekend_getal([7, 2, 3, 6, 5, 9, 1, 4, 8]))    # 10
#    print(ontbrekend_getal([10, 5, 1, 2, 4, 6, 8, 3, 9]))   # 7

lijst_1 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
lijst_2 = [5, 3, 8, 9, 10, 4, 1, 6, 7]
def missend_nummer(lijst):
    for cijfer in correcte_getallen:
        if cijfer not in lijst:
            print(cijfer)

missend_nummer(lijst_1)