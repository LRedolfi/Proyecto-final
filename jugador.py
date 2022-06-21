import pygame #importo librería
from constantes import * #importo constantes

class Jugador(pygame.sprite.Sprite): #defino la clase jugador
    def __init__(self): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre

        self.image=pygame.Surface([ancho_jugador,alto_jugador]) #creo superficie
        self.image.fill(color_jugador) #color de jugador
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.y=alto_ventana-alto_jugador-alto_piso #posición en y
        self.rect.x=ancho_ventana//2-ancho_jugador//2 #posición en x
        self.velocidad=velocidad_jugador #velocidad del jugador
        self.velocidad_x=0 #velocidad en x
        self.velocidad_y=0 #velocidad en y

    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect) #dibujo el jugador

    #Defino la función para moverse hacia la izquierda
    def izquierda(self):
        self.rect.x-=self.velocidad

    #Defino la función para moverse hacia la derecha
    def derecha(self):
        self.rect.x+=self.velocidad