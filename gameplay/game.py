# izveidojam jaunu klasi Game
import random
import time
import sys
from scripts.display import Display
from animations.animationHangmanLives import AnimationHangmanLives
from datetime import datetime 

"""The level of the Game is defined with list of words by difficulty (3 levels options: easy, medium or hard words).

self. includes characteristic of the words and letters for guess, and other parameters of variable, also taimer and animation class. 
"""
class Game:
    # veicam klases inicializāciju nododot tai minamo vārdu
    def __init__(self, vards, grutibas_pakape):
        #veicam visu mainīgo lielumu reģistrāciju
        self.vards = vards.upper()
        self.dzivibas = 6
        self.minetie_burti = []
        self.minetie_vardi = []
        self.uzminetie_burti = []
        self.aizklats_vards = self._aizklata_varda_generators()
        self.vards_atminets = False
        self.papildiespeja = False
        self.grutibas_pakape = grutibas_pakape

        # Taimera mainīgie lielumi
        self.start_time = 0

        # Karātavu bilde
        self.karatavas = AnimationHangmanLives()
        
        # Displeja izvades parametri
        self.display = Display()

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
        time_elapsed = datetime.now() - self.start_time
        self.display.updateCulumn(0, self.karatavas.getFrame(self.dzivibas))

        self.display.updateLine(1, 0, f"        __  ________    _____    ____  ___    __")
        self.display.updateLine(1, 1, f"       / / / /__  / |  / /   |  / __ \/   |  / /")
        self.display.updateLine(1, 2, f"      / / / /  / /| | / / /| | / /_/ / /| | / / ")
        self.display.updateLine(1, 3, f"     / /_/ /  / /_| |/ / ___ |/ _, _/ ___ |/_/  ")
        self.display.updateLine(1, 4, f"     \____/  /____/___/_/  |_/_/ |_/_/  |_(_)   ")
        self.display.updateLine(1, 5, f" ")
        self.display.updateLine(1, 6, f"Apsveicu tu uzminēji vārdu {self.vards}. Spēles laks (hh:mm:ss) {time_elapsed}")

        self.display.updateLine(2, 1, f"   Dzīvības: {self.dzivibas}")
        self.display.updateLine(2, 3, f"   Minēto burtu sk.: {len(self.minetie_burti)}")
        self.display.updateLine(2, 4, f"   Minēto vārdu sk.: {len(self.minetie_vardi)}")

        self.display.refresh()

    # Metode, kura izvada zaudējuma paziņojumu
    def _game_over_pazinojums(self):
        time_elapsed = datetime.now() - self.start_time
        self.display.updateCulumn(0, self.karatavas.getFrame(self.dzivibas))

        self.display.updateLine(1, 0, f"   _________    __  _________   ____ _    ____________ ")
        self.display.updateLine(1, 1, f"  / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \\")
        self.display.updateLine(1, 2, f" / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ /")
        self.display.updateLine(1, 3, f"/ /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/ ")
        self.display.updateLine(1, 4, f"\____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_|  ")
        self.display.updateLine(1, 5, f" ")
        self.display.updateLine(1, 6, f"Nezināmais vārds bija {self.vards}. Spēles laks (hh:mm:ss) {time_elapsed}")

        self.display.updateLine(2, 1, f"   Dzīvības: {self.dzivibas}")
        self.display.updateLine(2, 3, f"   Minēto burtu sk.: {len(self.minetie_burti)}")
        self.display.updateLine(2, 4, f"   Minēto vārdu sk.: {len(self.minetie_vardi)}")

        self.display.refresh()

    def _game_exit(self):
        time_elapsed = datetime.now() - self.start_time
        self.display.updateCulumn(0, self.karatavas.getFrame(self.dzivibas))

        self.display.updateLine(1, 0, f"   __  _______      ____  __________  _____   ____   __")
        self.display.updateLine(1, 1, f"  / / / /__  /     / __ \/ ____/ __ \/__  /  /  _/  / /")
        self.display.updateLine(1, 2, f" / / / /  / /     / /_/ / __/ / / / /  / /   / /   / / ")
        self.display.updateLine(1, 3, f"/ /_/ /  / /__   / _, _/ /___/ /_/ /  / /___/ /   /_/  ")
        self.display.updateLine(1, 4, f"\____/  /____/  /_/ |_/_____/_____/  /____/___/  (_)   ")
        self.display.updateLine(1, 5, f" ")
        self.display.updateLine(1, 6, f"Nezināmais vārds bija {self.vards}. Spēles laks (hh:mm:ss) {time_elapsed}")
        self.display.updateLine(1, 7, f"Paldies par spēli gaidīsim tevi atkal!")

        self.display.updateLine(2, 1, f"   Dzīvības: {self.dzivibas}")
        self.display.updateLine(2, 3, f"   Minēto burtu sk.: {len(self.minetie_burti)}")
        self.display.updateLine(2, 4, f"   Minēto vārdu sk.: {len(self.minetie_vardi)}")

        self.display.refresh()

    # Metode, kura satur spēles pamatloģiku
    def play(self):
        # Uzsākam laika atskaiti
        self.start_time = datetime.now()

        # Izveidojam pirmo displeja izvadi
        self.display.updateLine(1, 0, f"   --== Laipni lūgti karātāvās! ==--")
        self.display.updateLine(1, 2, f"Uzmini vārdu, kas sastāv no {len(self.vards)} burtiem.")
        
        self.display.updateLine(2, 0, f"Statistika:")
        self.display.updateLine(2, 2, f"   Vārda  garums: {len(self.vards)}")
        self.display.updateLine(2, 6, f"Grūtības pakāpe: {self.grutibas_pakape}.")
        self.display.updateLine(2, 7, f"Raksti EXIT, lai izietu.")

        # Uzsākam spēles pamatciklu
        while not self.vards_atminets:
            # Izdrukā atlikušo dzīvību skaitu un minēšanas progresu
            self.display.updateCulumn(0, self.karatavas.getFrame(self.dzivibas))
            self.display.updateLine(1, 6, f"Tavs progress: {self.aizklats_vards}")
            self.display.updateLine(2, 1, f"   Dzīvības: {self.dzivibas}")
            self.display.updateLine(2, 3, f"   Minēto burtu sk.: {len(self.minetie_burti)}")
            self.display.updateLine(2, 4, f"   Minēto vārdu sk.: {len(self.minetie_vardi)}")

            self.display.refresh()

            # Burta vai vārda ievade un ievades validācija
            deriga_ievade = False
            minejums = ""
            while not deriga_ievade:
                try:
                    minejums = input("\nIeraksti burtu vai vārdu: ")
                except EOFError:
                    self.display.updateLine(1, 2, 'Saņemta "EOFError" kļūda!')
                    self.display.updateLine(1, 3, " ")
                    self.display.updateLine(1, 4, " ")
                    self.display.updateLine(1, 5, " ")
                    self.display.refresh()
                except KeyboardInterrupt:
                    self._game_exit()
                    sys.exit()
                else:
                    if minejums.isalpha():
                        # Minējums sastāv tikai no burtiem
                        minejums = minejums.upper()
                        deriga_ievade = True
                        self.display.updateLine(1, 2, " ")
                        self.display.updateLine(1, 3, " ")
                        self.display.updateLine(1, 4, " ")
                        self.display.updateLine(1, 5, " ")
                    else:
                        # Nederīgs minējums
                        self.display.updateLine(1, 2, "Netika ievadīts burts vai vārds. Lūdzu mēģini vēlreiz.")
                        self.display.updateLine(1, 3, " ")
                        self.display.updateLine(1, 4, " ")
                        self.display.updateLine(1, 5, " ")
                        self.display.refresh()
            
            # Noskaidrojam minējuma garumu, t.i. vai ir minēts burts vai vārds
            if len(minejums) == 1:
                # Minējums ir burts
                # Pārbaudam vai šāds burts jau ir minēts
                if minejums in self.minetie_burti:
                    # Šāds burts jau ir minēts
                    self.display.updateLine(1, 2, "Šo burtu tu jau esi minējis!")
                    self.display.updateLine(1, 3, "Esi uzmanīgāks!")
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
                            self.display.updateLine(1, 2, "Tu uzminēji burtu!")
                    else:
                        # Šis burts nav vārdā
                        self.dzivibas -= 1
                        self.display.updateLine(1, 2, "Diemžēl tu neuzminēji, mēģini vēlreiz!")
                        self.display.updateLine(1, 3, f'Minamajā vārdā nav burta "{minejums}"')
            else:
                # Minējums ir vārds
                # Pārbaudam vai šāds vārds jau ir minēts
                if minejums in self.minetie_vardi:
                    # Šāds vārds jau ir minēts
                    self.display.updateLine(1, 2, "Šo vārdu tu jau esi minējis!")
                    self.display.updateLine(1, 3, "Esi uzmanīgāks!")
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
                            self.display.updateLine(1, 2, "Diemžēl tu neuzminēji!")
                        elif len(self.vards) > len(minejums):
                            # Minētais vārds ir par īsu
                            self.display.updateLine(1, 2, "Ievadītais vārds ir par īsu!")
                        else:
                            # Minētais vārds ir par garu
                            self.display.updateLine(1, 2, "Ievadītais vārds ir par garu!")
            
            # Pārbaudam vai spēlētājam vēl ir dzīvības
            if self.dzivibas < 1:
                # Beidzās dzīvības
                self.vards_atminets = True
                self._game_over_pazinojums()

            # Atlaujam atvert kadu no neuzminetajiem burtiem, ja ir palikusi 1 dziviba
            # Izmantojot papildiespeju tiek izmantots nejausi izvelets burts, kas nav atminets
            if self.dzivibas == 1 and self.papildiespeja == False:
                self.display.updateLine(1, 4, "Ak vai tev palika tikai viena dzīvība.")
                self.display.updateLine(1, 5, "Lai tev palīdzētu, sniegsim tev papildiespēju!")
                self.display.refresh()

                try:
                    atbilde = input("\nVai gribi izmantot papildiespeju un atklat vienu burtu (jā / nē): ").upper()
                except EOFError:
                    self.display.updateLine(1, 2, 'Saņemta "EOFError" kļūda!')
                    self.display.updateLine(1, 3, " ")
                    self.display.updateLine(1, 4, " ")
                    self.display.updateLine(1, 5, " ")
                    self.display.refresh()
                    time.sleep(3)
                except KeyboardInterrupt:
                    self._game_exit()
                    sys.exit()
                else:
                    if atbilde in ["JĀ", "JA", "J", "Yes", "Y"]:
                        self.papildiespeja = True
                        neuzminetie_burti = []
                        for burts in self.vards:
                            if burts not in self.aizklats_vards:
                                neuzminetie_burti.append(burts)
                        neuzminetie_burti = list(set(neuzminetie_burti))
                        atklatais_burts = random.choice(neuzminetie_burti)
                        self.display.updateLine(1, 2, f'Nezināmais vārds satur burtu "{atklatais_burts}".')
                        self.display.updateLine(1, 3, " ")
                        self.display.updateLine(1, 4, " ")
                        self.display.updateLine(1, 5, " ")
                    else:
                        # Papildiespeja netika izmantota
                        self.display.updateLine(1, 2, f'Tev ir palikusi pēdējā dzīvība. Saņemies!')
                        self.display.updateLine(1, 3, " ")
                        self.display.updateLine(1, 4, " ")
                        self.display.updateLine(1, 5, " ")