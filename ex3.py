import random
jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi']
print(jours)
print(jours[0], ' ', jours[-1])
print(jours[3])
jours[-2] = 'Dimanche'
tmp = jours[0]
jours[0] = jours[-1]
jours[-1] = tmp
print(jours)      
print('**********************')
exo = [10, 20, 30 ,40]
exo.append(50)
del(exo[0])
exo.remove(40)
exo.append(55)
print(exo[0] + exo[1])
if exo[0] > exo[-1] :
    print('Le premier nombre est plus grand que le dernier de la liste')
print('**********************')
bla = "Ceci est un test"
blabla = []
value = ""
i = 0
for l in bla :
    if l == " " :
        blabla.append(value)
        value = ""
    elif i == len(bla) -1 :
        value += l
        blabla.append(value)
    else :
        value += l
    i += 1
print(blabla)    
print('**********************')
eleves = ['yolan', 'yohann', 'joachim', 'diana', 'jerome']
print(eleves)
random.shuffle(eleves)
print(eleves)    
print('**********************')
numbers = []
for i in range(0, 30) :
    numbers.append(random.randint(0, 200))
print(numbers)    
action = input('Action (ajouter, supprimer) : ')
if action.lower() == 'ajouter' :    
    inp = int(input('Nombre : '))
    inp2 = int(input('Position : '))

    if inp2 > len(numbers) :
        print('Position invalide')
    else :
        numbers.insert(inp2, inp)
        print(numbers)
else :
    inp3 = int(input('Nombre a supprimer: '))
    if inp3 in numbers :
        numbers.remove(inp3)
        print(numbers)
    else :
        print('Erreur')
