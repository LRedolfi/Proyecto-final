import pygame #importo librería
from constantes import * #importo constantes

class Banner(pygame.sprite.Sprite): #defino la clase banner
    def __init__(self): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre

        self.image=pygame.Surface([ancho_ventana,alto_banner]) #creo superficie
        self.image.fill(color_banner) #color de banner
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.y=0 #posición en y
        self.rect.x=0 #posición en x

    def dibujar(self,superficie): #dibujo el banner
        superficie.blit(self.image,self.rect) #dibujo la superficie