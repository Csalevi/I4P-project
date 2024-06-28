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
with open("words.txt", "r") as bemenet:
    for sor in bemenet:
        szo = sor.strip()
        szotar.append(szo)


#def kodfejto(rejtuz1, rejtuz2, ismertszo, szavaklista):             FÜGGVÉNY KEZDETE LESZ
#print(kodol("cat visible absolutely ceo", "abcdefghijklmnopqrstuvwxyz "))       A KETTŐ ÜZENET PLUSZ A KULCS
#print(kodol("admission depression season", "abcdefghijklmnopqrstuvwxyz "))
rejtuz1 = "cbvcznypjuokmofcakkxesvzbm"
rejtuz2 = "aeolwxovvinpadsghzfftm xpmm"
ismertszo = "cat"
szavaklista = szotar


if len(rejtuz1) >= len(rejtuz2):
    kulcshossz = len(rejtuz1)
else:
   kulcshossz = len(rejtuz2)

uzenet1 = ""
uzenet1 = ismertszo + " "

kulcs = ""
kulcs += dekodol(rejtuz1[0:len(uzenet1)], uzenet1)

uzenet2 = ""
uzenet2most = dekodol(rejtuz2[:len(kulcs)], kulcs)
print(uzenet2most)

# while len(kulcs) < kulcshossz:                    CIKLUS?

utolsoszokoz = 0
if uzenet2most.__contains__(" "):
    for i in range(len(uzenet2most)):
        if uzenet2most[i] == " ":
            utolsoszokoz = i
uzenet2_utolsoszava = uzenet2most[utolsoszokoz:len(uzenet2most)]

lehet2 = []
for szo in szavaklista:
    if szo.startswith(uzenet2_utolsoszava):
        lehet2.append(szo)

#print(lehet)                                   LEHETSÉGES SZAVAK LISTÁJA

kulcslehet = ""
uzenet1lehet = ""
uzenet2lehet = ""

lehetne = []
for szo in lehet2:
        uzenet2lehet = szo
        print(szo)
        kulcslehet = dekodol(rejtuz2[:len(uzenet2lehet)], uzenet2lehet)
        uzenet1lehet = dekodol(rejtuz1[:len(kulcslehet)], kulcslehet)
        uzenet1lehet = uzenet1lehet[len(uzenet1):]
        print(uzenet1lehet)
        lehetne.append(uzenet1lehet)

print(lehetne)

lehet1 = []
for szo in lehetne:
    for i in range(len(szavaklista)):
        if szavaklista[i].startswith(szo) and not lehet1.__contains__(szo):
            lehet1.append(szo)
print(lehet1)