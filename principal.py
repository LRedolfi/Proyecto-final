import pygame,sys #importo librerías
from constantes import * #importo constantes

pygame.init() #inicializo pygame

ventana=pygame.display.set_mode((ancho_ventana,alto_ventana)) #creo ventana
pygame.display.set_caption("Juego proyecto final") #título de la ventana

reloj=pygame.time.Clock() #creo reloj

while True:
    reloj.tick(60) #tiempo de refresco de pantalla 60 fps

    for evento in pygame.event.get(): #recorro eventos
        if evento.type==pygame.QUIT: #si se presiona x se cierra
            pygame.quit() #se cierra pygame
            sys.exit() #se cierra programa

    ventana.fill(color_fondo) #Color de fondo

    pygame.display.update() #actualizo pantalla