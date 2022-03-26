import pymunk as pm
from pymunk import Vec2d
import pygame
import math

# Parametri generali dei poligoni utilizzati pr la costruzione delle strutture da abbattere
class Poligono():
    def __init__(self, posizione, lunghezza, altezza, spazio, massa=3.7):
        momento = 1000
        corpo = pm.Body(massa, momento)
        corpo.position = Vec2d(*posizione)
        forma = pm.Poly.create_box(corpo, (lunghezza, altezza))
        forma.color = (0, 0, 255)
        forma.friction = 0.5
        forma.collision_type = 2
        spazio.add(corpo, forma)
        self.body = corpo
        self.shape = forma
        legno = pygame.image.load("../resources/images/wood.png").convert_alpha()
        legno2 = pygame.image.load("../resources/images/wood2.png").convert_alpha()
        retta = pygame.Rect(251, 357, 86, 22)
        self.beam_image = legno.subsurface(retta).copy()
        retta = pygame.Rect(16, 252, 22, 84)
        self.column_image = legno2.subsurface(retta).copy()

# Converione cordinate pymunk a cordinate per pygame
    def to_pygame(self, p):
        return int(p.x), int(-p.y+600)

# Disegno le travi e le colonne generali
    def disegnare_poli(self, elemento, schermo):
        poli = self.shape
        ps = poli.get_vertices()
        ps.append(ps[0])
        ps = map(self.to_pygame, ps)
        ps = list(ps)
        colore = (255, 0, 0)
        pygame.draw.lines(schermo, colore, False, ps)

# Completamento travi
        if elemento == 'travi':
            p = poli.body.position
            p = Vec2d(*self.to_pygame(p))
            gradi_angoli = math.degrees(poli.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.beam_image,
                                                       gradi_angoli)
            offset = Vec2d(*rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            schermo.blit(rotated_logo_img, (np.x, np.y))

# Completamento colonne
        if elemento == 'colonne':
            p = poli.body.position
            p = Vec2d(*self.to_pygame(p))
            gradi_angoli = math.degrees(poli.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.column_image,
                                                       gradi_angoli)
            offset = Vec2d(*rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            schermo.blit(rotated_logo_img, (np.x, np.y))
