import pymunk as pm
from pymunk import Vec2d

# Creazione classe "pall1" + piccola parentesi sulla fionda
class pall1():
    def __init__(self, distanza, angoli, x, y, spazio):
        self.vita = 25
        massa = 6
        radius = 15
        inerzia = pm.moment_for_circle(massa, 0, radius, (10, 0))
        corpo = pm.Body(massa, inerzia)
        corpo.position = x, y
        potenza = distanza * 50
        impulso = potenza * Vec2d(1, 0)
        angoli = -angoli
        corpo.apply_impulse_at_local_point(impulso.rotated(angoli))
        forma = pm.Circle(corpo, radius, (0, 0))
        forma.elasticity = 1
        forma.friction = 1
        forma.collision_type = 0
        spazio.add(corpo, forma)
        self.corpo = corpo
        self.forma = forma

# Creazione classe "Maiali"
class Maiali():
    def __init__(self, x, y, spazio):
        self.life = 20
        mass = 5
        radius = 14
        inerzia = pm.moment_for_circle(mass, 0, radius, (0, 0))
        corpo = pm.Body(mass, inerzia)
        corpo.position = x, y
        forma = pm.Circle(corpo, radius, (0, 0))
        forma.elasticity = 0.50
        forma.friction = 0.50
        forma.collision_type = 1
        spazio.add(corpo, forma)
        self.corpo = corpo
        self.forma = forma
