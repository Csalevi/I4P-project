# 1. feladat
        
# kodolo fuggveny

def kodol(uzenet, kulcs):

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    def betuertek(betu):
        for i in range(len(abc)):
            if abc[i] == betu:
             return i

    rejtett = ""
    rejtertek = 0
    for i in range(len(uzenet)):
        rejtertek = betuertek(uzenet[i]) + betuertek(kulcs[i])
        
        if rejtertek <= 26:
            rejtett += abc[rejtertek]
        else:
            rejtett += abc[rejtertek % 27]

    return rejtett

# dekodolo fuggveny

def dekodol(rejtettuzenet, kulcs):

    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

    def betuertek(betu):
        for i in range(len(abc)):
            if abc[i] == betu:
                return i

    uzenet = ""
    uzenetertek = 0
    for i in range(len(rejtettuzenet)):
        uzenetertek = betuertek(rejtettuzenet[i]) - betuertek(kulcs[i])
        
        if uzenetertek >= 0:
            uzenet += abc[uzenetertek]
        else:

            uzenet += abc[27 - abs(uzenetertek)]
        
    return uzenet


# 2. feladat 

print("------------------------------------------")

szotar = []
with open('words.txt', "r") as bemenet:
    for sor in bemenet:
        szo = sor.strip()
        szotar.append(szo)

lejatszas_szama = 0
uzenet1 = ""
kulcs = ""
uzenet2 = ""
tart = 0
tartlista = ""

