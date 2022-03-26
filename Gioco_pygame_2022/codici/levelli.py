from charattere import Maiali
from Poligono import Poligono

# Creazione classe "Levelli" in manier molto generale
class Levelli():
    def __init__(self, maiali, colonne, travi, spazio):
        self.maiali = maiali
        self.colonne = colonne
        self.travi = travi
        self.spazio = spazio
        self.number = 1
        self.number_of_birds = 5
        
# Creazione schermata partita vincente
        self.stella1 = 30000
        self.stella2 = 40000
        self.stella3 = 60000
        self.bool_space = False

# Creazione di una struttura piatta aperta grazie alla creazione della classe "Struttura_piatta_aperta"
    def Struttura_piatta_aperta(self, x, y, n):
        y0 = y
        for i in range(n):
            y = y0+100+i*100
            p = (x, y)
            self.colonne.append(Poligono(p, 20, 85, self.spazio))
            p = (x+60, y)
            self.colonne.append(Poligono(p, 20, 85, self.spazio))
            p = (x+30, y+50)
            self.travi.append(Poligono(p, 85, 20, self.spazio))

# Creazione di una pila orizzontale grazie alla classe "pila_orrizontale"
    def pila_orrizontale(self, x, y, n):
        y += 70
        for i in range(n):
            p = (x, y+i*20)
            self.travi.append(Poligono(p, 85, 20, self.spazio))

# Creazione di una pila verticale grazie alla classe "pila_verticale"
    def pila_verticale(self, x, y, n):
        y += 10
        for i in range(n):
            p = (x, y+85+i*85)
            self.colonne.append(Poligono(p, 20, 85, self.spazio))

# Livello 0
    def build_0(self):
        pig1 = Maiali(1000, 120, self.spazio)
        pig2 = Maiali(1005, 182, self.spazio)
        self.maiali.append(pig1)
        self.maiali.append(pig2)
        p = (980, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1030, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1000, 170)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (970, 220)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1030, 220)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1000, 260)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8
        self.stella1 = 30000
        self.stella2 = 40000
        self.stella3 = 60000

    def build_1(self):
        """livello 1"""
        pig1 = Maiali(880, 180, self.spazio)
        self.maiali.append(pig1)
        pig2 = Maiali(1000, 230, self.spazio)
        self.maiali.append(pig2)
        p = (880, 80)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (880, 150)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (1000, 80)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1000, 180)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1000, 210)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_2(self):
        """livello 2"""
        pig = Maiali(950, 320, self.spazio)
        pig.life = 15
        self.maiali.append(pig)
        pig = Maiali(885, 225, self.spazio)
        pig.life = 20
        self.maiali.append(pig)
        pig = Maiali(1005, 225, self.spazio)
        pig.life = 25
        self.maiali.append(pig)
        p = (1100, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1070, 152)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (1040, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (980, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (920, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (950, 152)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (1010, 180)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (860, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (800, 100)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (830, 152)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (890, 180)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (860, 223)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (920, 223)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (980, 223)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (1040, 223)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (890, 280)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (1010, 280)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (950, 300)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        p = (920, 350)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (980, 350)
        self.colonne.append(Poligono(p, 20, 85, self.spazio))
        p = (950, 400)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8

    def build_3(self):
        """livello 3"""
        pig = Maiali(1050, 180, self.spazio)
        pig.life = 20
        self.maiali.append(pig)
        pig = Maiali(900, 180, self.spazio)
        pig.life = 20
        self.maiali.append(pig)
        self.Struttura_piatta_aperta(1050, 0, 3)
        self.Struttura_piatta_aperta(963, 0, 2)
        self.Struttura_piatta_aperta(880, 0, 2)
        self.Struttura_piatta_aperta(790, 0, 3)
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8


    def build_4(self):
        """livello 4"""
        pig = Maiali(820, 177, self.spazio)
        self.maiali.append(pig)
        pig = Maiali(960, 150, self.spazio)
        self.maiali.append(pig)
        pig = Maiali(1100, 130, self.spazio)
        self.maiali.append(pig)
        pig = Maiali(890, 270, self.spazio)
        pig.life = 20
        self.maiali.append(pig)
        self.pila_orrizontale(800, 0, 5)
        self.pila_orrizontale(950, 0, 3)
        self.pila_orrizontale(1100, 0, 2)
        self.pila_verticale(745, 0, 2)
        self.pila_verticale(855, 0, 2)
        self.pila_verticale(900, 0, 2)
        self.pila_verticale(1000, 0, 2)
        p = (875, 230)
        self.travi.append(Poligono(p, 85, 20, self.spazio))
        self.number_of_birds = 4
        if self.bool_space:
            self.number_of_birds = 8
    

    def load_level(self):
        try:
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
        except AttributeError:
            self.number = 0
            build_name = "build_"+str(self.number)
            getattr(self, build_name)()
