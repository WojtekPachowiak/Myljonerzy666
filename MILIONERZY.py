# Myljonerzy666
########## MODUŁY ############
import random
import time
import os
import winsound
import pygame
from colorama import init
from colorama import Fore, Back, Style
from termcolor import colored
init()


from funkcje import *
from publicznosc import *
from kingakola import *

#### LOSOWE PYTANIA ##########
licznik_dobrych_odpowiedzi = 0


lista_easy = [
["Czym Chińczycy tradycyjnie jadają potrawy z ryżu?",
"A - łyżkami",
"B - wykałaczkami",
"C - widelcami",
"D - pałeczkami",
"D"],
["Jaka część mowy odpowiada na pytania: kto, co?",
"A - przymiotnik",
"B - czasonik",
"C - rzeczownik",
"D - przysłówek",
"C"],
["Kto ma łeb obdarty?",
"A - kto późno przychodzi",
"B - kto jest krótko ostrzyżony",
"C - kto gra w karty",
"D - kto ma nos zadarty",
"C"],
["Która z tych małp jest największa?",
"A - orangutan",
"B - kapucynka",
"C - szympans",
"D - goryl",
"D"],
["W jakim mieście jest Wawel?",
"A - we Wrocławiu",
"B - w Warszawie",
"C - w Poznaniu",
"D - w Krakowie",
"D"],
["Jakie są najwyższe góry na świecie?",
"A - Tatry",
"B - Himalaje",
"C - Pireneje",
"D - Alpy",
"B"],
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






lista_medium = [
["Kto wypowiedział słowa: \"Ja nie z soli ani z roli, ale z tego, co mnie boli\"?",
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
"B"],
["Gdzie leży Arktyka?",
"A - wokół bieguna południowego",
"B - wokół bieguna północnego",
"C - na równiku",
"D - na Księżycu",
"B"],
["Ile jest znaków zodiaku?",
"A - 12",
"B - 15",
"C - 16",
"D - 10",
"A"],
["Bohaterowie Jeziora Łabędziego Piotra Czajkowskiego to?",
"A - Odetta, Zygfryd, Wolfgang",
"B - Ludmiła, Rusłan, Igor",
"C - Rosa, Gaetano, Eusebio",
"D - Anna, Władysław, Jan",
"A"],
["W którym filmie Andrzeja Wajdy zobaczymy reżysera jako samego siebie?",
"A - W Tataraku",
"B - w Ziemi Obiecanej",
"C - W Człowieku z żelaza",
"D - W Powidokach",
"A"],
["Kto miał ustsza słodsze od malin?",
"A - Kasia Cichopek",
"B - Towarysz Stalin",
"C - Izabela Łęcka",
"D - Ewa Chodakowska",
"B"],]






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
"B"],
["Które z poniższych jest najliczniejsze",
"A - Fotodżoker",
"B - Multidżoker",
"C - Dżokerro",
"D - Minidżoker",
"B"],
["Co powiedział Zbigniew Stonoga w słynnej przemowie do narodu?",
"A - \"geje, tfu\"",
"B - \"We all live in a yellow submarine\"",
"C - \"Będzie was PiS ruchał w dupe\"",
"D - \"Kościół, szkoła, strzelnica\"",
"C"]]

#tutaj trafiają te pytania, które już zostały wylosowane ~ Piotr
lista_już_wylosowanych = []




