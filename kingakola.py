import random
import time
from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style
init()
#NIE BYŁO TESTOWANE
#porównuje ostatnią (właściwą) literkę i porównuje z odpowiedziami, szukając właściweej, poźniej gracz wpisuje jedna z 2 wyswietlonych odp,
#jeśli jest prawidłowa to gra dalej(także później trzeba dodać przekierowanie do dalszej rozgrywki) jeśli nie to(nie wiem, koniec programu??)
def pol_na_pol(pytanie):
    Hu = colored("Hubert","yellow")
    print(Hu, "Pół na pół.\nCzy aby na pewno jest łatwiej?")
    if pytanie[5] == 'A':
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[1], pytanie[3])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")

    elif pytanie[5] == 'B':
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[2], pytanie[4])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")

    elif pytanie[5] == 'C':
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[3], pytanie[2])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")

    elif pytanie[5] == 'D':
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[4], pytanie[1])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")


#to jeszcze do przerobienia
def telefon(pytanie):
    print("     Zatem zadzwońmy do Twojego przyjaciela")
    for i in range (3):
        time.sleep(1)
        print("     .    ",end = '')
    poprawne = random.random()
    if poprawne < 0.7:
        print("     \nKonfucjusz uważa, że prawidłowa odpowiedź to: ", pytanie[5])#i tu #tu też dam pętle wait for it)
    else:
        print("     \nKonfucjusz uważa, że prawidłowa odpowiedź to: ", pytanie[2],)





#print("Czy chcesz skorzystać z koła ratunkowego?(T/N)") #to Piotrze pozmieniaj tak aby pasowało ci do banerów
#kolo = input()
#if kolo == "T":
#    print("Które z kół chcesz wykorzystać?\nTelefon do przyjaciela(1)\nPół na pół(2)\nPytanie do publiczności(3)")
#    odp = int(input())
#    if odp == 1:
#        telefon(pytanie)
#    elif odp == 2:
#        pol_na_pol(pytanie)
    #else: #tu pyt do publiczności
