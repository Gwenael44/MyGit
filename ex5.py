import math
import random
import re

def SommeMultipliéParDeux(nb1, nb2):
    return (nb1 * nb2) * 2

def Moyenne(nb1, nb2):
    return nb1/nb2

def Max(nb1, nb2):
    if nb1 > nb2:
        return nb1
    else:
        return nb2

def Min(nb1, nb2):
    if nb1 < nb2:
        return nb1
    else:
        return nb2


print('*******************')
nb1 = int(input('Nb : '))
nb2 = int(input('Nb : '))
print('Max : ', Max(nb1, nb2), '\n Min : ', Min(nb1,nb2))
print('*******************')
nb1 = int(input('Nb : '))
nb2 = int(input('Nb : '))
if nb1 != nb2:
    print('Max : ', Max(nb1, nb2), '\n Min : ', Min(nb1,nb2))
else:
    print('nb egaux')
print('*******************')
def AireTriangle(longueur, largeur):
    return (longueur * largeur) / 2
def Hypothenuse(longueur, largeur):
    return math.sqrt(longueur ** 2 + largeur ** 2)
print('*******************')
exo4 = [1, 2, 4, 9, 44, 11, 20, 34, 7]

def MaxArray(array):
    biggest;
    for a in range(array):
        if a == 0:
            biggest = array[a]
        else:
            if array[a] > biggest:
                biggest = array[a]

    return biggest

def SommeArray(array):
    somme = 0;
    for a in array:
        somme += a
    return somme

def MoyenneArray(array):
    total = SommeArray(array)
    return total / len(array)

def IsPair(nb):
    if nb %2 == 0:
        return True
    else:
        return False
def IsImpair(nb):
    if nb %2 == 1:
        return True
    else:
        return False

print(IsPair(1))
print(IsImpair(1))
print('*******************')

def NbChar(str):
    return len(str)

def NbWord(str):
    blabla = []
    value = ""
    i = 0
    for l in str :
        if l == " " :
            blabla.append(value)
            value = ""
        elif i == len(bla) -1 :
            value += l
            blabla.append(value)
        else :
            value += l
        i += 1
    return len(blabla)

def ListSommeRand(nb):
    array = []
    while SommeArray(array) < nb:
        
        if SommeArray(array) > nb:
            print('fail')
            return
        else:
            array.append(random.randint(0, nb - SommeArray(array)))
    print(SommeArray(array))
    return array

print(ListSommeRand(50))

print('*******************')
def IsADN(str):
    char = ["a","t","g","c"]
    check = 0
    for s in str:
        for c in char:
            if s == c:
                check += 1
    if check == len(str):
        return True
    else:
        return False

def GenerateADN(nb = 0):
    char = ["a","t","g","c"]
    validADN = ""
    if nb == 0:
        nb = random.randint(0, 20)
    for i in range(nb):
        rnd = random.randint(0, len(char) - 1)
        validADN += char[rnd]
    return validADN
                
print(GenerateADN(9))

def SeqADN(adn, seq):
    print('Chaine ADN : ', adn)
    print('Pattern : ', seq)
    print('Il y a', len(re.findall(seq, adn)) / len(adn) * 100, '% de', seq, 'dans votre chaine.')
    return len(re.findall(seq, adn))

print(SeqADN(GenerateADN(), 'ac'))
