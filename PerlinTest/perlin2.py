import numpy
from opensimplex import OpenSimplex
import cv2
import math
import random

altura = 800
largura = 800
seed = 885
simplex = OpenSimplex(seed=seed)
lado = 5

def noise(nx, ny, v=7):
    return simplex.noise2d(v * nx, v * ny) / 2.0 + 0.5

def ridgenoise(nx, ny):
    return 2 * (0.5 - abs(0.5 - noise(nx, ny, 40)))


elevacao = [[0 for i in range(largura)] for j in range(altura)]
dist = lado * 2
cx = largura / 2 / largura - 0.5
cy = altura / 2 / altura - 0.5

for i in range(altura):
    for j in range(largura):
        nx = j/largura - 0.5
        ny = i/altura - 0.5
        
        d = math.sqrt(math.pow(nx - cx, 2) + math.pow(ny - cy, 2))
        d = math.pow(d, 0.7)

        e = 1 * noise(nx, ny) + 0.5 * noise(2 * nx, 2 * ny) + 0.25 * noise(4 * nx, 4 * ny) + 0.125 * noise(8 * nx, 8 * ny) + 0.0625 * noise(16 * nx, 16 * ny)
        e = e / (1 + 0.5 + 0.25 + 0.125 + 0.0625)

        elevacao[i][j] = (1 + e - d) / 2


seed = 1156
simplex = OpenSimplex(seed=seed)

umidade = [[0 for i in range(largura)] for j in range(altura)]
for i in range(altura):
    for j in range(largura):
        nx = j/largura - 0.5
        ny = i/altura - 0.5
        e = 1 * noise(nx, ny) + 0.5 * noise(2 * nx, 2 * ny) + 0.25 * noise(4 * nx, 4 * ny) + 0.125 * noise(8 * nx, 8 * ny) + 0.0625 * noise(16 * nx, 16 * ny)
        e = e / (1 + 0.5 + 0.25 + 0.125 + 0.0625)
        umidade[i][j] = e

"""seed = 123
simplex = OpenSimplex(seed=seed)
rios = [[0 for i in range(largura)] for j in range(altura)]
for i in range(altura):
    for j in range(largura):
        nx = j/largura - 0.5
        ny = i/altura - 0.5
        e0 = ridgenoise(nx, ny)
        #e1 = 0.5 * ridgenoise(2 * nx, 2 * ny) * e0
        #e2 = 0.25 * ridgenoise(4 * nx, 4 * ny) * e1
        #e = (e0 + e1) / (1 + 0.5)
        a = math.pow(e0, 2)

        if a > 0.88:
            rios[i][j] = 1
        else:
            rios[i][j] = 0"""


img = numpy.zeros((altura, largura, 1), numpy.uint8)
img2 = numpy.zeros((altura, largura, 1), numpy.uint8)
img3 = numpy.zeros((altura, largura, 3), numpy.uint8)
img4 = numpy.zeros((altura, largura, 3), numpy.uint8)

