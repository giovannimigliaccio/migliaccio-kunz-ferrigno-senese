from locale import setlocale
import os
import sys
import math
import time
import pygame
current_path = os.getcwd()
import pymunk as pm
from charattere import pall1
from levelli import Levelli

# Inizio creazioni delle variabili utili per il reparto grafico 
pygame.init()
schermo = pygame.display.set_mode((1200, 650))
sprite = pygame.image.load(
    "../resources/images/palla.jpg").convert_alpha()
sfondo2 = pygame.image.load(
    "../resources/images/background1.jpg").convert_alpha()
arma = pygame.image.load(
    "../resources/images/sling-3.png").convert_alpha()
full_sprite = pygame.image.load(
    "../resources/images/full-sprite.png").convert_alpha()
retta = pygame.Rect(181, 1050, 50, 50)
cropped = full_sprite.subsurface(retta).copy()
nemico_immagine = pygame.transform.scale(cropped, (30, 30))
bottone = pygame.image.load(
    "../resources/images/selected-buttons.png").convert_alpha()
immagine_sconfitta = pygame.image.load(
    "../resources/images/pig_failed.png").convert_alpha()
immagine_vittoria = pygame.image.load(
    "../resources/images/stars-edited.png").convert_alpha()
retta = pygame.Rect(0, 0, 200, 200)
stella1 = immagine_vittoria.subsurface(retta).copy()
retta = pygame.Rect(204, 0, 200, 200)
stella2 = immagine_vittoria.subsurface(retta).copy()
retta = pygame.Rect(426, 0, 200, 200)
stella3 = immagine_vittoria.subsurface(retta).copy()
retta = pygame.Rect(164, 10, 60, 60)
pause_button = bottone.subsurface(retta).copy()
retta = pygame.Rect(24, 4, 100, 100)
replay_button = bottone.subsurface(retta).copy()
retta = pygame.Rect(142, 365, 130, 100)
next_button = bottone.subsurface(retta).copy()
orologio = pygame.time.Clock()
retta = pygame.Rect(18, 212, 100, 100)
play_button = bottone.subsurface(retta).copy()
orologio = pygame.time.Clock()
corsa = True

# Strutturazione della fisica iniziale
spazio = pm.Space()
spazio.gravity = (0.0,-700.0)
maiali = []
palle = []
polys = []
travi = []
colonne = []
numero_palle = 0
distanza_mouse = 0
lunghezza_corda = 90
angolo = 0
x_mouse = 0
y_mouse = 0
contatore = 0
pressione_mouse = False
t1 = 0
tocco_nuovo_cerchio = 10
ROSSO = (255, 0, 0)
BLU = (0, 0, 255)
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
fionda_x, fionda_y = 135, 450
fionda2_x, fionda2_y = 160, 450
score = 0
inizio_gioco = 0
disegno_palla = []
porta_punti = 0
restart_porta_punti = False
punteggio_bonus = True
bold_font = pygame.font.SysFont("arial", 30, bold=True)
bold_font2 = pygame.font.SysFont("arial", 40, bold=True)
bold_font3 = pygame.font.SysFont("arial", 50, bold=True)
muri = True

# Comportamento del terreno
corpi_statici = pm.Body(body_type=pm.Body.STATIC)
line_immobili = [pm.Segment(corpi_statici, (0.0, 060.0), (1200.0, 060.0), 0.0)]
line_immobili1 = [pm.Segment(corpi_statici, (1200.0, 060.0), (1200.0, 800.0), 0.0)]
for linea in line_immobili:
    linea.elasticity = 0.95
    linea.friction = 1
    linea.collision_type = 3
for linea in line_immobili1:
    linea.elasticity = 0.95
    linea.friction = 1
    linea.collision_type = 3
spazio.add(corpi_statici)
for linea in line_immobili:
    spazio.add(linea)

# Converto le cordinate pymunk a pygame
def to_pygame(p):
      return int(p.x), int(-p.y+600)

