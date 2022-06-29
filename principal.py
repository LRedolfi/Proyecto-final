import pygame,sys #importo librerías
from constantes import * #importo constantes
from piso import Piso #importo clase piso
from techo import Techo #importo clase techo
from texto import Texto #importo clase banner
from jugador import Jugador #importo clase jugador
from pelota import Pelota #importo clase pelota
from bloque import Bloque #importo clase bloque
from menu import Menu #importo clase menu

pygame.init() #inicializo pygame

ventana=pygame.display.set_mode((ancho_ventana,alto_ventana)) #creo ventana
pygame.display.set_caption("Invasión arácnida") #título de la ventana

reloj=pygame.time.Clock() #creo reloj

piso=Piso() #creo piso

techo=Techo() #creo techo

banner=Texto() #creo banner

jugador_1=Jugador() #creo jugador
jugador_2=Jugador() #creo jugador

pelota=Pelota() #creo pelota

sonido_rebote=pygame.mixer.Sound(os.path.join(dirSonidos,'rebote.wav')) #creo sonido rebote

bloques=pygame.sprite.Group() #creo grupo de bloques

archivo=open("puntaje.txt","r")
puntaje_máximo=int(archivo.read())
archivo.close()

menu=Menu() #creo menu

menu.dibujar(ventana,puntaje_máximo) #dibujo menu

