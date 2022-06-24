import pygame,sys #importo librerías
from constantes import * #importo constantes
from piso import Piso #importo clase piso
from techo import Techo #importo clase techo
from banner import Banner #importo clase banner
from jugador import Jugador #importo clase jugador
from pelota import Pelota #importo clase pelota
from bloque import Bloque #importo clase bloque

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

bloques=pygame.sprite.Group() #creo grupo de bloques

while True: #bucle de juego
    reloj.tick(60) #tiempo de refresco de pantalla 60 fps

    tecla=pygame.key.get_pressed() #obtengo las teclas presionadas
    if tecla[pygame.K_LEFT] or tecla[pygame.K_a]: #si se presiona la tecla izquierda
        jugador_1.izquierda() #muevo a la izquierda
    if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]: #si se presiona la tecla derecha
        jugador_1.derecha() #muevo a la derecha
    if tecla[pygame.K_UP] or tecla[pygame.K_w]: #si se presiona la tecla arriba
        pelota.subiendo=True #muevo la pelota hacia arriba
        pelota.moviendo_derecha=True #muevo la pelota a la derecha

    #Chequeo que el jugador no se salga de la pantalla
    if jugador_1.rect.x<0:
        jugador_1.rect.x=0
        jugador_1.cabeza.x=0
    if jugador_1.rect.x>ancho_ventana-ancho_jugador:
        jugador_1.rect.x=ancho_ventana-ancho_jugador
        jugador_1.cabeza.x=ancho_ventana-ancho_jugador

    #Chequeo que la pelota no se salga de la pantalla
    if pelota.rect.x<0:
        pelota.moviendo_izquierda=False
        pelota.moviendo_derecha=True
    if pelota.rect.x>ancho_ventana-ancho_pelota:
        pelota.moviendo_izquierda=True
        pelota.moviendo_derecha=False
    
    #Detecto colisión con techo
    if pygame.sprite.collide_rect(pelota,techo):
        pelota.subiendo=False
        pelota.bajando=True

    #Detecto colisión con jugador 1 y muevo la pelota con el jugador 1
    if pelota.rect.colliderect(jugador_1.cabeza):
        if jugador_1.rect.x>0:
            if tecla[pygame.K_LEFT] or tecla[pygame.K_a]: #si se presiona la tecla izquierda
                pelota.izquierda(velocidad_jugador) #muevo a la izquierda
        if jugador_1.rect.x<ancho_ventana-ancho_jugador:
            if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]: #si se presiona la tecla derecha
                pelota.derecha(velocidad_jugador) #muevo a la derecha
        if pelota.bajando: #si la pelota baja
            pelota.subiendo=True
            pelota.bajando=False

    #Detecto la colisión con los bloques, depende donde le pego al bloque, la pelota se mueve en la dirección contraria, y elimino el bloque
    for bloque in bloques:
        if pelota.rect.colliderect(bloque.abajo):
            pelota.subiendo=False
            pelota.bajando=True
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje
        if pelota.rect.colliderect(bloque.arriba):
            pelota.subiendo=True
            pelota.bajando=False
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje
        if pelota.rect.colliderect(bloque.izquierda):
            pelota.moviendo_izquierda=True
            pelota.moviendo_derecha=False
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje
        if pelota.rect.colliderect(bloque.derecha):
            pelota.moviendo_izquierda=False
            pelota.moviendo_derecha=True
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje

    #Detecto colisión con piso
    if pygame.sprite.collide_rect(pelota,piso):
        if juego==True:
            print("Juego terminado")
            juego=False
        velocidad_pelota=0

    #Llamo a los movimientos de la pelota
    if pelota.subiendo:
        pelota.subir(velocidad_pelota)
    
    if pelota.bajando:
        pelota.bajar(velocidad_pelota)

    if pelota.moviendo_izquierda:
        pelota.izquierda(velocidad_pelota)
    
    if pelota.moviendo_derecha:
        pelota.derecha(velocidad_pelota)

    #Creo el array de bloques
    if len(bloques)==0:
        cantidad_bloques=ancho_ventana//ancho_bloque
        for i in range(cantidad_bloques-1):
            x_bloque=i*ancho_bloque+2*i
            bloque=Bloque(x_bloque,alto_banner+alto_techo)
            bloques.add(bloque)

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

    for bloque in bloques:
        bloque.dibujar(ventana) #dibujo bloques
    
    banner.dibujar_texto(ventana,puntaje,nivel) #dibujo texto

    pygame.display.update() #actualizo pantalla