# Restituisce il vettore dei punti p0 = (xo,yo), p1 = (x1,y1)
def vettore(p0, p1):
    a = p1[0] - p0[0]
    b = p1[1] - p0[1]
    return (a, b)

# Restituisce il vettore unitario dei punti v = (a,b)
def vettori(v):
    h = ((v[0]**2)+(v[1]**2))**0.5
    if h == 0:
        h = 0.000000000000001
    ua = v[0] / h
    ub = v[1] / h
    return (ua, ub)

# Distanza tra punti
def distanza(xo, yo, x, y):
    dx = x - xo
    dy = y - yo
    d = ((dx ** 2) + (dy ** 2)) ** 0.5
    return d

# Base musicale
def musica():
    song1 = '../resources/sounds/da sussare 2.mp3'
    pygame.mixer.music.load(song1)
    pygame.mixer.music.play(-1)

# Attegiamento laccio/corda 
def azione_della_corda():
    global distanza_mouse
    global lunghezza_corda
    global angoli
    global x_mouse
    global y_mouse

# Fissaggio della palla alla fune
    v = vettore((fionda_x, fionda_y), (x_mouse, y_mouse))
    uv = vettori(v)
    uv1 = uv[0]
    uv2 = uv[1]
    distanza_mouse = distanza(fionda_x, fionda_y, x_mouse, y_mouse)
    pu = (uv1*lunghezza_corda+fionda_x, uv2*lunghezza_corda+fionda_y)
    corda_grande = 90
    x_palle = x_mouse - 20
    y_palle = y_mouse - 20
    if distanza_mouse > lunghezza_corda:
        pux, puy = pu
        pux -= 20
        puy -= 20
        pul = pux, puy
        schermo.blit(sprite, pul)
        pu2 = (uv1*corda_grande+fionda_x, uv2*corda_grande+fionda_y)
        pygame.draw.line(schermo, (0, 0, 0), (fionda2_x, fionda2_y), pu2, 5)
        schermo.blit(sprite, pul)
        pygame.draw.line(schermo, (0, 0, 0), (fionda_x, fionda_y), pu2, 5)
    else:
        distanza_mouse += 10
        pu3 = (uv1*distanza_mouse+fionda_x, uv2*+fionda_y)
        pygame.draw.line(schermo, (0, 0, 0), (fionda2_x, fionda2_y), pu3, 5)
        schermo.blit(sprite, (x_palle, y_palle))
        pygame.draw.line(schermo, (0, 0, 0), (fionda_x, fionda_y), pu3, 5)

# Forza del angolo
    dy = y_mouse - fionda_y
    dx = x_mouse - fionda_x
    if dx == 0:
        dx = 0.00000000000001
    angoli = math.atan((float(dy))/dx)

# In caso di vincita
def partita_pulita():
    global inizio_gioco
    global punteggio_bonus
    global score
    livello_pulito = bold_font3.render("livello superato! xD ", 1, BIANCO)
    score_level_cleared = bold_font2.render(str(score), 1, BIANCO)
    if livello.number_of_birds >= 0 and len(maiali) == 0:
        if punteggio_bonus:
            score += (livello.number_of_birds-1) * 10000
        punteggio_bonus = False
        inizio_gioco = 4
        rect = pygame.Rect(300, 0, 600, 800)
        pygame.draw.rect(schermo, NERO, rect)
        schermo.blit(livello_pulito, (450, 90))
        if score >= livello.stella1 and score <= livello.stella2:
            schermo.blit(stella1, (310, 190))
        if score >= livello.stella2 and score <= livello.stella3:
            schermo.blit(stella1, (310, 190))
            schermo.blit(stella2, (500, 170))
        if score >= livello.stella3:
            schermo.blit(stella1, (310, 190))
            schermo.blit(stella2, (500, 170))
            schermo.blit(stella3, (700, 200))
        schermo.blit(score_level_cleared, (550, 400))
        schermo.blit(replay_button, (510, 480))
        schermo.blit(next_button, (620, 480))

