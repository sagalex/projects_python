import math

PAR = [2, 3, 4]

PI = math.pi

def dobra_lista(plista):
    return [x*2 for x in plista]

def multiplica(plista):
    r = 1
    for i in plista:
        r *= i
    return r    

plista = [1, 2, 3, 4]

if __name__ == '__main__':
    print(dobra_lista(plista))
    print(multiplica(plista))
    print(PI)
    print(__name__)
    print(PAR)