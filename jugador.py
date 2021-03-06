import pygame #importo librería
from constantes import * #importo constantes
import os

class Jugador(pygame.sprite.Sprite): #defino la clase jugador
    def __init__(self): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre

        self.imágenes=(
            pygame.image.load(os.path.join(dirImágenes,'arriba_der.png')),
            pygame.image.load(os.path.join(dirImágenes,'arriba_izq.png')),
            pygame.image.load(os.path.join(dirImágenes,'perdedor.png')),
        )

        self.image=self.imágenes[1]#creo superficie
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.y=alto_ventana-alto_jugador-alto_piso #posición en y
        self.rect.x=ancho_ventana//2-ancho_jugador//2 #posición en x
        self.velocidad=velocidad_jugador #velocidad del jugador
        self.velocidad_x=0 #velocidad en x
        self.velocidad_y=0 #velocidad en y
        self.cabeza=pygame.Rect(self.rect.x,self.rect.y,self.rect.width,1) #cabeza del jugador

    def dibujar(self,superficie,jugando):
        superficie.blit(self.image,self.rect) #dibujo el jugador
        if not jugando:
            self.image=self.imágenes[2]

    def dibujar_nuevamente(self,superficie):
        self.rect.y=alto_ventana-alto_jugador-alto_piso
        self.rect.x=ancho_ventana//2-ancho_jugador//2
        self.cabeza=pygame.Rect(self.rect.x,self.rect.y,self.rect.width,1)
        superficie.blit(self.image,self.rect)
        self.image=self.imágenes[1]

    #Defino la función para moverse hacia la izquierda
    def izquierda(self,velocidad):
        self.rect.x-=velocidad
        self.cabeza.x-=velocidad
        self.image=self.imágenes[0]

    #Defino la función para moverse hacia la derecha
    def derecha(self,velocidad):
        self.rect.x+=velocidad
        self.cabeza.x+=velocidad
        self.image=self.imágenes[1]