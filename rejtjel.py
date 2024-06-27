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
