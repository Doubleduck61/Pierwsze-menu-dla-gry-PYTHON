#dorobić funkcje

x=int(0)
while x==0:
    print("MENU\n")
    print("[1] NOWA GRA")
    print("[2] WCZYTAJ GRĘ")
    print("[3] NAJLEPSZE WYNIKI")
    print("[4] TWÓRCY")
    print("[5] CIEKAWOSTKI")
    print("[6] WYJŚCIE\n")
    x=int(input("CO WYBIERASZ? "))
    if x==1:
        print("\n[1] NOWA GRA\n")
        petlanowagra1=1
        print("WŁAŚNIE STWORZYŁEŚ NOWĄ GRĘ!")
        print("PODAJ SWOJE IMIĘ")
        imie=str(input())
        imie1=len(imie)
        znak=imie[(imie1)-1:(imie1)]
        if znak=="a" or znak=="A":
            print("JESTEŚ KOBIETĄ!")
            plec="K"
        else:
            print("JESTEŚ MĘŻCZYZNĄ")
            plec="M"
        nick=input("PODAJ SWÓJ NICK: ")
        while petlanowagra1==1:
            if plec=="M" or plec=="m":
                print("WŁAŚNIE STWORZYŁEŚ POSTAĆ O PSEUDONIMIE",nick,"!\n")
            elif plec=="K" or plec=="k":
                print("WŁAŚNIE STWORZYŁAŚ POSTAĆ O PSEUDONIMIE",nick,"!\n")
            else:
                print("UTWORZONO POSTAĆ O PSEUDONIMIE",nick,"!\n")
            print ("CO CHCESZ DALEJ ZROBIĆ?")
            print("[0] WYJŚCIE")
            print("[1] EDYTOWAĆ NAZWĘ POSTACI")
            print("[2] ZACZNIJ GRĘ - ZGADYWANIE LICZBY")
            print("[3] ZACZNIJ GRĘ - RYSOWANIE CHOINKI")
            x=int(input())
            if x==0:
                print("WYJŚCIE!\n")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                petlanowagra1=0
            elif x==1:
                print("EDYTUJESZ NAZWĘ POSTACI!")
                print("[1] ZMIANA PSEUDONIMU NA DUŻE LITERY")
                print("[2] ZMIANA PSEUDONIMU NA MAŁE LITERY")
                print("[3] ZMIANA PSEUDONIMU - WYBRANA LITERA JEST DUŻA,RESZTA LITER JEST MAŁA")
                print("[4] ZMIANA PSEUDONIMU - WYBRANA LITERA JEST MAŁA,RESZTA LITER JEST DUŻA")
                print("[5] ZMIANA PSEUDONIMU - ZAMIANA LITER DUŻYCH NA MAŁE I ODWROTNIE")
                print("[6] PONOWNY WYBÓR PSEUDONIMU")
                wybor=int(input())
                if wybor==1:
                    nick=nick.upper()
                    print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                    print("POWRÓT DO MENU")
                    yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                    x=0
                elif wybor==2:
                    nick=nick.lower()
                    print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                    print("POWRÓT DO MENU")
                    yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                    x=0
                elif wybor==3:
                    nr=input("KTÓRA LITERA TWOJEGO PSEUDONIMU MA ZOSTAĆ ZMIENIONA NA DUŻĄ? - ")
                    nr=int(nr)-1
                    nr1=nr+1
                    nick=nick.lower()
                    ostLit=(len(nick))
                    nick=nick[nr-nr:nr]+nick[nr:nr1].upper()+nick[nr1:ostLit].lower()
                    print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                elif wybor==4:
                    while wybor==4:
                        nr=input("KTÓRA LITERA TWOJEGO PSEUDONIMU MA ZOSTAĆ ZMIENIONA NA MAŁĄ? - ")
                        nr=int(nr)-1
                        if nr<=len(nick):
                            nr1=nr+1
                            nick=nick.upper()
                            ostLit=(len(nick))
                            nick=nick[nr-nr:nr]+nick[nr:nr1].lower()+nick[nr1:ostLit].upper()
                            print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                            wybor=0
                            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                            x=0
                        else:
                            print("TWÓJ NICK NIE JEST TAK DŁUGI!")
                            print("CO CHCESZ ZROBIĆ?")
                            print("[0] WYJŚCIE DO MENU")
                            print("[1] PONOWNA EYCJA NICKU")
                            wybor=int(input())
                            if wybor==1:
                                print("PONOWNA EDYCJA NICKU")
                                wybor=4
                            else:
                                print("PRZEJŚCIE DO MENU")
                                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                                x=0
                elif wybor==5:
                    nick=nick.swapcase()
                    print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                    wybor=0
                    yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                    x=0
                elif wybor==6:
                    print("PODAJ SWÓJ NOWY NICK")
                    nick=input()
                    print("TWÓJ NICK ZOSTAŁ ZMIENIONY - TERAZ NAZYWASZ SIĘ",nick)
                    wybor=0
                    yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                    x=0
                else:
                    print("BŁĘDNA KOMENA, DANE NIE ZOSTANĄ ZAPISANE. POWRÓT DO MENU!")
                    yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                    x=0
            elif x==2:
                from random import randint
                print("ZASADY GRY - ZOSTANIESZ POPROSZONY O PODANIE LICZBY, WYZNACZY ONA ZAKRES DLA PROGRAMU. KOMPUTER WYLOSUJE LOSOWO JEDNĄ Z LICZB - TWOIM ZADANIEM JEST ODGADNĄĆ TĄ LICZBĘ. Z KAŻDA PRÓBĄ, KOMPUTER PODPOWIE CI CZY WYBRANA LICZBA JEST WIĘKSZA CZY MNIEJSZA OD TEJ KTÓRĄ MASZ ZGADNĄĆ. PAMIĘTAJ, ABY NIE WYBIERAĆ LICZB Z POZA ZAKRESU!\n")
                print("CZEŚĆ",nick,"Z POŚRÓD ILU LICZB CHCESZ ZGADYWAĆ? ")
                zm=int(input())
                zag = randint(0,zm)
                for i in range(50):
                    odp=-1
                    i=0
                    print("ZGADNIJ WYLOSOWANĄ LICZBĘ Z ZADANEGO PRZEDZIAŁU, OD 0 DO",zm)
                    while odp!=zag:
                        i+=1
                        odp = int(input("Podaj liczbę: "))
                        if odp<0 or odp>zm:
                            print("LICZBA NIE ZNAJDUJE SIĘ W PRZEDZIALE!")
                        else:
                            if odp<zag:
                                print("WYLOSOWANA LICZBA JEST WIEKSZA OD TWOJEJ!")
                                print("LICZBA PRÓB:",i,"\n")
                            elif odp>zag:
                                print("WYLOSOWANA LICZBA JEST MNIEJSZA OD TWOJEJ!")
                                print("LICZBA PRÓB:",i,"\n")
                    print("BRAWO,",nick,"ODGADŁEŚ LICZBĘ ZA",i,"RAZEM!")
                    dec=input("CZY CHCESZ WYJŚĆ Z GRY? T/N ")
                    if dec=="T" or dec=="t":
                        print("CHCESZ WYJŚĆ Z GRY!")
                        yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                        break
                    elif dec=="N" or dec=="n":
                        print("CHCESZ ZOSTAĆ W GRZE!")
                        zm=int(input("SPOŚRÓD ILU LICZB CHCESZ ZGADYWAĆ? "))
                        zag = randint(0,zm)
                    else:
                        print("NIEROZPONANA DECYZJA - WYJŚCIE Z GRY!")
                        yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                        break
            elif x==3:
                print("[3] DRUKOWANIE CHOINKI")
                print("TU PO PROSTU WYDRUKUJĘ CHOINKĘ, OK?")
                ok=input()
                print("")
                if ok=="ok" or ok=="OK" or ok=="TAK" or ok=="tak":
                    ch=int(0)
                    print("ILE POZIOMÓW MA POSIADAĆ CHOINKA? ")
                    ch1=input()
                    print("Z JAKIEGO ZNAKU POINNA BYĆ CHOINKA? ")
                    znak=input()
                    znak=str(znak)
                    ch1=int(ch1)
                    print("DRUKOWANIE CHOINKI:")
                    while ch<ch1+1:
                        print(ch*znak)
                        ch+=1
                    print(znak)
                    print("\nCHOINKA O WYSOKOŚCI",ch1,"ZE ZNAKU",znak,"POWINNA BYĆ NARYSOWANA")
                    print("CO DALEJ?")
                    print ("[0] EXIT")
                    x=input()
                    x=int(x)
                    if x==0:
                        print("WYJŚCIE DO MENU!")
                        yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                    else:
                        print("COŚ ŹLE CI SIĘ PRZYCISNĘŁO, PRZEKIEROWANIE DO MENU")
                        yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                        x=0
                else:
                    print("NIE CHCESZ CHOINKI? TO SPADAJ DO MENU")
                    yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                    x=0
    elif x==2: 
        print("\n[2] WCZYTAJ GRĘ\n")
        moment=int(input("JAKI MOMENT GRY CHCESZ WCZYTAĆ? ([1/2/3/4/5]"))
        if moment<6:
            print("BRAK ZAPISANYCH MOMENTÓW!")
            powrot=int(input("KLIKNIJ [0] ABY POWRÓCIĆ DO MENU "))
            if powrot==0:
                print("POWRÓT DO MENU")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x=0
            else:
                print("BŁĘDNA KOMENDA! POWRÓT DO MENU.")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x=0
        else:
            print("BŁĘDNA KOMENDA! POWRÓT DO MENU.")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        print("[1] ULUBIONE\n")
        print("[0] WYJŚCIE")
        y=int(input())
        if y==0:
            print("WYJŚCIE!")
            del y
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        elif y==1:
            print("[2.1] ULUBIONE")
            print("TUTAJ SĄ ZAPISANE TWOJE ULUBIONE MOMENTY Z GRY\n")
            print("[0] WYJŚCIE")
            x=int(input())
            if x==0:
                print("PRZEKIEROWANIE DO GŁÓWNEGO MENU!")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x==0
            else:
                print("BŁĘDNA KOMENDA! PRZEKIEROWANIE DO MENU!")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x=int(0);
        else:
            print("BŁĘDNA KOMENDA! PRZEKIEROWANIE DO MENU!")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=int(0);
    elif x==3: 
        print("\n[3] NAJLEPSZE WYNIKI")
        wynik = int(1)
        while wynik<11:
            print (wynik,"BRAK NAJLEPSZEGO WYNIKU")
            wynik = wynik + 1
            
        print("[0] WYJŚCIE")
        x=int(input())
        if x==0:
            print("WYJŚCIE")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        else:
            print("BŁĘDNA KOMENDA! PRZEKIEROWANIE DO MENU!")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0;
    elif x==4: 
        print("\n[4] TWÓRCY")
        print("WSZYSTKO TUTAJ ROBIĘ SAM, NIE BĘDĘ SIĘ ZBĘDNIE ROZPISYWAĆ :)")
        print ("[0] EXIT")
        x=int(input())
        if x==0: 
            print("WYJŚCIE DO MENU!")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        else:
            print("COŚ ŹLE CI SIĘ PRZYCISNĘŁO, PRZEKIEROWANIE DO MENU")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
    elif x==5: 
        print("\n[5] CIEKAWOSTKI\n")
        print("[0] WYJŚCIE")
        print("[1] SPRAWDZANIE PIERWSZEGO SŁOWA")
        print("[2] SPRAWDZANIE OSTATNIEGO SŁOWA")
        print("[3] ZLICZANIE OKREŚLONEGO ZNAKU")
        print("[4] ZASTĘPOWANIE ZNAKU INNYM ZNAKIEM")
        print("[5] SPRADZANIE CZY WE FRAZIE SĄ SAME CYFRY ALBO LITERY")
        print("[6] SPRAWDZANIE POPRAWNOŚCI NUMERU TELEFONU\n")
        ciek=int(input("CO DOKŁADNIE CHCESZ ZROBIĆ? "))
        if ciek==0:
            print("[0] WYJŚCIE")
            print("PRZEKIEROWANIE DO MENU!")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        elif ciek==1:
            print("[1] SPRAWDZANIE PIERWSZEGO SŁOWA\n")
            slowo=input("PODAJ WYBRANE SŁOWO: ")
            print("STWÓRZ ZDANIE ROZPOCZYNAJĄCE SIĘ OD SŁOWA",slowo)
            zdanie=input()
            wynik=(zdanie.startswith(slowo))
            if wynik==True:
                print("ŚWIETNA ROBOTA!")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x=0
            else:
                print("NO NIE DO KOŃCA...")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x=0
        elif ciek==2:
            print("[2] SPRAWDZANIE OSTATNIEGO SŁOWA\n")
            slowo=input("PODAJ WYBRANE SŁOWO: ")
            print("STWÓRZ ZDANIE KOŃCZĄCE SIĘ NA SŁOWIE",slowo)
            zdanie=input()
            wynik=(zdanie.endswith(slowo))
            if wynik==True:
                print("ŚWIETNA ROBOTA!")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x=0
            else:
                print("NO NIE DO KOŃCA...")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
                x=0
        elif ciek==3:
            print("[3] ZLICZANIE OKREŚLONEGO ZNAKU\n")
            print("WPISZ PRZYKŁADOWĄ FRAZĘ (ZDANIE/SŁOWO/MYŚL):")
            sentencja=input()
            print("PODAJ ZNAK JAKI CIĘ INTERESUJE")
            senteznak=input()
            dana=sentencja.count(senteznak)
            print("SZUKANY ZNAK W PODANEJ FRAZIE WYSTĘPUJE",dana,"RAZY.")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        elif ciek==4:
            print("[4] ZASTĘPOWANIE ZNAKU INNYM ZNAKIEM\n")
            print("WPISZ PRZYKŁADOWĄ FRAZĘ (ZDANIE/SŁOWO/MYŚL):")
            sentencja=input()
            senteznak=input("PODAJ ZNAK/SŁOWO JAKI/E CHCESZ ZMIENIĆ WE FRAZIE?: ")
            ZnakDoZmiany=input("JAKI ZNAK/SŁOWO CHCESZ WPROWADZIĆ?: ")
            print(sentencja.replace(senteznak,ZnakDoZmiany))
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        elif ciek==5:
            print("[5] SPRADZANIE CZY WE FRAZIE SĄ SAME ZNAKI ALBO LITERY\n")
            print("WPISZ PRZYKŁADOWĄ FRAZĘ (ZDANIE/SŁOWO/MYŚL):")
            sentencja=input()
            isdigit=sentencja.isdigit()
            isalpha=sentencja.isalpha()
            if isdigit == True:
                print("\nTWOJA FRAZA ZAWIERA JEDYNIE CYFRY (1,2,3... :)")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            elif isalpha==True:
                print("\nTWOJA FRAZA ZAIERA JEDYNIE LITERY (A,B,C... :)")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            else:
                print("\nTWOJA FRAZA TO MIX LITER I CYFR!")
                yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
        elif ciek==6:
            print("[6] SPRAWDZANIE POPRAWNOŚCI NUMERU TELEFONU\n")
            print("PODAJ NUMER TELEFONU KOMÓRKOEGO BĄDŹ STACJONARNEGO.")
            print("PODANE NUMERY NIE POWINNY ZAWIERAĆ SPACJI!")
            print("NP: 510111990 albo 134323409\n")
            print("WPROWADŹ NUMER")
            nrTel=input()
            dlugosc=len(nrTel)
            poprawnosc=nrTel.isdigit()
            if dlugosc==9 and poprawnosc==True:
                print("NUMER TELEFONU JEST POPRAWNY!")
                yy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            else:
                print("NUMER TELEFONU NIE JEST POPRANY!")
                yy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
                
        else:
            print("\nBŁĘDNA KOMENDA - PRZEKIEROWANIE DO MENU!")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
    elif x==6: 
        print("\n[6] WYJŚCIE")
        print("CZY CHCESZ OPUŚCIĆ GRĘ? T/N\n")
        decyzja=str(input())
        if decyzja=="T" or decyzja=="t":
            print("DO WIDZENIA!")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
        elif decyzja=="N" or decyzja=="n":
            print("POWRÓT DO MENU!")
            x=0
        else:
            print("NIEPOPRAWNA KOMENDA, POWRÓT DO MENU")
            yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
            x=0
    else:
        print("\nBŁĘDNIE WYBRANA KOMENDA!")
        yyy=input("KLIKNIJ DOWOLNY PRZYCISK ABY KONTYNUOWAĆ...\n")
        x=int(0)
