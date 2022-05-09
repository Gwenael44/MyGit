for i in range(10):
    print("J'aime programmer avec Python !")
print('************************')
animaux = ['baleine', 'chien', 'chat', 'brebis', 'loup']
for a in animaux :
    print(a)
for i in range(len(animaux)):
    print(animaux[i], ' ', i)
print('************************')
a = 0
while a <= 10:
    a += 1
b = 0
while b != 10:
    b = int(input('Nombre : '))
print('************************')
c = 55
d = 0
while d != c:
    d = int(input('Nombre : '))
    if d < c:
        print('Trop petit')
    if d > c:
        print('Trop grand')
print('************************')
in1 = int(input('Largueur : '))
in2 = int(input('Longueur : '))
char = input('Character : ' )
for i in range(in2):
    print(char * in1)
print('************************')
long = int(input('longueur : '))
sapin = '@'
blank = ' '
for n in range(long) :
           print(blank * long + sapin + blank * long)
           sapin += '@@'
           long -= 1
print('************************')
long = int(input('longueur : '))
longx = long *3
sapin = '@'
blank = ' '
for n in range(long) :
           print(blank * longx + sapin + blank * longx)
           sapin += '@@'
           longx -= 1
sapin = '@'
longs = long * 2 - 1
for n in range(long) :
           print(blank * longx + sapin + blank * longs + sapin + blank * longx)
           sapin += '@@'
           longx -= 1
           longs -= 2

           
