import random
def lanceDes(nb):
    des = [1, 2, 3, 4, 5, 6]
    combinaison = [[1], [2], [3], [4], [5], [6]]
    result = 0;
    found = False
    for i in range(nb) :
          result += random.randint(1,6)
    for d in des :
        for de in des :
            if d + de == result :
                found = True
                if d == 1 :
                    combinaison[0].append(de)     
                elif d == 2 :
                    combinaison[1].append(de)
                elif d == 3 :
                    combinaison[2].append(de)
                elif d == 4 :
                    combinaison[3].append(de)
                elif d == 5 :
                    combinaison[4].append(de)
                elif d == 6 :
                    combinaison[5].append(de)

    print('result : ', result)
    for c in range(len(combinaison)) :
        if len(combinaison[c]) > 1 :
            for a in range(1, len(combinaison[c])) :
                print(int(c + 1), ' + ', combinaison[c][a])
    return combinaison, found
comb = lanceDes(2)