# In caso di perdita
def lievllo_perso():
    global inizio_gioco
    perdita = bold_font3.render("Hai perso! :P ", 1, ROSSO)
    if livello.number_of_birds <= 0 and time.time() - t2 > 5 and len(maiali) > 0:
        inizio_gioco = 3
        retta = pygame.Rect(300, 0, 600, 800)
        pygame.draw.rect(schermo, NERO, rect)
        schermo.blit(perdita, (450, 90))
        schermo.blit(immagine_sconfitta, (380, 120))
        schermo.blit(replay_button, (520, 460))

# In caso di perdita 2
def restart():
    maiali_da_rimuovere = []
    palle_da_rimuovere = []
    colonne_da_rimuovere = []
    travi_da_rimuovere = []
    for maiale in maiali:
        maiali_da_rimuovere.append(maiale)
    for maiale in maiali_da_rimuovere:
        spazio.remove(maiale.forma, maiale.forma.body)
        maiali.remove(maiale)
    for bird in palle:
        palle_da_rimuovere.append(bird)
    for bird in palle_da_rimuovere:
        spazio.remove(bird.forma, bird.forma.body)
        palle.remove(bird)
    for colonna in colonne:
        colonne_da_rimuovere.append(colonna)
    for colonna in colonne_da_rimuovere:
        spazio.remove(colonna.shape, colonna.shape.body)
        colonne.remove(colonna)
    for trave in travi:
        travi_da_rimuovere.append(trave)
    for trave in travi_da_rimuovere:
        spazio.remove(trave.shape, trave.shape.body)
        travi.remove(trave)

# Contatto tra maiale e palla
def post_contatto1(arbitro, spazi, _):
    superficie=schermo
    a, b = arbitro.shapes
    corpo_palla = a.body
    corpo_maiale = b.body
    p = to_pygame(corpo_palla.position)
    p2 = to_pygame(corpo_maiale.position)
    r = 30
    pygame.draw.circle(superficie, NERO, p, r, 4)
    pygame.draw.circle(superficie, ROSSO, p2, r, 4)
    mailali_da_rimuovere = []
    for maiale in maiali:
        if corpo_maiale == maiale.corpo:
            maiale.life -= 20
            mailali_da_rimuovere.append(maiale)
            global score
            score += 10000
    for maiale in mailali_da_rimuovere:
        spazi.remove(maiale.forma, maiale.forma.body)
        maiali.remove(maiale)

# Collisione palla e legno
def post_contatto2(arbitro, spazio, _):
    poli_da_rimuovere = []
    if arbitro.total_impulse.length > 1100:
        a, b = arbitro.shapes
        for column in colonne:
            if b == column.shape:
                poli_da_rimuovere.append(column)
        for beam in travi:
            if b == beam.shape:
                poli_da_rimuovere.append(beam)
        for poli in poli_da_rimuovere:
            if poli in colonne:
                colonne.remove(poli)
            if poli in travi:
                travi.remove(poli)
        spazio.remove(b, b.body)
        global score
        score += 5000

# Collisione tra il maiale e il legno
def post_contatto3(arbitro, spazio, _):
    mailali_da_rimuovere = []
    if arbitro.total_impulse.length > 700:
        maiale_forma, wood_forma = arbitro.shapes
        for maiale in maiali:
            if maiale_forma == maiale.forma:
                maiale.life -= 20
                global score
                score += 10000
                if maiale.life <= 0:
                    mailali_da_rimuovere.append(maiale)
    for maiale in mailali_da_rimuovere:
        spazio.remove(maiale.forma, maiale.forma.body)
        maiali.remove(maiale)

