import numpy
from opensimplex import OpenSimplex
import cv2
import pygame
import math

altura = 800;
largura = 1200;
se = 998209697;
simplex = OpenSimplex(seed=se)
lado = 5

def noise(nx, ny):
    return simplex.noise2d(10 * nx, 10 * ny) / 2.0 + 0.5


class Hexagon():
    def __init__(self, cx, cy, cor):
        self.cx = cx
        self.cy = cy
        self.cor = cor
        self.lado = lado
        self.pontos = []
        self.pontosext = []
        self.definir_vertices()
    
    def definir_vertices(self):
        self.pontos.append((self.cx + self.lado * math.sin(math.pi / 2), self.cy + self.lado * math.cos(math.pi / 2)))
        self.pontos.append((self.cx + self.lado * math.sin(math.pi / 6), self.cy + self.lado * math.cos(math.pi / 6)))
        self.pontos.append((self.cx + self.lado * math.sin(11 * math.pi / 6), self.cy + self.lado * math.cos(11 * math.pi / 6)))
        self.pontos.append((self.cx + self.lado * math.sin(3 * math.pi / 2), self.cy + self.lado * math.cos(3 * math.pi / 6)))
        self.pontos.append((self.cx + self.lado * math.sin(7 * math.pi / 6), self.cy + self.lado * math.cos(7 * math.pi / 6)))
        self.pontos.append((self.cx + self.lado * math.sin(5 * math.pi / 6), self.cy + self.lado * math.cos(5 * math.pi / 6)))

        self.pontosext.append((self.cx + self.lado * math.sin(math.pi / 2), self.cy + self.lado * math.cos(math.pi / 2)))
        self.pontosext.append((self.cx + self.lado * math.sin(math.pi / 6), self.cy + self.lado * math.cos(math.pi / 6)))
        self.pontosext.append((self.cx + self.lado * math.sin(11 * math.pi / 6), self.cy + self.lado * math.cos(11 * math.pi / 6)))
        self.pontosext.append((self.cx + self.lado * math.sin(3 * math.pi / 2), self.cy + self.lado * math.cos(3 * math.pi / 6)))
        self.pontosext.append((self.cx + self.lado * math.sin(7 * math.pi / 6), self.cy + self.lado * math.cos(7 * math.pi / 6)))
        self.pontosext.append((self.cx + self.lado * math.sin(5 * math.pi / 6), self.cy + self.lado * math.cos(5 * math.pi / 6)))

    def desenhar(self, tela):
        pygame.draw.polygon(tela, self.cor, self.pontos)
        pygame.draw.polygon(tela, (0, 0, 0), self.pontosext, width=2)




matriz = [[0 for i in range(largura)] for j in range(altura)]
lista = []
dist = lado * 2
curdistx = 0
curdisty = 0
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

        matriz[i][j] = (1 + e - d) / 2

        #matriz[i][j] = e

img = numpy.zeros((altura, largura, 1), numpy.uint8)
img2 = numpy.zeros((altura, largura, 3), numpy.uint8)

for i in range(altura):
    if i % 2 == 0:
        curdistx = 0
    else:
        curdistx = lado + lado / 2

    for j in range(largura):
        img[i][j] = matriz[i][j] * 255

        if matriz[i][j] < 0.47:
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
            img2[i][j] = [255, 255, 255]

        """if matriz[i][j] < 0.50:
            obj = Hexagon(curdistx, curdisty, [30, 60, 120])
        elif matriz[i][j] < 0.54:
            obj = Hexagon(curdistx, curdisty, [0, 120, 150])
        elif matriz[i][j] < 0.56:
            obj = Hexagon(curdistx, curdisty, [190, 150, 0])
        elif matriz[i][j] < 0.60:
            obj = Hexagon(curdistx, curdisty, [80, 150, 0])
        elif matriz[i][j] < 0.70:
            obj = Hexagon(curdistx, curdisty, [0, 100, 0])
        elif matriz[i][j] < 0.75:
            obj = Hexagon(curdistx, curdisty, [140, 70, 0])
        elif matriz[i][j] < 0.80:
            obj = Hexagon(curdistx, curdisty, [150, 150, 150])
        else:
            obj = Hexagon(curdistx, curdisty, [255, 255, 255])
        
        lista.append(obj)"""

        curdistx += lado * 3

    curdisty += lado * math.sqrt(3) / 2


cv2.imwrite('perlin.png', img)
cv2.imwrite('perlin_color.png', img2)
#cv2.imwrite('perlin_c.png', img3)


"""pygame.init()
screen = pygame.display.set_mode((1600, 900))
running = True

poli = Hexagon(150, 150, (150, 150, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))

    for hexa in lista:
        hexa.desenhar(screen)

    pygame.display.flip()

pygame.quit()"""
