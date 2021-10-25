import random

# Minamo vārdu saraksts - latviešu alfabets
vardu_saraksts = ["Vanna"]

# Nejauši izvēlas vārdu un pārveido uz lielajiem burtiem
vards = random.choice(vardu_saraksts).upper()
varda_garums = len(vards)

# Atlikušās dzīvības
dzivibas = 6

# Minēto burtu saraksts
minetie_burti = []

#uzminēto burtu saraksts
uzminetie_burti = []

# Minēto vārdu saraksts
minetie_vardi = []

def aizklata_varda_generators(vards, uzminetie_burti): # funkcija kas izveido aizklātu vārdu, funkcijai vajag divus parametrus mināmo vārdu un sarakstu ar jau uzminētajiem burtiem
    aizklats_vards = ""
    for burts in vards:
        if burts in uzminetie_burti:
            aizklats_vards += burts
        else:
            aizklats_vards += "-"
    return aizklats_vards # tiek atgriezts teksts

def uzvaras_pazinojums(vards):
    print("\nApsveicu tu uzminēji vārdu!")
    print(f"Nezināmais vārds bija {vards}.\n")
    return True

# Izveido aizklāto vārdu
aizklats_vards = aizklata_varda_generators(vards, uzminetie_burti)

# Iepazīšanās ar spēli
print("\nSveicināti karātavās!")
print(f"Uzmini vārdu, kas sastāv no {varda_garums} burtiem.\n")

# Uzsāk spēles ciklu
vards_atminets = False
while not vards_atminets:
    print(f"Tev vēl ir palikušas {dzivibas} dzīvības.\n")
    print(f" {aizklats_vards}\n")

    # Burta vai vārda ievade un ievades validācija
    deriga_ievade = False
    while not deriga_ievade:
        minejums = input("Ieraksti burtu vai vārdu: ")
        if minejums.isalpha():
            # Minējums sastāv tikai no burtiem
            minejums = minejums.upper()
            deriga_ievade = True
        else:
            # Nederīgs minējums
            print("Netika ievadīts burts vai vārds. Lūdzu mēģini vēlreiz.")

    if len(minejums) == 1:
        # Minējums ir burts
        if minejums in minetie_burti:
            # Šāds burts jau ir minēts
            dzivibas -= 1
            print("\nŠo burtu tu jau minēji!")
        else:
            # Šāds burts vēl nav minēts
            minetie_burti.append(minejums)
            if minejums in vards:
                #Šis burts ir vārdā
                uzminetie_burti.append(minejums)

                # Parāda atminētos burtus
                aizklats_vards = aizklata_varda_generators(vards, uzminetie_burti)
                
                if aizklats_vards == vards:
                    # Vārds ir atminēts
                    vards_atminets = uzvaras_pazinojums(vards)
                else:
                    # Visi burti vēl nav atminēti
                    print("\nTu uzminēji burtu!\n")
            else:
                # Šis burts nav vārdā
                dzivibas -= 1
                print("\nDiemžēl tu neuzminēji!")
    else:
        # Minējums ir vārds
        if minejums in minetie_vardi:
            # Šāds vārds jau ir minēts
            dzivibas -= 1
            print("\nŠo vārdu tu jau minēji!")
        else:
            # Šāds vārds vēl nav minēts
            minetie_vardi.append(minejums)
            if minejums == vards:
                # Vārds ir atminēts
                vards_atminets = uzvaras_pazinojums(vards)
            else:
                # Vārds nav atminēts
                dzivibas -= 1
                if varda_garums == len(minejums):
                    print("\nDiemžēl tu neuzminēji!")
                elif varda_garums > len(minejums):
                    print("\nIevadītais vārds ir par īsu!")
                else:
                    print("\nIevadītais vārds ir par garu!")


    if dzivibas < 1:
        # Beidzās dzīvības
        print("\nDiemžēl, tev beidzās dzīvības un tu neizdevās uzminēt vārdu!\n")
        print("\nGAME OVER\n")
        vards_atminets = True