# Gestione delle collisioni + gestione della musica
# Palle e maiali
spazio.add_collision_handler(0, 1).post_solve=post_contatto1
# Palle e legno
spazio.add_collision_handler(0, 2).post_solve=post_contatto2
# Maiali e legno
spazio.add_collision_handler(1, 2).post_solve=post_contatto3
musica()
livello = Levelli(maiali, colonne, travi, spazio)
livello.number = 0
livello.load_level()

# Parametri input per i "personaggi"
while corsa:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corsa = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
            corsa = False
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_w:

# Gestione della gravità tasto "E" no gravitè mentre "R" ritorna allostato iniziale
            if wall:
                for line1 in line_immobili1:
                    spazio.remove(line1)
                wall = False
            else:
                for line1 in line_immobili1:
                    spazio.add(line1)
                wall = True

# Assegnamenti tasti già citati 
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_e:
            spazio.gravity = (0.0, 0.0)
            livello.bool_space = True
        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_r:
            spazio.gravity = (0.0, -700.0)
            livello.bool_space = False
        if (pygame.mouse.get_pressed()[0] and x_mouse > 100 and
                x_mouse < 250 and y_mouse > 370 and y_mouse < 550):
            pressione_mouse = True
        if (evento.type == pygame.MOUSEBUTTONUP and
                evento.button == 1 and pressione_mouse):

# Rilascia di una nuova palla
            pressione_mouse = False
            if livello.number_of_birds > 0:
                livello.number_of_birds -= 1
                t1 = time.time()*1000
                xo = 150
                yo = 152
                if distanza_mouse > lunghezza_corda:
                    distanza_mouse = lunghezza_corda
                if x_mouse < fionda_x+5:
                    pall0 = pall1(distanza_mouse, angoli, xo, yo, spazio)
                    palle.append(pall0)
                else:
                    pall0 = pall1(-distanza_mouse, angoli, xo, yo, spazio)
                    palle.append(pall0)
                if livello.number_of_birds == 0:
                    t2 = time.time()
        if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
            if (x_mouse < 60 and y_mouse < 155 and y_mouse > 90):
                inizio_gioco = 1
            if inizio_gioco == 1:
                if x_mouse > 500 and y_mouse > 200 and y_mouse < 300:

# Gestione completa schermata di pausa
                    inizio_gioco = 0
                if x_mouse > 500 and y_mouse > 300:

# Restrt partita ma non ancora fallita
                    restart()
                    livello.load_level()
                    inizio_gioco = 0
                    disegno_palla = []
            if inizio_gioco == 3:

# Restart partita fallita
                if x_mouse > 500 and x_mouse < 620 and y_mouse > 450:
                    restart()
                    livello.load_level()
                    inizio_gioco = 0
                    disegno_palla = []
                    score = 0
            if inizio_gioco == 4:

 # Passagio al nuovo livello
                if x_mouse > 610 and y_mouse > 450:
                    restart()
                    livello.number += 1
                    inizio_gioco = 0
                    livello.load_level()
                    score = 0
                    disegno_palla = []
                    punteggio_bonus = True
                if x_mouse < 610 and x_mouse > 500 and y_mouse > 450:

# Azzeramento punteggio della scorsa partita
                    restart()
                    livello.load_level()
                    inizio_gioco = 0
                    disegno_palla = []
                    score = 0
    x_mouse, y_mouse = pygame.mouse.get_pos()

# Creazione dello sfondo che prende dalla cartella "immagini"
    schermo.fill((130, 200, 100))
    schermo.blit(sfondo2, (0, -50))

# inizializzazione della fionda
    rect = pygame.Rect(50, 0, 70, 220)
    schermo.blit(arma, (138, 420), rect)

# Disegno del perscorso della palla
    for punto in disegno_palla:
        pygame.draw.circle(schermo, BIANCO, punto, 5, 0)

# Mette le palle in basso a destra in fila indiana
    if livello.number_of_birds > 0:
        for i in range(livello.number_of_birds-1):
            x = 100 - (i*35)
            schermo.blit(sprite, (x, 508))

