# izveidojam jaunu klasi Game
import random
from scripts.clear import clearConsole
import time
import sys

from datetime import datetime 
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
        self.karatavas = ['''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=======
''','''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=======
''','''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=======
''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=======
''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=======
''','''
  +---+
  |   |
  O   |
      |
      |
      |
=======
''','''
  +---+
  |   |
      |
      |
      |
      |
=======
''']
        
        # Displeja izvades parametri
        self.left_column_max = 7
        self.middle_column_max = 77
        self.right_column_max = 30
        self.left_column = []
        self.middle_column = ["","","","","","",""]
        self.right_column = ["","","","","","",""]

    # Displeja izvades menedžments
    def _refreshDisplay(self):
        # Atrast maksimālo rindu skaitu displeja reģionos
        max_rows = len(self.left_column)
        if len(self.middle_column) > max_rows:
            max_rows = len(self.middle_column)
        if len(self.right_column) > max_rows:
            max_rows = len(self.right_column)

        # Normalizēt attēlojamos displeja reģionus
        self.left_column = self._normalize(self.left_column, max_rows, self.left_column_max)
        self.middle_column = self._normalize(self.middle_column, max_rows, self.middle_column_max)
        self.right_column = self._normalize(self.right_column, max_rows, self.right_column_max)

        # Attēlot displeju
        clearConsole()
        for n in range(0, max_rows):
            print(f'{self.left_column[n]}   {self.middle_column[n]} | {self.right_column[n]}')

    # Izlīdzina līniju garumu un līniju skaitu sarakstā
    def _normalize(self, list, rows, cols):
        if len(list) < rows:
            i = rows - len(list)
            list += [' '] * i
        for l in range(0, len(list)):
            line = str(list[l])
            if len(line) < cols:
                c = cols - len(line)
                line = line + " " * c
            elif len(line) > cols:
                line = line[0:cols]
            list[l] = line
        return list

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
        self.left_column = self.karatavas[self.dzivibas].splitlines()

        self.middle_column[0] = f"        __  ________    _____    ____  ___    __"
        self.middle_column[1] = f"       / / / /__  / |  / /   |  / __ \/   |  / /"
        self.middle_column[2] = f"      / / / /  / /| | / / /| | / /_/ / /| | / / "
        self.middle_column[3] = f"     / /_/ /  / /_| |/ / ___ |/ _, _/ ___ |/_/  "
        self.middle_column[4] = f"     \____/  /____/___/_/  |_/_/ |_/_/  |_(_)   "
        self.middle_column[5] = f""
        self.middle_column[6] = f"Apsveicu tu uzminēji vārdu {self.vards}. Spēles laks (hh:mm:ss) {time_elapsed}"

        self.right_column[1] = f"   Dzīvības: {self.dzivibas}"
        self.right_column[3] = f"   Minēto burtu sk.: {len(self.minetie_burti)}"
        self.right_column[4] = f"   Minēto vārdu sk.: {len(self.minetie_vardi)}"

        self._refreshDisplay()

    # Metode, kura izvada zaudējuma paziņojumu
    def _game_over_pazinojums(self):
        time_elapsed = datetime.now() - self.start_time
        self.left_column = self.karatavas[self.dzivibas].splitlines()

        self.middle_column[0] = f"   _________    __  _________   ____ _    ____________ "
        self.middle_column[1] = f"  / ____/   |  /  |/  / ____/  / __ \ |  / / ____/ __ \\"
        self.middle_column[2] = f" / / __/ /| | / /|_/ / __/    / / / / | / / __/ / /_/ /"
        self.middle_column[3] = f"/ /_/ / ___ |/ /  / / /___   / /_/ /| |/ / /___/ _, _/ "
        self.middle_column[4] = f"\____/_/  |_/_/  /_/_____/   \____/ |___/_____/_/ |_|  "
        self.middle_column[5] = f""
        self.middle_column[6] = f"Nezināmais vārds bija {self.vards}. Spēles laks (hh:mm:ss) {time_elapsed}"

        self.right_column[1] = f"   Dzīvības: {self.dzivibas}"
        self.right_column[3] = f"   Minēto burtu sk.: {len(self.minetie_burti)}"
        self.right_column[4] = f"   Minēto vārdu sk.: {len(self.minetie_vardi)}"

        self._refreshDisplay()


    # Metode, kura satur spēles pamatloģiku
    def play(self):
        # Uzsākam laika atskaiti
        self.start_time = datetime.now()

        # Izveidojam pirmo displeja izvadi
        self.middle_column[0] = f"   --== Laipni lūgti karātāvās! ==--"
        self.middle_column[2] = f"Uzmini vārdu, kas sastāv no {len(self.vards)} burtiem."
        
        self.right_column[0] = f"Statistika:"
        self.right_column[2] = f"   Vārda  garums: {len(self.vards)}"
        self.right_column[6] = f"Grūtības pakāpe: {self.grutibas_pakape}"

        # Uzsākam spēles pamatciklu
        while not self.vards_atminets:
            # Izdrukā atlikušo dzīvību skaitu un minēšanas progresu
            self.left_column = self.karatavas[self.dzivibas].splitlines()
            self.middle_column[6] = f"Tavs progress: {self.aizklats_vards}"
            self.right_column[1] = f"   Dzīvības: {self.dzivibas}"
            self.right_column[3] = f"   Minēto burtu sk.: {len(self.minetie_burti)}"
            self.right_column[4] = f"   Minēto vārdu sk.: {len(self.minetie_vardi)}"

            self._refreshDisplay()

            # Burta vai vārda ievade un ievades validācija
            deriga_ievade = False
            minejums = ""
            while not deriga_ievade:
                try:
                    minejums = input("\nIeraksti burtu vai vārdu: ")
                except EOFError:
                    self.middle_column[2] = 'Saņemta "EOFError" kļūda!'
                    self.middle_column[3] = ""
                    self.middle_column[4] = ""
                    self.middle_column[5] = ""
                    self._refreshDisplay()
                except KeyboardInterrupt:
                    print('\nPaldies par spēli gaidīsim tevi atkal!')
                    sys.exit()
                else:
                    if minejums.isalpha():
                        # Minējums sastāv tikai no burtiem
                        minejums = minejums.upper()
                        deriga_ievade = True
                        self.middle_column[2] = ""
                        self.middle_column[3] = ""
                        self.middle_column[4] = ""
                        self.middle_column[5] = ""
                    else:
                        # Nederīgs minējums
                        self.middle_column[2] = "Netika ievadīts burts vai vārds. Lūdzu mēģini vēlreiz."
                        self.middle_column[3] = ""
                        self.middle_column[4] = ""
                        self.middle_column[5] = ""
                        self._refreshDisplay()
            
            # Noskaidrojam minējuma garumu, t.i. vai ir minēts burts vai vārds
            if len(minejums) == 1:
                # Minējums ir burts
                # Pārbaudam vai šāds burts jau ir minēts
                if minejums in self.minetie_burti:
                    # Šāds burts jau ir minēts
                    self.middle_column[2] = "Šo burtu tu jau esi minējis!"
                    self.middle_column[3] = "Esi uzmanīgāks!"
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
                            self.middle_column[2] = "Tu uzminēji burtu!"
                    else:
                        # Šis burts nav vārdā
                        self.dzivibas -= 1
                        self.middle_column[2] = "Diemžēl tu neuzminēji, mēģini vēlreiz!"
                        self.middle_column[3] = f'Minamajā vārdā nav burta "{minejums}"'
            else:
                # Minējums ir vārds
                # Pārbaudam vai šāds vārds jau ir minēts
                if minejums in self.minetie_vardi:
                    # Šāds vārds jau ir minēts
                    self.middle_column[2] = "Šo vārdu tu jau esi minējis!"
                    self.middle_column[3] = "Esi uzmanīgāks!"
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
                            self.middle_column[2] = "Diemžēl tu neuzminēji!"
                        elif len(self.vards) > len(minejums):
                            # Minētais vārds ir par īsu
                            self.middle_column[2] = "Ievadītais vārds ir par īsu!"
                        else:
                            # Minētais vārds ir par garu
                            self.middle_column[2] = "Ievadītais vārds ir par garu!"
            
            # Pārbaudam vai spēlētājam vēl ir dzīvības
            if self.dzivibas < 1:
                # Beidzās dzīvības
                self.vards_atminets = True
                self._game_over_pazinojums()

            # Atlaujam atvert kadu no neuzminetajiem burtiem, ja ir palikusi 1 dziviba
            # Izmantojot papildiespeju tiek izmantots nejausi izvelets burts, kas nav atminets
            if self.dzivibas == 1 and self.papildiespeja == False:
                self.middle_column[4] = "Ak vai tev palika tikai viena dzīvība."
                self.middle_column[5] = "Lai tev palīdzētu, sniegsim tev papildiespēju!"
                self._refreshDisplay()

                try:
                    atbilde = input("\nVai gribi izmantot papildiespeju un atklat vienu burtu (jā / nē): ").upper()
                except EOFError:
                    self.middle_column[2] = 'Saņemta "EOFError" kļūda!'
                    self.middle_column[3] = ""
                    self.middle_column[4] = ""
                    self.middle_column[5] = ""
                    self._refreshDisplay()
                    time.sleep(3)
                except KeyboardInterrupt:
                    print('\nPaldies par spēli gaidīsim tevi atkal!')
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
                        self.middle_column[2] = f'Nezināmais vārds satur burtu "{atklatais_burts}".'
                        self.middle_column[3] = ""
                        self.middle_column[4] = ""
                        self.middle_column[5] = ""
                    else:
                        # Papildiespeja netika izmantota
                        self.middle_column[2] = f'Tev ir palikusi pēdējā dzīvība. Saņemies!'
                        self.middle_column[3] = ""
                        self.middle_column[4] = ""
                        self.middle_column[5] = ""