while True: #bucle de juego
    reloj.tick(60) #tiempo de refresco de pantalla 60 fps

    tecla=pygame.key.get_pressed() #obtengo las teclas presionadas
    if (tecla[pygame.K_LEFT] or tecla[pygame.K_a]) and pausa==False: #si se presiona la tecla izquierda
        jugador_1.izquierda(velocidad_jugador) #muevo a la izquierda
    if (tecla[pygame.K_RIGHT] or tecla[pygame.K_d]) and pausa==False: #si se presiona la tecla derecha
        jugador_1.derecha(velocidad_jugador) #muevo a la derecha
    
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
        sonido_rebote.play()
    if pelota.rect.x>ancho_ventana-ancho_pelota:
        pelota.moviendo_izquierda=True
        pelota.moviendo_derecha=False
        sonido_rebote.play()
    
    #Detecto colisión con techo
    if pygame.sprite.collide_rect(pelota,techo):
        pelota.subiendo=False
        pelota.bajando=True
        sonido_rebote.play()

    #Detecto colisión con jugador 1 y muevo la pelota con el jugador 1
    if pelota.abajo.colliderect(jugador_1.cabeza):
        if tecla[pygame.K_UP] or tecla[pygame.K_w] and juego==False: #si se presiona la tecla arriba
            pelota.subiendo=True #muevo la pelota hacia arriba
            pelota.moviendo_derecha=True #muevo la pelota a la derecha
            juego=True #cambio el estado del juego
            if nivel<5:
                velocidad_pelota=nivel+1 #cambio la velocidad de la pelota
            else:
                velocidad_pelota=5
            pelota.moviendo_izquierda=False #no muevo la pelota a la izquierda
        if jugador_1.rect.x>0:
            if tecla[pygame.K_LEFT] or tecla[pygame.K_a]: #si se presiona la tecla izquierda
                pelota.izquierda(velocidad_jugador) #muevo a la izquierda
        if jugador_1.rect.x<ancho_ventana-ancho_jugador:
            if tecla[pygame.K_RIGHT] or tecla[pygame.K_d]: #si se presiona la tecla derecha
                pelota.derecha(velocidad_jugador) #muevo a la derecha
        if pelota.bajando: #si la pelota baja
            sonido_rebote.play()
            pelota.subiendo=True
            pelota.bajando=False

    #Pausa del juego
    if tecla[pygame.K_r] and pausa == True:
        pausa=False
        if nivel<5:
                velocidad_pelota=nivel+1 #cambio la velocidad de la pelota
        else:
            velocidad_pelota=5
    
    if tecla[pygame.K_p] and pausa == False:
        pausa=True
        velocidad_pelota=0

    #Detecto la colisión con los bloques, depende donde le pego al bloque, la pelota se mueve en la dirección contraria, y elimino el bloque
    for bloque in bloques:
        if pelota.rect.colliderect(bloque.abajo):
            pelota.subiendo=False
            pelota.bajando=True
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje
            sonido_araña=pygame.mixer.Sound(os.path.join(dirSonidos,'araña.wav'))
            sonido_araña.play()
        if pelota.rect.colliderect(bloque.arriba):
            pelota.subiendo=True
            pelota.bajando=False
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje
            sonido_araña=pygame.mixer.Sound(os.path.join(dirSonidos,'araña.wav'))
            sonido_araña.play()
        if pelota.rect.colliderect(bloque.izquierda):
            pelota.moviendo_izquierda=True
            pelota.moviendo_derecha=False
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje
            sonido_araña=pygame.mixer.Sound(os.path.join(dirSonidos,'araña.wav'))
            sonido_araña.play()
        if pelota.rect.colliderect(bloque.derecha):
            pelota.moviendo_izquierda=False
            pelota.moviendo_derecha=True
            bloques.remove(bloque) #elimino el bloque
            puntaje+=100 #aumento el puntaje
            sonido_araña=pygame.mixer.Sound(os.path.join(dirSonidos,'araña.wav'))
            sonido_araña.play()

    #Detecto colisión con piso
    if pygame.sprite.collide_rect(pelota,piso):
        if juego==True:
            vidas-=1 #resto una vida
            juego=False
            jugando=False
            sonido_perder=pygame.mixer.Sound(os.path.join(dirSonidos,'perder.wav'))
            sonido_perder.play()
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
        if nivel<=10:
            máximas_filas=nivel
        else:
            máximas_filas=10
        for o in range(máximas_filas):
            for i in range(cantidad_bloques-1):
                y_bloque=o*alto_bloque+2*o
                x_bloque=i*ancho_bloque+2*i
                bloque=Bloque(x_bloque,alto_banner+alto_techo+y_bloque,ancho_bloque,alto_bloque)
                if x_bloque<ancho_ventana-ancho_bloque:
                    bloques.add(bloque)
        if juego==True:
            nivel+=1
            velocidad_jugador+=1
            velocidad_pelota=0
            jugador_1.dibujar_nuevamente(ventana)
            pelota.dibujar_nuevamente(ventana)

    for evento in pygame.event.get(): #recorro eventos
        if evento.type==pygame.QUIT: #si se presiona x se cierra
            pygame.quit() #se cierra pygame
            sys.exit() #se cierra programa

    ventana.blit(pygame.image.load(os.path.join(dirImágenes,'fondo.jpg')),(0,0)) #Color de fondo

    piso.dibujar(ventana) #dibujo piso

    techo.dibujar(ventana) #dibujo techo

    banner.dibujar(ventana) #dibujo banner

    jugador_1.dibujar(ventana,jugando) #dibujo jugador

    pelota.dibujar(ventana) #dibujo pelota

    for bloque in bloques:
        bloque.dibujar(ventana) #dibujo bloques
    
    banner.dibujar_texto(ventana,puntaje,nivel,jugando,vidas,pausa,ganador,puntaje_máximo) #dibujo texto

    if jugando==False and tecla[pygame.K_r] and vidas>0:
        jugador_1.dibujar_nuevamente(ventana)
        pelota.dibujar_nuevamente(ventana)
        jugando=True

    if jugando==False and tecla[pygame.K_r] and vidas==0:
        jugador_1.dibujar_nuevamente(ventana)
        pelota.dibujar_nuevamente(ventana)
        jugando=True
        nivel=1
        puntaje=0
        vidas=3
        bloques.empty()
        ganador=False

    if puntaje>puntaje_máximo:
        puntaje_máximo=puntaje
        archivo=open("puntaje.txt","w")
        archivo.write(str(puntaje_máximo))
        archivo.close()
        ganador=True

    pygame.display.update() #actualizo pantalla