for i in range(altura):
    for j in range(largura):
        img[i][j] = elevacao[i][j] * 255
        img2[i][j] = umidade[i][j] * 255

        if elevacao[i][j] < 0.47:
            img3[i][j] = [120, 60, 30]
        elif elevacao [i][j] < 0.50:
            img3[i][j] = [150, 120, 0]
        elif elevacao[i][j] < 0.51:
            img3[i][j] = [0, 150, 190]

        elif elevacao[i][j] < 0.57:
            if umidade[i][j] < 0.35:
                img3[i][j] = [0, 150, 190]
            elif umidade[i][j] < 0.60:
                img3[i][j] = [0, 120, 80]
            else:
                img3[i][j] = [0, 100, 70]

        elif elevacao[i][j] < 0.68:
            if umidade[i][j] < 0.42:
                img3[i][j] = [0, 120, 140]
            elif umidade[i][j] < 0.60:
                img3[i][j] = [0, 70, 30]
            else:
                img3[i][j] = [25, 60, 30]

        elif elevacao[i][j] < 0.73:
            img3[i][j] = [100, 100, 100]
        
        elif elevacao[i][j] < 0.76:
            img3[i][j] = [150, 150, 150]

        else:
            img3[i][j] = [255, 255, 255]

        

        if elevacao[i][j] < 0.51:
             img4[i][j] = [120, 60, 30]

        elif elevacao[i][j] < 0.55:
            img4[i][j] = [100, 100, 100]
        
        elif elevacao[i][j] < 0.60:
            img4[i][j] = [115, 115, 115]
        
        elif elevacao[i][j] < 0.65:
            img4[i][j] = [130, 130, 130]
        
        elif elevacao[i][j] < 0.70:
            img4[i][j] = [145, 145, 145]
        
        elif elevacao[i][j] < 0.75:
            img4[i][j] = [160, 160, 160]
        
        elif elevacao[i][j] < 0.80:
            img4[i][j] = [175, 175, 175]
        
        elif elevacao[i][j] < 0.85:
            img4[i][j] = [200, 200, 200]
        
        elif elevacao[i][j] < 0.90:
            img4[i][j] = [225, 225, 225]
        
        else:
            img4[i][j] = [255, 255, 255]


        """if matriz[i][j] < 0.47:
            img2[i][j] = [120, 60, 30]
        elif matriz[i][j] < 0.50:
            img2[i][j] = [150, 120, 0]
        elif matriz[i][j] < 0.51:
            img2[i][j] = [0, 150, 190]
        elif matriz[i][j] < 0.56:
            img2[i][j] = [0, 150, 80]
        elif matriz[i][j] < 0.65:
            img2[i][j] = [0, 100, 0]
        elif matriz[i][j] < 0.72:
            img2[i][j] = [0, 70, 140]
        elif matriz[i][j] < 0.80:
            img2[i][j] = [150, 150, 150]
        else:
            img2[i][j] = [255, 255, 255]"""


aux = [[0 for i in range(largura)] for j in range(altura)]

for i in range(300):
    x = random.randint(100, largura - 100)
    y = random.randint(100, altura - 100)
    
    w = 0
    z = 0

    direcao = random.randint(1, 8)
    xant = -1
    yant = -1
    minel = 10;
    cont = 0

    while True:
        cont += 1
        """if cont >= 65:
            cont = 0
            direcao = random.randint(1, 8)"""

        minel = 10
        xpro = 0
        ypro = 0

        """if xpro == 1 and ypro == 0:
            direcao = 1
        
        elif xpro == 1 and ypro == 1:
            direcao = 2
        
        elif xpro == 0 and ypro == 1:
            direcao = 3
        
        elif xpro == -1 and ypro == 1:
            direcao = 4

        elif xpro == -1 and ypro == 0:
            direcao = 5

        elif xpro == -1 and ypro == -1:
            direcao = 6

        elif xpro == 0 and ypro == -1:
            direcao = 7

        elif xpro == 1 and ypro == -1:
            direcao = 8

        else:
            direcao = 1"""

        if elevacao[x][y] < 0.50 or elevacao[x][y] > 0.68 or aux[x][y] == 1:
            break
        
        else:
            img4[x][y] = [150, 120, 0]
            img3[x][y] = [150, 120, 0]
            aux[x][y] = 1

            if direcao == 1:
                w = random.randint(1, 1) 
                z = random.randint(-1, 1)

            elif direcao == 2:
                a = random.randint(1, 2)
                b = random.randint(0, 1)

                w = 1
                z = 1

                if a == 1:
                    w -= b
                else:
                    z -= b

            elif direcao == 3:
                w = random.randint(-1, 1) 
                z = random.randint(1, 1)

            elif direcao == 4:
                a = random.randint(1, 2)
                b = random.randint(0, 1)

                w = -1
                z = 1

                if a == 1:
                    w += b
                else:
                    z -= b
            
            elif direcao == 5:
                w = random.randint(-1, -1) 
                z = random.randint(-1, 1)
            
            elif direcao == 6:
                a = random.randint(1, 2)
                b = random.randint(0, 1)

                w = -1
                z = -1

                if a == 1:
                    w += b
                else:
                    z += b

            elif direcao == 7:
                w = random.randint(-1, 1) 
                z = random.randint(-1, -1)

            elif direcao == 8:
                a = random.randint(1, 2)
                b = random.randint(0, 1)

                w = 1
                z = -1

                if a == 1:
                    w -= b
                else:
                    z += b

            if x + w != xant and y + y != yant and x + w >= 0 and x + w < largura and y + z >= 0 and y + z < altura:
                x += w
                y += z


cv2.imwrite('perlin_a.png', img)
cv2.imwrite('perlin_b.png', img2)
cv2.imwrite('perlin_color.png', img3)
cv2.imwrite('perlin_c.png', img4)