import pygame #importo librería
from constantes import * #importo constantes

class Piso(pygame.sprite.Sprite): #defino la clase piso
    def __init__(self): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre

        self.image=pygame.Surface([ancho_ventana,alto_piso]) #creo superficie
        self.image.fill(color_piso) #color de piso
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.y=alto_ventana-alto_piso #posición en y
        self.rect.x=0 #posición en x

    def dibujar(self,superficie): #dibujo el piso
        superficie.blit(self.image,self.rect) #dibujo la superficie