# Completamento del attegiamento della fionda
    if pressione_mouse and livello.number_of_birds > 0:
        azione_della_corda()
    else:
        if time.time()*1000 - t1 > 300 and livello.number_of_birds > 0:
            schermo.blit(sprite, (130, 426))
        else:
            pygame.draw.line(schermo, (0, 0, 0), (fionda_x, fionda_y-8),
                             (fionda2_x, -7), 5)
    palle_da_rimuovere = []
    mailali_da_rimuovere = []
    porta_punti += 1

# Completamento delle palle
    for palla in palle:
        if palla.forma.body.position.y < 0:
            palle_da_rimuovere.append(palla)
        p = to_pygame(palla.forma.body.position)
        x, y = p
        x -= 22
        y -= 20
        schermo.blit(sprite, (x, y))
        pygame.draw.circle(schermo, BLU,
                           p, int(pall0.forma.radius), 2)

# Gestione del tempo
        if porta_punti >= 3 and time.time() - t1 < 5:
            disegno_palla.append(p)
            restart_porta_punti = True
    if restart_porta_punti:
        porta_punti = 0
        restart_porta_punti = False

# Rimozione delle palle e dei maiali
    for pall0 in palle_da_rimuovere:
        spazio.remove(pall0.forma, pall0.forma.body)
        palle.remove(pall0)
    for maiale in mailali_da_rimuovere:
        spazio.remove(maiale.forma, maiale.forma.body)
        maiali.remove(maiale)

# Completamento linee statiche
    for line1 in line_immobili:
        corpo = line1.body
        pv1 = corpo.position + line1.a.rotated(corpo.angle)
        pv2 = corpo.position + line1.b.rotated(corpo.angle)
        p1 = to_pygame(pv1)
        p2 = to_pygame(pv2)
        pygame.draw.lines(schermo, (150, 150, 150), False, [p1, p2])
    i = 0

# Completamento maiali
    for maiale in maiali:
        i += 1
        maiale = maiale.forma
        if maiale.body.position.y < 0:
            mailali_da_rimuovere.append(maiale)

        p = to_pygame(maiale.body.position)
        x, y = p

        angolo_gradi = math.degrees(maiale.body.angle)
        img = pygame.transform.rotate(nemico_immagine, angolo_gradi)
        w,h = img.get_size()
        x -= w*0.5
        y -= h*0.5
        schermo.blit(img, (x, y))
        pygame.draw.circle(schermo, BLU, p, int(maiale.radius), 2)

# Posizionamento colonne e travi
    for colonna in colonne:
        colonna.disegnare_poli('colonne', schermo)
    for trave in travi:
        trave.disegnare_poli('travi', schermo)
        
# Modificazione di alcuni parametri fisici per migliorare la stabibilità 
    dt = 1.0/50.0/2.
    for x in range(2):
        spazio.step(dt)
    
# Completamento della fionda
    rect = pygame.Rect(0, 0, 60, 200)
    schermo.blit(arma, (120, 420), rect)

# Esibizione del punteggio
    carattre_punteggio= bold_font.render("SCORE", 1, BIANCO)
    carattere_numeri = bold_font.render(str(score), 1, BIANCO)
    schermo.blit(carattre_punteggio, (1060, 90))
    if score == 0:
        schermo.blit(carattere_numeri, (1100, 130))
    else:
        schermo.blit(carattere_numeri, (1060, 130))
    schermo.blit(pause_button, (10, 90))

# Completamento delle imposazioni di pausa
    if inizio_gioco == 1:
        schermo.blit(play_button, (500, 200))
        schermo.blit(replay_button, (500, 300))
    
    partita_pulita()
    lievllo_perso()

# Visione FPS
    pygame.display.flip()
    orologio.tick(50)
    pygame.display.set_caption("fps: " + str(orologio.get_fps()))