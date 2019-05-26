import random

###################PRZYKŁADOWE PYTANIE###############
x = ["pytanie1","A","B","C","D","D"]





############ŁATWE PYTANIE########################

def pytanie_do_publicznosci_easy(losowe_pytanie):

    lista_mozliwych_odpowiedzi = [x[1],x[2],x[3],x[4]]

    for i in lista_mozliwych_odpowiedzi:
        if i is x[5]:
            lista_mozliwych_odpowiedzi.remove(i)
            break

    procent_odp1 = 0
    procent_odp2 = 0
    szansa_dobrej_podpowiedzi_od_publicznosci = random.random()

    if szansa_dobrej_podpowiedzi_od_publicznosci <= 0.75:
        procent_dobra_odp = random.randint(50,80)
    else:
        procent_dobra_odp = random.randint(0,49)

    procent_odp1 = random.randint(0,100 - procent_dobra_odp)
    zakres_procent_odp2 = 100 - procent_dobra_odp - procent_odp1
    procent_odp2 = random.randint(0,zakres_procent_odp2)
    procent_odp3 = 100 - procent_dobra_odp - procent_odp1 - procent_odp2



    print(losowe_pytanie[5],"-",procent_dobra_odp , "%")

    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp1,"%")


    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp2,"%")


    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp3,"%")




#pytanie_do_publicznosci_easy(x)

############ŚREDNIE PYTANIE########################

def pytanie_do_publicznosci_medium(losowe_pytanie):

    lista_mozliwych_odpowiedzi = [x[1],x[2],x[3],x[4]]

    for i in lista_mozliwych_odpowiedzi:
        if i is x[5]:
            lista_mozliwych_odpowiedzi.remove(i)
            break
    procent_odp1 = 0
    procent_odp2 = 0
    szansa_dobrej_podpowiedzi_od_publicznosci = random.random()

    if szansa_dobrej_podpowiedzi_od_publicznosci <= 0.50:
        procent_dobra_odp = random.randint(50,80)
    else:
        procent_dobra_odp = random.randint(0,49)

    procent_odp1 = random.randint(0,100 - procent_dobra_odp)
    zakres_procent_odp2 = 100 - procent_dobra_odp - procent_odp1
    procent_odp2 = random.randint(0,zakres_procent_odp2)
    procent_odp3 = 100 - procent_dobra_odp - procent_odp1 - procent_odp2



    print(losowe_pytanie[5],"-",procent_dobra_odp , "%")

    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp1,"%")


    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp2,"%")


    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp3,"%")






############TRUDNE PYTANIE########################



def pytanie_do_publicznosci_hard(losowe_pytanie):
    lista_mozliwych_odpowiedzi = [x[1],x[2],x[3],x[4]]

    for i in lista_mozliwych_odpowiedzi:
        if i is x[5]:
            lista_mozliwych_odpowiedzi.remove(i)
            break

    procent_odp1 = 0
    procent_odp2 = 0
    szansa_dobrej_podpowiedzi_od_publicznosci = random.random()

    if szansa_dobrej_podpowiedzi_od_publicznosci <= 0.25:
        procent_dobra_odp = random.randint(50,80)
    else:
        procent_dobra_odp = random.randint(0,49)

    procent_odp1 = random.randint(0,100 - procent_dobra_odp)
    zakres_procent_odp2 = 100 - procent_dobra_odp - procent_odp1
    procent_odp2 = random.randint(0,zakres_procent_odp2)
    procent_odp3 = 100 - procent_dobra_odp - procent_odp1 - procent_odp2



    print(losowe_pytanie[5],"-",procent_dobra_odp , "%")

    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp1,"%")


    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp2,"%")


    zmienna = random.choice(lista_mozliwych_odpowiedzi)
    lista_mozliwych_odpowiedzi.remove(zmienna)
    print(zmienna,"-",procent_odp3,"%")
