# izveidojam jaunu klasi Game
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
        print("\nApsveicu tu uzminēji vārdu!")
        print(f"Nezināmais vārds bija {self.vards}.\n")

    # Metode, kura satur spēles pamatloģiku
    def play(self):
        # Iepazīšanās ar spēli
        print("\nSveicināti karātavās!")
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
                    print("Netika ievadīts burts vai vārds. Lūdzu mēģini vēlreiz.")
            
            # Noskaidrojam minējuma garumu, t.i. vai ir minēts burts vai vārds
            if len(minejums) == 1:
                # Minējums ir burts
                # Pārbaudam vai šāds burts jau ir minēts
                if minejums in self.minetie_burti:
                    # Šāds burts jau ir minēts
                    self.dzivibas -= 1
                    print("\nŠo burtu tu jau esi minējis!")
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
                            print("\nTu uzminēji burtu!\n")
                    else:
                        # Šis burts nav vārdā
                        self.dzivibas -= 1
                        print("\nDiemžēl tu neuzminēji, mēģini vēlreiz!")
            else:
                # Minējums ir vārds
                # Pārbaudam vai šāds vārds jau ir minēts
                if minejums in self.minetie_vardi:
                    # Šāds vārds jau ir minēts
                    self.dzivibas -= 1
                    print("\nŠo vārdu tu jau minēji!")
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
                        if len(self.vards) == len(minejums):
                            # Minētais vārds ir pareiza garuma
                            print("\nDiemžēl tu neuzminēji!")
                        elif len(self.vards) > len(minejums):
                            # Minētais vārds ir par īsu
                            print("\nIevadītais vārds ir par īsu!")
                        else:
                            # Minētais vārds ir par garu
                            print("\nIevadītais vārds ir par garu!")
            
            # Pārbaudam vai spēlētājam vēl ir dzīvības
            if self.dzivibas < 1:
                # Beidzās dzīvības
                print("\nDiemžēl, tev beidzās dzīvības un tu neizdevās uzminēt vārdu!\n")
                print(f"Nezināmais vārds bija {self.vards}.")
                print("\nGAME OVER\n")
                # Beidzam pamatcikla darbību
                self.vards_atminets = True
