a = int(input('1ere valeur : '))
b = int(input('2eme valeur : '))
if a > b :
    print('Plus grosse valeur : ', a)
elif a == b :
    print('Les valeurs sont égales')
else :
    print ('Plus grosse valeur : ', b)

print('******************')

password = 'toto'
check = input('Mot de passe : ')
if password == check :
    print('Mot de passe correct')
else :
    print('Mot de passe incorrect')

print('******************')
input1 = input('Mois : ')
month = 0
value = 50
months = ['JANVIER', 'FEVRIER', 'MARS', 'AVRIL', 'MAI', 'JUIN', 'JUILLET', 'AOUT', 'SEPTEMBRE', 'OCTOBRE', 'NOVEMBRE', 'DECEMBRE']
for m in months :
    month += 1
    if input1.upper() == m :
        value = month
if value == 50 :
    print('Erreur de saisie')
else :
    print('Le mois est : ', value)
print('******************')
nb = int(input("Nombre : "))
if nb%2 == 0 :
    print("C'est un nombre pair")
else :
    print("C'est un nombre impair")
print('******************')
chaine1 = input('1ere chaine : ')
chaine2 = input('2eme chaine : ')

if len(chaine1) == len(chaine2) :
    print('La longueur des chaines est égale')
elif len(chaine1) > len(chaine2) :
    print("C'est : ", chaine1, " la plus longue.")
else :
    print("C'est : ", chaine2, " la plus longue.")
print('******************')
lettre = input('Lettre : ')
voyelles = ["a","e","i","o","u","y"]
consonnes = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
test = False
test2 = False
for v in voyelles :
    if lettre.lower() == v :
        test = True
for c in consonnes :
    if lettre.lower() == c :
        test2 = True        
if test :
    print('Voyelle : ', lettre)
elif test2 :
    print('Consonne : ', lettre)
else :
    print("Pas une lettre de l'alphabet")

print('a' in voyelles)

