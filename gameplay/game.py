

# izveidojam jaunu klasi Game
import random
from scripts.clear import clearConsole
#123

class Game:
    # veicam klases inicializāciju nododot tai minamo vārdu
    def __init__(self, vards):
        #veicam visu mainīgo lielumu reģistrāciju
        self.vards = vards.upper()
        self.dzivibas = 6
        self.minetie_burti = []
        self.minetie_vardi = []
        self.uzminetie_burti = []
        self.aizklats_vards = self._aizklata_varda_generators()
        self.vards_atminets = False
        self.papildiespeja = False

    # Metode, kura nodrošina neuzminēto burtu aiklāšanu ar "-" simboli
    def _aizklata_varda_generators(self):
        self.aizklats_vards = ""
        for burts in self.vards:
            if burts in self.uzminetie_burti:
                self.aizklats_vards += burts
            else:
                self.aizklats_vards += "-"
        return self.aizklats_vards # tiek atgriezts teksts

    # Metode, kura izvada uzvaras paziņojumu
    def _uzvaras_pazinojums(self):
        clearConsole()
        print("\nApsveicu tu uzminēji vārdu!")
        print(f"Nezināmais vārds bija {self.vards}.\n")

    # Metode, kura satur spēles pamatloģiku
    def play(self):

        print(f"Uzmini vārdu, kas sastāv no {len(self.vards)} burtiem.\n")

        # Uzsākam spēles pamatciklu
        while not self.vards_atminets:
            # Izdrukā atlikušo dzīvību skaitu un minēšanas progresu
            print(f"Tev vēl ir palikušas {self.dzivibas} dzīvības.\n")
            print(f"Tavs progress: {self.aizklats_vards}\n")

            # Burta vai vārda ievade un ievades validācija
            deriga_ievade = False
            minejums = ""
            while not deriga_ievade:
                minejums = input("Ieraksti burtu vai vārdu: ")
                if minejums.isalpha():
                    # Minējums sastāv tikai no burtiem
                    minejums = minejums.upper()
                    deriga_ievade = True
                else:
                    # Nederīgs minējums
                    print("\nNetika ievadīts burts vai vārds. Lūdzu mēģini vēlreiz.")
            
            # Noskaidrojam minējuma garumu, t.i. vai ir minēts burts vai vārds
            if len(minejums) == 1:
                # Minējums ir burts
                # Pārbaudam vai šāds burts jau ir minēts
                if minejums in self.minetie_burti:
                    # Šāds burts jau ir minēts
                    #self.dzivibas -= 1
                    clearConsole()
                    print("\nŠo burtu tu jau esi minējis!\n")
                else:
                    # Šāds burts vēl nav minēts
                    self.minetie_burti.append(minejums)
                    # Pārbaudam vai burts ir minamajā vārdā
                    if minejums in self.vards:
                        # Šis burts ir vārdā. Pievienojam to uzminēto burtu sarakstam.
                        self.uzminetie_burti.append(minejums)

                        # Atjaunina minēšanas progresu
                        self.aizklats_vards = self._aizklata_varda_generators()
                        
                        # Pārbaudam vai minējuma progress sakrīt ar minamo vārdu
                        if self.aizklats_vards == self.vards:
                            # Vārds ir atminēts
                            self.vards_atminets = True
                            self._uzvaras_pazinojums()
                        else:
                            # Visi burti vēl nav atminēti
                            clearConsole()
                            print("\nTu uzminēji burtu!\n")
                    else:
                        # Šis burts nav vārdā
                        self.dzivibas -= 1
                        clearConsole()
                        print("\nDiemžēl tu neuzminēji, mēģini vēlreiz!\n")
            else:
                # Minējums ir vārds
                # Pārbaudam vai šāds vārds jau ir minēts
                if minejums in self.minetie_vardi:
                    # Šāds vārds jau ir minēts
                    #self.dzivibas -= 1
                    clearConsole()
                    print("\nŠo vārdu tu jau minēji!\n")
                else:
                    # Šāds vārds vēl nav minēts
                    # Pievienojam jauno vārdu minēto vārdu sarakstam
                    self.minetie_vardi.append(minejums)

                    # Pārbaudam vai minējums sakrīt ar minamo vārdu
                    if minejums == self.vards:
                        # Vārds ir atminēts
                        self.vards_atminets = True
                        self._uzvaras_pazinojums()
                    else:
                        # Vārds nav atminēts
                        self.dzivibas -= 1

                        # Pārbaudām vai minētais vārds ir ar pareizu garumu
                        clearConsole()
                        if len(self.vards) == len(minejums):
                            # Minētais vārds ir pareiza garuma
                            print("\nDiemžēl tu neuzminēji!\n")
                        elif len(self.vards) > len(minejums):
                            # Minētais vārds ir par īsu
                            print("\nIevadītais vārds ir par īsu!\n")
                        else:
                            # Minētais vārds ir par garu
                            print("\nIevadītais vārds ir par garu!\n")
            
            
            # Pārbaudam vai spēlētājam vēl ir dzīvības
            if self.dzivibas < 1:
                # Beidzās dzīvības
                clearConsole()
                print("\nDiemžēl, tev beidzās dzīvības un tu neizdevās uzminēt vārdu!\n")
                print(f"Nezināmais vārds bija {self.vards}.")
                print("\nGAME OVER\n")
                # Beidzam pamatcikla darbību
                self.vards_atminets = True

            # Atlaujam atvert kadu no neuzminetajiem burtiem, ja ir palikusi 1 dziviba
            # Izmantojot papildiespeju tiek izmantots nejausi izvelets burts, kas nav atminets
            if self.dzivibas == 1 and self.papildiespeja == False:
                 
                print("\nVai gribi izmantot papildiespeju un atklat vienu burtu?\n")
                atbilde = input("Vai gribi izmantot papildiespeju un atklat vienu burtu (jā / nē): ").upper()
                if atbilde in ["JĀ", "JA", "J", "Yes", "Y"]:
                    self.papildiespeja = True
                    neuzminetie_burti = []
                    for burts in self.vards:
                        if burts not in self.aizklats_vards:
                            neuzminetie_burti.append(burts)
                    neuzminetie_burti = list(set(neuzminetie_burti))
                    atklatais_burts = random.choice(neuzminetie_burti)
                    print(f"\nSis vards satur burtu {atklatais_burts}")
                else:
                    # Papildiespeja netika izmantota
                    print("\nTev ir palikusi pedeja dziviba. Sanemies!")

            # Atlaujam iziet no speles jebkura bridi

                        