################################################################################
# Stworzyłem klasę ~ Piotr
### Poniższe zmienne mówią nam, CZY KOŁO RATUNKOWE ZOSTAŁO WYKORZYSTANE, czy też NIE! ### ~ Piotr
class q():

    czy_1 = 0
    czy_2 = 0
    czy_3 = 0

    def __init__(self):
        self.czy_1 = 0
        self.czy_2 = 0
        self.czy_3 = 0

    def zwroc_czy_1(self):
        return self.czy_1

    def zwroc_czy_1(self):
        return self.czy_2

    def zwroc_czy_1(self):
        return self.czy_3

    def kola_ratunkowe(self,x,losowe):
        if x == '1' and self.czy_1 == 0:
            self.czy_1 = self.czy_1 + 1
            if licznik_dobrych_odpowiedzi <= 6:
                print("(Pytanie do publiczności!)")
                pytanie_do_publicznosci_easy(losowe)
            elif licznik_dobrych_odpowiedzi in range(7,9):
                print("(Pytanie do publiczności!)")
                pytanie_do_publicznosci_medium(losowe)
            elif licznik_dobrych_odpowiedzi in range(9,12):
                print("(Pytanie do publiczności!)")
                pytanie_do_publicznosci_hard(losowe)
            x = input(Hub + str("Cóż więc zaznaczamy? "))
            wynik = self.pytanie_huberta(x,losowe)
            return wynik

        if x == '1' and self.czy_1 == 1:
            print("(Wykorzystałeś już pytanie do publiczności!)")
            x = input(Hub + str("Cóż więc zaznaczamy? "))
            wynik = self.pytanie_huberta(x,losowe)
            return wynik


        if x == '2' and self.czy_2 == 0:
            self.czy_2 = self.czy_2 + 1
            print("(Telefon do przyjaciela!)")
            telefon(losowe)
            # [[[[[[[[TUTAJ WSTAWIĆ FUNKCJĘ TELEFON!]]]]]]]

            x = input(Hub + str("No to jaka jest prawidłowa odpowiedź? "))
            wynik = self.pytanie_huberta(x,losowe)
            return wynik
        if x == '2' and self.czy_2 == 1:
            print("(Wykorzystałeś już telefon do przyjaciela!)")
            x = input(Hub + str("A więc, którą odpowiedź zaznaczasz? "))
            wynik = self.pytanie_huberta(x,losowe)
            return wynik


        if x == '3' and self.czy_3 == 0:
            self.czy_3 = self.czy_3 + 1
            print("(Pół na pół!)")
            pol_na_pol(losowe)
            x = input(Hub + str("No to jaka jest prawidłowa odpowiedź? "))
            wynik = self.pytanie_huberta(x,losowe)
            return wynik
        if x == '3' and self.czy_3 == 1:
            print("(Wykorzystałeś już pół na pół!)")
            x = input(Hub + str("A więc, którą odpowiedź zaznaczasz? "))
            wynik = self.pytanie_huberta(x,losowe)
            return wynik


    def pytanie_huberta(self,x,pytanie):
        if x == 'A' or x == 'B' or x == 'C' or x == 'D':
            prawdopodobienstwo = random.randint(0,10)
            if licznik_dobrych_odpowiedzi == 11:
                pytanie = str(input(Hub + str("To jest pytanie o MILION. \nCzy definitywnie to jest Twoja odpowiedź 'T/'N'?")))
                if pytanie == "T" or pytanie == "t":
                    return x
                else:
                    x = input(Hub + str("Która odpowiedź jest więc prawidłowa?"))
                    return x
            elif prawdopodobienstwo <= 5:
                pytanie = str(input(Hub + str("Definitywnie 'T/'N'?")))
                if pytanie == "T" or pytanie == "t":
                    return x
                else:
                    x = input(Hub + str("No to jaka jest prawidłowa odpowiedź? "))
                    return x
            else:
                return x
        elif x == '1' or x =='2' or x == '3':
            wynik = self.kola_ratunkowe(x,pytanie)
            return wynik
################################################################################
        else:
            while True:
                teksty_huberta = "Jaka więc jest poprawna odpowiedź?","Hmmm, a więc co zechcesz zaznaczyć?","No to która?","Którą zaznaczamy?"
                los = random.choice(teksty_huberta)
                x = input(Hub + los + str(" "))
                if x == 'A' or x == 'B' or x == 'C' or x == 'D':
                    return x
                elif x == '1' or x =='2' or x == '3':
                    wynik = self.kola_ratunkowe(x,pytanie)
                    return wynik
que = q() #Uruchamiam klasę.


