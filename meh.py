import random
import time

#NIE BYŁO TESTOWANE
def pol_na_pol(pytanie):
    print("Pół na pół.\nCzy aby na pewno jest łatwiej?")
    print(pytanie[3], pytanie[5])
    print("Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")
    odpowiedz = input()
    if odpowiedź == pytanie[3]:
        print("Niestety, to nie jest poprawna odpowiedź")
    else:
        print("Gratulacje! Udało się Panu!")#tu musi być jeszcze przekierowanie do pytania


def telefon(pytanie):
    print("Zatem zadzwońmy do Twojego przyjaciela")
    for i in range (3):
        time.sleep(1)
        print(".")
    poprawne = random.random()
    if poprawne < 0.7:
        print("Konfucjusz uważa, że prawidłowa odpowiedź to: ", pytanie[5], "Czy zgadzasz się z nim?(T/N)")#i tu
        decyzja = input()
        if decyzja == "T":
            print("To prawidłowa odpowiedź!")#i tu
        else:
            print("Niestety nie udało się. To nie jest prawidłowa odpowiedź.")
    else:
        print("Konfucjusz uważa, że prawidłowa odpowiedź to: ", pytanie[2], "Czy zgadzasz się z nim?(T/N)")
        dec = input()
        if dec == "T":
            print("Konfucjusz nie miał racji.")
        else:#powrót do pytania



print("Czy chcesz skorzystać z koła ratunkowego?(T/N)") #to Piotrze pozmieniaj tak aby pasowało ci do banerów
kolo = input()
if kolo == "T":
    print("Które z kół chcesz wykorzystać?\nTelefon do przyjaciela(1)\nPół na pół(2)\nPytanie do publiczności(3)")
    odp = int(input())
    if odp == 1:
        telefon(pytanie)
    elif odp == 2:
        pol_na_pol(pytanie)
    #else: #tu pyt do publiczności
#else: #tu miało być przekierowanie do pytania ale mają być banery więc idk what to do
