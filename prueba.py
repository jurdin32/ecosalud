import math

def solution(puntos):
    suma1=0
    suma2=0
    total=0
    x=0
    y=0
    for p in range(len(puntos)):
        try:
            if p==1:
                x= abs(puntos[p][0])
                y=abs(puntos[p+1][0])
                suma1+=x+y
            else:
                suma1 += abs(puntos[p+1][0])
            if p==1:
                a=abs(puntos[p][1])
                b=abs(puntos[p+1][1])
            else:
                suma2+=abs(puntos[p+1][1])
            print(suma1,suma2)
        except:
            pass
    total=math.pow(suma1,2)+math.pow(suma2,2)
    return math.sqrt(total,2)

p = [[0, 11], [-7, 1], [-5, -3]]
print(solution(p))


