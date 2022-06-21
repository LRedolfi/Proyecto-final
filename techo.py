import pygame #importo librería
from constantes import * #importo constantes

class Techo(pygame.sprite.Sprite): #defino la clase techo
    def __init__(self): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre

        self.image=pygame.Surface([ancho_ventana,alto_techo]) #creo superficie
        self.image.fill(color_techo) #color de techo
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.y=30 #posición en y
        self.rect.x=0 #posición en x

    def dibujar(self,superficie): #dibujo el piso
        superficie.blit(self.image,self.rect) #dibujo la superficie