def kodfejto(rejtuz1, rejtuz2, ismertszo, szavaklista):
#print(kodol("cat visible absolutely ceo", "abcdefghijklmnopqrstuvwxyz "))       A KETTŐ ÜZENET PLUSZ A KULCS
#print(kodol("admission depression season", "abcdefghijklmnopqrstuvwxyz "))

    def utolsoszotorles(mondat):
        szavak = mondat.split()  
        if len(szavak) > 1: 
            szavak.pop()                   # Eltávolítja az utolsó szót
            uj_mondat = ""
            for i in range(len(szavak)):
                if i < len(szavak):
                    uj_mondat += szavak[i] + " "
                elif i == len(szavak):
                    uj_mondat += szavak[i]
        else:
            uj_mondat = mondat
        return uj_mondat
    
    global lejatszas_szama
    global uzenet1
    global kulcs
    global uzenet2
    global tart
    global tartlista

    
    kulcshossz = max(len(rejtuz1), len(rejtuz2))

    if lejatszas_szama == 0: 

        uzenet1 = ismertszo + " "
        kulcs = dekodol(rejtuz1[0:len(uzenet1)], uzenet1)
        uzenet2 = dekodol(rejtuz2[:len(kulcs)], kulcs)

    elif lejatszas_szama > 0: 

        uzenet1 += " "
        kulcs = dekodol(rejtuz1[:len(uzenet1)], uzenet1)
        uzenet2 = dekodol(rejtuz2[:len(kulcs)], kulcs)

        masodikszavai = uzenet2.strip().split(" ")
        print(masodikszavai)
        mindegyikhelyes = True
        for i in range(len(masodikszavai)):
            if i < len(masodikszavai) - 1:
                if masodikszavai[i] not in szavaklista:
                    mindegyikhelyes = False
        if mindegyikhelyes == False:
            uzenet1 = utolsoszotorles(uzenet1) + tartlista[tart + 1]
            tart += 1
            kulcs = dekodol(rejtuz1[0:len(uzenet1)], uzenet1)
            uzenet2 = dekodol(rejtuz2[:len(kulcs)], kulcs)
            kodfejto(rejtuz1, rejtuz2, ismertszo, szotar)            

    print(f"Lejatszas szama: {lejatszas_szama}")
    print(f"Uzenet 1: {uzenet1}") 
    print(f"Kulcs: {kulcs}")  
    print(f"Uzenet 2: {uzenet2}") 

    # while len(kulcs) < kulcshossz:                    CIKLUS?

    utolsoszokoz = 0
    if uzenet2.__contains__(" "):
        for i in range(len(uzenet2)):
            if uzenet2[i] == " ":
                utolsoszokoz = i
        uzenet2_utolsoszava = uzenet2[utolsoszokoz + 1:]
    else:
        uzenet2_utolsoszava = uzenet2[utolsoszokoz:]
    print(f"uzenet2_utolsoszava: {uzenet2_utolsoszava}")

    lehet2 = []
    for szo in szavaklista:
        if szo.startswith(uzenet2_utolsoszava):
            lehet2.append(szo)
    print(f"lehetseges 2. szavak: {lehet2}")



    lehetne = []
    for szo in lehet2:
            print(f"vizsgalt szo: {szo}")            
            kulcslehet = ""
            uzenet1lehet = ""
            uzenet2lehet = ""


            if utolsoszokoz == 0:
                uzenet2lehet = szo
            else:
                uzenet2lehet = utolsoszotorles(uzenet2) + szo
            print("uzenet2lehet " + uzenet2lehet)


            kulcslehet += dekodol(rejtuz2[:len(uzenet2lehet)], uzenet2lehet)
            print("kulcslehet "+ kulcslehet)


            uzenet1lehet = dekodol(rejtuz1[:len(kulcslehet)], kulcslehet)
            uzenet1lehet = uzenet1lehet[len(uzenet1):]
            print("uzenet1lehet " + uzenet1lehet)
            if uzenet1lehet == "":
                return kulcslehet

            print(f"vizsgalt eredmeny: {uzenet1lehet}")
            lehetne.append(uzenet1lehet)

    print(f"eredmenyek listaja: {lehetne}")

    lehetoseg = []
    for resz in lehetne:
        for i in range(len(szavaklista)):
            if szavaklista[i].startswith(resz) and not lehetoseg.__contains__(resz) and resz != "":
                lehetoseg.append(resz)
    print(f"ertelmes eredmenyek: {lehetoseg}")

        # itt futtassa végig az összes lehetségest és adja hozzá ha jó szavakat ad ki aztán csatoljon vissza a ciklus elejére vagy magába egy új függvénybe?
        # kilistázom a lehetőségeket és egy ciklusban hozzáadom az eddigi mondatokhoz és ismét lefuttatom az elejéről a már kiegészített mondatokkal


    lehet1 = []
    for resz in lehetoseg:
        for szo in szavaklista:              
            if szo.startswith(resz):
                lehet1.append(szo)
    
    if len(lehet1) > 0:
        tartlista = lehet1
        tart = 0

    print(f"1es mondat folytatasa lehet: {lehet1}")

    if len(lehet1) == 0:
        uzenet1 = utolsoszotorles(uzenet1) + tartlista[tart + 1]
        tart += 1
        kulcs = dekodol(rejtuz1[0:len(uzenet1)], uzenet1)
        uzenet2 = dekodol(rejtuz2[:len(kulcs)], kulcs)
        kodfejto(rejtuz1, rejtuz2, ismertszo, szotar)

    else:
        for i in range(len(lehet1)):
            if len(kulcs) == len(rejtuz1):
                return kulcs
            if len(kulcs) == kulcshossz:
                return kulcs
            elif len(kulcs) < kulcshossz:
                    lejatszas_szama += 1
                    uzenet1 += lehet1[i]
                    kulcs = dekodol(rejtuz1[0:len(uzenet1)], uzenet1)
                    uzenet2 = dekodol(rejtuz2[:len(kulcs)], kulcs)
                    kodfejto(rejtuz1, rejtuz2, ismertszo, szotar)
            



# A TESZT
rejtuz1 = "cbvcznypjuokmofcakkxesvzbm"
rejtuz2 = "aeolwxovvinpadsghzfftm xpmm"
ismertszo = "cat"
szavaklista = szotar
akulcs = kodfejto(rejtuz1, rejtuz2, ismertszo, szotar)
print(akulcs)