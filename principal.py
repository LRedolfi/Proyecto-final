import pygame,sys #importo librerías
from constantes import * #importo constantes
from piso import Piso #importo clase piso
from techo import Techo #importo clase techo
from banner import Banner #importo clase banner

pygame.init() #inicializo pygame

ventana=pygame.display.set_mode((ancho_ventana,alto_ventana)) #creo ventana
pygame.display.set_caption("Juego proyecto final") #título de la ventana

reloj=pygame.time.Clock() #creo reloj

piso=Piso() #creo piso

techo=Techo() #creo techo

banner=Banner() #creo banner

while True:
    reloj.tick(60) #tiempo de refresco de pantalla 60 fps

    for evento in pygame.event.get(): #recorro eventos
        if evento.type==pygame.QUIT: #si se presiona x se cierra
            pygame.quit() #se cierra pygame
            sys.exit() #se cierra programa

    ventana.fill(color_fondo) #Color de fondo

    piso.dibujar(ventana) #dibujo piso

    techo.dibujar(ventana) #dibujo techo

    banner.dibujar(ventana) #dibujo banner

    pygame.display.update() #actualizo pantalla