def utwor(y):
    if y == 0:
        pygame.mixer.init()
        pygame.mixer.music.load('tlo.mp3')
        pygame.mixer.music.play(999)
    if y == 7:
        pygame.mixer.init()
        pygame.mixer.music.load('tlo2.mp3')
        pygame.mixer.music.play(999)
    if y == 11:
        pygame.mixer.init()
        pygame.mixer.music.load('tlo3.mp3')
        pygame.mixer.music.play(999)
    if y == 12:
        pygame.mixer.init()
        pygame.mixer.music.load('intro.mp3')
        pygame.mixer.music.play(999)

####### W TYM MIEJSCU ODPALAM MUZYKĘ ORAZ ŁADUJĘ INTRO I POWITANIE! ###########


pygame.mixer.init()
pygame.mixer.music.load('intro.mp3')
pygame.mixer.music.play(999)
#winsound.PlaySound("intro.wav",  winsound.SND_ALIAS | winsound.SND_ASYNC)

intro()
os.system('cls')
start = input() #to musi tutaj być ~~ Piotr
witaj()
Hub = colored("         Hubert: ","yellow")

###############################################################################


while True:
    ###### PYTANIA LOSOWANE Z LISTY ŁATWYCH ###### ~ Piotr
    utwor(licznik_dobrych_odpowiedzi)
    if licznik_dobrych_odpowiedzi <= 6:
        losowe_pytanie = random.choice(lista_easy)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            baner()
            print()

            o_ile_gram(licznik_dobrych_odpowiedzi)
            for i in range(0,len(losowe_pytanie)-1):
                if i == 0:
                    print(losowe_pytanie[i])
                    print()
                else:
                    print(losowe_pytanie[i])
            print()

            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = que.pytanie_huberta(odp,losowe_pytanie)

            if odpowiedz_uczestnika == losowe_pytanie[5]:
                        licznik_dobrych_odpowiedzi +=1
                        dobrze()
                        time.sleep(2)
                        os.system('cls')
            else:
                przegrales()
                break
                print("")



    ###### PYTANIE LOSOWANE Z LISTY ŚREDNICH ###### ~ Piotr
    elif licznik_dobrych_odpowiedzi in range(7,9):
        losowe_pytanie = random.choice(lista_medium)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            baner()
            print()
            o_ile_gram(licznik_dobrych_odpowiedzi)
            for i in range(0,len(losowe_pytanie)-1):
                if i == 0:
                    print(losowe_pytanie[i])
                    print()
                else:
                    print(losowe_pytanie[i])
            print()

            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = que.pytanie_huberta(odp,losowe_pytanie)

            if odpowiedz_uczestnika == losowe_pytanie[5]:
                        licznik_dobrych_odpowiedzi +=1
                        dobrze()
                        time.sleep(2)
                        os.system('cls')
            else:
                przegrales()
                break
                print("")



    ###### PYTANIE LOSOWANE Z LISTY TRUDNYCH ###### ~ Piotr
    elif licznik_dobrych_odpowiedzi in range(9,12):
        losowe_pytanie = random.choice(lista_hard)
        if losowe_pytanie not in lista_już_wylosowanych:
            lista_już_wylosowanych.append(losowe_pytanie)
            baner()
            print()
            o_ile_gram(licznik_dobrych_odpowiedzi)
            for i in range(0,len(losowe_pytanie)-1):
                if i == 0:
                    print(losowe_pytanie[i])
                    print()
                else:
                    print(losowe_pytanie[i])
            print()

            odp = input("Podaj prawidłową odpowiedź: ")
            odpowiedz_uczestnika = que.pytanie_huberta(odp,losowe_pytanie)

            if odpowiedz_uczestnika == losowe_pytanie[5]:
                        licznik_dobrych_odpowiedzi +=1
                        dobrze()
                        time.sleep(2)
                        os.system('cls')
            else:
                przegrales()
                break
                print("")

    if licznik_dobrych_odpowiedzi == 12:
        utwor(licznik_dobrych_odpowiedzi)
        wygrales()
        ok = input()
        break



#####       http://testwiedzy.pl/print/print_test/29791.html      #######
