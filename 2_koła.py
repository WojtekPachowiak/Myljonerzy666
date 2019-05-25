import random
import time

#NIE BYŁO TESTOWANE
#porównuje ostatnią (właściwą) literkę i porównuje z odpowiedziami, szukając właściweej, poźniej gracz wpisuje jedna z 2 wyswietlonych odp,
#jeśli jest prawidłowa to gra dalej(także później trzeba dodać przekierowanie do dalszej rozgrywki) jeśli nie to(nie wiem, koniec programu??)
def pol_na_pol(pytanie):
    print(Hu, "Pół na pół.\nCzy aby na pewno jest łatwiej?")
    if pytanie[5] == 'A': 
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[1], pytanie[3])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?") 
        odpowiedz = input()
        if odpowiedz == 'A':
            print(Hu, "Tak, A jest prawidłową odpowiedzią!")
        else:
            print(Hu, "Niestety, nie udało się. :(")        
    elif pytanie[5] == 'B':
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[2], pytanie[4])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")
        odpowiedz = input()
        if odpowiedz == 'B':
            print(Hu, "Dokładnie tak! B to prawidłowa odpowiedź!")
        else:
            print(Hu, "Pańska droga do miliona się zakończyła. ")            
    elif pytanie[5] == 'C':
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[3], pytanie[2])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")
        odpowiedz = input()
        if odpowiedz == 'C':
            print(Hu, "Doskonale!")
        else:
            print(Hu, "Nie, to nie jest prawidłowa odpowiedź.")            
    elif pytanie[5] == 'D':
        print(Hu, "Pozostałe odpowiedzi to:", pytanie[4], pytanie[1])
        print(Hu, "Tylko, która z tych dwóch odpowiedzi jest prawidłowa?")
        odpowiedz = input()
        if odpowiedz == 'D':
            print(Hu, "Gratulacje! Mądrze Pan wybrał!")
        else:
            print(Hu, "No cóż, nie udało się.")

#to jeszcze do przerobienia
def telefon(pytanie):
    print("Zatem zadzwońmy do Twojego przyjaciela")
    for i in range (3):
        time.sleep(1)
        print(".")
    poprawne = random.random()
    if poprawne < 0.7:
        print("Konfucjusz uważa, że prawidłowa odpowiedź to: ", pytanie[5], "Czy zgadzasz się z nim?(T/N)")#i tu #tu też dam pętle wait for it
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
