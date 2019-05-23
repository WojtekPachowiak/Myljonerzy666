# Myljonerzy666
########## MODUŁY ############
import random
import time
import os
#### LOSOWE PYTANIA ##########
licznik_dobrych_odpowiedzi = 0


lista_easy = [["Czym Chińczycy tradycyjnie jadają potrawy z ryżu?",
"A - łyżkami",
"B - wykałaczkami",
"C - widelcami",
"D - pałeczkami",
"D"],
["Ile miesięcy liczy kwartał?",
"A - 2",
"B - 3",
"C - 4",
"D - 5",
"B"],
["11 listopada to rocznica:",
"A - odzyskania niepodległości",
"B - wybuchu I wojny światowej",
"C - uchwalenia konstytucji",
"D - powstania listopadowego",
"A"],
["Woda to tlenek:",
"A - węgla",
"B - srebra",
"C - żelaza",
"D - wodoru",
"D"],
["Międzynarodowa organizacja policyjna ścigająca przestępstwa kryminalne to:",
"A - Mosad",
"B - Czeka",
"C - Interpol",
"D - Secret Service",
"C"],
["Które z określeń nie oznacza wysłannika?",
"A - Werona",
"B - Wenecja",
"C - Florencja",
"D - Palermo",
"D"],
["Jakie włoskie miasto było tłem burzliwego i tragicznego w skutkach romansu Romea i Julii?",
"A - Werona",
"B - Wenecja",
"C - Florencja",
"D - Palermo",
"A"],
["Kto wypowiedział słynne słowa: \"to mały krok dla człowieka, ale wielki skok dla ludzkości\"?",
"A - kosmonauta na księżycu",
"B - laureat nagrody nobla",
"C - genetyk, który sklonował owcę",
"D - konstruktor pierwszego komputera",
"A"]]


lista_medium = [["Kto wypowiedział słowa: \"Ja nie z soli ani z roli, ale z tego, co mnie boli\"?",
"A - Jan III Sobieski",
"B - Bartosz Głowacki",
"C - Stefan Czarniecki",
"D - Józef Piłsudzki",
"C"],
["Pytanie za 32 000 zł: Wafel pieczony z delikatnego ciasta w specjalnych foremkach to:",
"A - bajgiel",
"B - andrut",
"C - bakława",
"D - beza",
"B"]]

lista_hard = [["Wysoka czapka futrzana noszona wWielkiej Brytanii przez reprezentacyjne oddziały gwardii to:",
"A - kołpak",
"B - tiara",
"C - papacha",
"D - bermyca",
"D"],
["Gdzie produkowany jest od 1835 roku włoski wermut Cinzano (rodzaj wina)?",
"A - w Turynie",
"B - w Wenecji",
"C - w Mediolanie",
"D - we Florencji",
"A"],
["Który z podanych instrumentów nie należy do grupy aerofonów?",
"A - obój",
"B - tuba",
"C - dudy",
"D - żele",
"D"],
["Jak nazywa się amerykańska baza wojskowa na Kubie?",
"A - Santa Clara",
"B - Bayamo",
"C - Guantanamo",
"D - Matanzas",
"C"],
["Z jakimi plemionami Indian walczył generał Custer nad Little Big Horn?",
"A - Czirokezami i Seminolami",
"B - Sjuksami i Szejenami",
"C - Szoszonami i Wronami",
"D - Huronami i Mohikanami",
"B"]]

 #tutaj trafiają te pytania, które już zostały wylosowane ~ Piotr
lista_już_wylosowanych = []


