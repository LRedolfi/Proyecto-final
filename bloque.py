import pygame #importo librería
from constantes import * #importo constantes

class Bloque(pygame.sprite.Sprite): #defino la clase bloque
    def __init__(self,x,y): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre
        
        self.image=pygame.Surface([ancho_bloque,alto_bloque]) #creo superficie
        self.image.fill(color_bloque) #color de bloque
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.x=x #posición en x
        self.rect.y=y #posición en y
        
    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect) #dibujo el bloque
        