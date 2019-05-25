# Myljonerzy666
########## MODUŁY ############
import random
import time
import os
import winsound
from funkcje import *
import pygame
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
["Wafel pieczony z delikatnego ciasta w specjalnych foremkach to:",
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




def pytanie_huberta(x):
    prawdopodobienstwo = random.randint(0,10)
    if licznik_dobrych_odpowiedzi == 11:
        pytanie = str(input("Hubert: To jest pytanie o MILION. \nCzy definitywnie to jest Twoja odpowiedź 'T/'N'?"))
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




gramy_dalej = ""


while True:

    ###### PYTANIA LOSOWANE Z LISTY ŁATWYCH ###### ~ Piotr



    if licznik_dobrych_odpowiedzi <= 6:

        if licznik_dobrych_odpowiedzi >= 2:
            gramy_dalej = input("Hubert: Masz zagwarantowane 1000zł. Czy gramy dalej? 'T/'N'?")
            if gramy_dalej == "T" or gramy_dalej == "t":
                 print("Hubert: OK! Następne pytanie...")
                 pass

            elif gramy_dalej == "N" or gramy_dalej == "n":
                print("Hubert: No to nie! Wracasz do domu z zagwarantowanym 1000zł!")
                break

        losowe_pytanie = random.choice(lista_easy)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            o_ile_gram(licznik_dobrych_odpowiedzi)
            for i in losowe_pytanie[0:5]:
                print(i)


            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = pytanie_huberta(odp)

            if odpowiedz_uczestnika == losowe_pytanie[5] or odpowiedz_uczestnika == losowe_pytanie[5].lower():
                        licznik_dobrych_odpowiedzi +=1
                        print("Dobra odpowiedź!\n")
                        time.sleep(2)
                        os.system('cls')
            else:
                if licznik_dobrych_odpowiedzi < 2:
                    print("Zła odpowiedź. Przegrałeś")
                elif licznik_dobrych_odpowiedzi >= 2:
                    print("Zła odpowiedź. Przegrałeś, ale wracasz do domu z zagwarantowanym 1000zł")
                break
                print("")



    ###### PYTANIE LOSOWANE Z LISTY ŚREDNICH ###### ~ Piotr
    elif licznik_dobrych_odpowiedzi in range(7,9):
        gramy_dalej = input("Hubert: Masz zagwarantowane 40000zł. Czy gramy dalej? 'T/'N'?")
        if gramy_dalej == "T" or gramy_dalej == "t":
             print("Hubert: OK! Następne pytanie...")
             pass

        elif gramy_dalej == "N" or gramy_dalej == "n":
            print("Hubert: No to nie! Wracasz do domu z zagwarantowanym 40000zł!")
            break

        losowe_pytanie = random.choice(lista_medium)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            for i in losowe_pytanie[0:5]:
                print(i)


            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = pytanie_huberta(odp)

            if odpowiedz_uczestnika == losowe_pytanie[5] or odpowiedz_uczestnika == losowe_pytanie[5].lower():
                        licznik_dobrych_odpowiedzi +=1
                        print("Dobra odpowiedź!\n")
                        time.sleep(2)
                        os.system('cls')
            else:
                print("Zła odpowiedź. Przegrałeś, ale wracasz do domu z zagwarantowanym 40000zł")
                break
                print("")



    ###### PYTANIE LOSOWANE Z LISTY TRUDNYCH ###### ~ Piotr

    elif licznik_dobrych_odpowiedzi in range(9,12):
        gramy_dalej = input("Hubert: Masz zagwarantowane 40000zł. Czy gramy dalej? 'T/'N'?")
        if gramy_dalej == "T" or gramy_dalej == "t":
             print("Hubert: OK! Następne pytanie...")
             pass

        elif gramy_dalej == "N" or gramy_dalej == "n":
            print("Hubert: No to nie! Wracasz do domu z zagwarantowanym 40000zł!")
            break

        losowe_pytanie = random.choice(lista_hard)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            for i in losowe_pytanie[0:5]:
                print(i)
            print("")

            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = pytanie_huberta(odp)

            if odpowiedz_uczestnika == losowe_pytanie[5] or odpowiedz_uczestnika == losowe_pytanie[5].lower():
                        licznik_dobrych_odpowiedzi +=1
                        print("Dobra odpowiedź!\n")
                        time.sleep(2)
                        os.system('cls')
            else:
                if licznik_dobrych_odpowiedzi < 12:
                    print("Zła odpowiedź. Przegrałeś, ale wracasz do domu z zagwarantowanym 40000zł")
                break
                print("")

    if licznik_dobrych_odpowiedzi == 12:
        print("Brawo! Wygrałeś MILION ZŁOTYCH!")
        break



#####       http://testwiedzy.pl/print/print_test/29791.html      #######