#ta funkcja wyświetla odpowiedni napis w zależności od stanu licznik dobrych odpowiedzi! ~ Piotr
def o_ile_gram():
    if licznik_dobrych_odpowiedzi == 0:
        print("Grasz o 500zł!\n")
    if licznik_dobrych_odpowiedzi == 1:
        print("Grasz o 1000zł!\n")
    if licznik_dobrych_odpowiedzi == 2:
        print("Grasz o 2000zł!\n")
    if licznik_dobrych_odpowiedzi == 3:
        print("Grasz o 5000zł!\n")
    if licznik_dobrych_odpowiedzi == 4:
        print("Grasz o 10 000zł!\n")
    if licznik_dobrych_odpowiedzi == 5:
        print("Grasz o 20 000zł!\n")
    if licznik_dobrych_odpowiedzi == 6:
        print("Grasz o 40 000zł!\n")
    if licznik_dobrych_odpowiedzi == 7:
        print("Grasz o 75 000zł!\n")
    if licznik_dobrych_odpowiedzi == 8:
        print("Grasz o 125 000zł!\n")
    if licznik_dobrych_odpowiedzi == 9:
        print("Grasz o 250 000zł!\n")
    if licznik_dobrych_odpowiedzi == 10:
        print("Grasz o 500 000zł\n!")
    if licznik_dobrych_odpowiedzi == 11:
        print("Grasz o MILION!\n")

def pytanie_huberta(x):
    prawdopodobienstwo = random.randint(0,10)
    if licznik_dobrych_odpowiedzi == 11:
        pytanie = str(input("Hubert: To jest pytanie o MILION. \nDefinitywnie to jest Twoja odpowiedź 'T/'N'?"))
        if pytanie == "T" or pytanie == "t":
            return x
        else:
            y = input("Hubert: Która odpowiedź jest wiec prawidłowa? ")
            return y
    elif prawdopodobienstwo <= 5:
        pytanie = str(input("Hubert: Definitywnie 'T/'N'?"))
        if pytanie == "T" or pytanie == "t":
            return x
        else:
            y = input("Hubert: No to jaka jest prawidłowa odpowiedź? ")
            return y
    else:
        return x


while True:
    ###### PYTANIA LOSOWANE Z LISTY ŁATWYCH ###### ~ Piotr
    if licznik_dobrych_odpowiedzi <= 6:
        losowe_pytanie = random.choice(lista_easy)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            o_ile_gram()
            for i in losowe_pytanie[0:5]:
                print(i)

            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = pytanie_huberta(odp)

            if odpowiedz_uczestnika == losowe_pytanie[5]:
                        licznik_dobrych_odpowiedzi +=1
                        print("Dobra odpowiedź!\n")
                        print(licznik_dobrych_odpowiedzi)
                        time.sleep(2)
                        os.system('cls')
            else:
                print("Zła odpowiedź. Przegrałeś")
                break
                print("")


    ###### PYTANIE LOSOWANE Z LISTY ŚREDNICH ###### ~ Piotr
    elif licznik_dobrych_odpowiedzi in range(7,9):
        losowe_pytanie = random.choice(lista_medium)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            for i in losowe_pytanie[0:5]:
                print(i)

            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = pytanie_huberta(odp)

            if odpowiedz_uczestnika == losowe_pytanie[5]:
                        licznik_dobrych_odpowiedzi +=1
                        print("Dobra odpowiedź!\n")
                        print(licznik_dobrych_odpowiedzi)
                        time.sleep(2)
                        os.system('cls')
            else:
                print("Zła odpowiedź. Przegrałeś")
                break
                print("")


    ###### PYTANIE LOSOWANE Z LISTY TRUDNYCH ###### ~ Piotr
    elif licznik_dobrych_odpowiedzi in range(9,12):
        losowe_pytanie = random.choice(lista_hard)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            for i in losowe_pytanie[0:5]:
                print(i)
            print("")

            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = pytanie_huberta(odp)

            if odpowiedz_uczestnika == losowe_pytanie[5]:
                        licznik_dobrych_odpowiedzi +=1
                        print("Dobra odpowiedź!\n")
                        print(licznik_dobrych_odpowiedzi)
                        time.sleep(2)
                        os.system('cls')
            else:
                print("Zła odpowiedź. Przegrałeś")
                break
                print("")



    if licznik_dobrych_odpowiedzi == 12:
        print("Brawo! Wygrałeś MILION ZŁOTYCH!")
        break


#####       http://testwiedzy.pl/print/print_test/29791.html      #######
