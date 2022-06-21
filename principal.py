import pygame,sys #importo librerías
from constantes import * #importo constantes
from piso import Piso #importo clase piso
from techo import Techo #importo clase techo
from banner import Banner #importo clase banner
from jugador import Jugador #importo clase jugador
from pelota import Pelota #importo clase pelota

pygame.init() #inicializo pygame

ventana=pygame.display.set_mode((ancho_ventana,alto_ventana)) #creo ventana
pygame.display.set_caption("Juego proyecto final") #título de la ventana

reloj=pygame.time.Clock() #creo reloj

piso=Piso() #creo piso

techo=Techo() #creo techo

banner=Banner() #creo banner

jugador_1=Jugador() #creo jugador
jugador_2=Jugador() #creo jugador

pelota=Pelota() #creo pelota

while True:
    reloj.tick(60) #tiempo de refresco de pantalla 60 fps

    tecla=pygame.key.get_pressed() #obtengo las teclas presionadas
    if tecla[pygame.K_LEFT] or tecla[pygame.K_a]: #si se presiona la tecla izquierda
        jugador_1.izquierda() #muevo a la izquierda
    if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]: #si se presiona la tecla derecha
        jugador_1.derecha() #muevo a la derecha

    #Chequeo que el jugador no se salga de la pantalla
    if jugador_1.rect.x<0:
        jugador_1.rect.x=0
    if jugador_1.rect.x>ancho_ventana-ancho_jugador:
        jugador_1.rect.x=ancho_ventana-ancho_jugador

    for evento in pygame.event.get(): #recorro eventos
        if evento.type==pygame.QUIT: #si se presiona x se cierra
            pygame.quit() #se cierra pygame
            sys.exit() #se cierra programa

    ventana.fill(color_fondo) #Color de fondo

    piso.dibujar(ventana) #dibujo piso

    techo.dibujar(ventana) #dibujo techo

    banner.dibujar(ventana) #dibujo banner

    jugador_1.dibujar(ventana) #dibujo jugador

    pelota.dibujar(ventana) #dibujo pelota

    pygame.display.update() #actualizo pantalla