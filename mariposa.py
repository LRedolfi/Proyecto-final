import pygame #importo librería
from constantes import * #importo constantes

class Mariposa(pygame.sprite.Sprite): #defino la clase bloque
    def __init__(self,x,y,ancho_bloque,alto_bloque): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre
        
        self.image=pygame.image.load(os.path.join(dirImágenes,'mariposa.png')) #creo superficie
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.x=x #posición en x
        self.rect.y=y #posición en y
        self.arriba=pygame.Rect(self.rect.x,self.rect.y,self.rect.width,1)
        self.abajo=pygame.Rect(self.rect.x,self.rect.y+alto_bloque-1,self.rect.width,1)
        self.izquierda=pygame.Rect(self.rect.x,self.rect.y,1,self.rect.height-1)
        self.derecha=pygame.Rect(self.rect.x+ancho_bloque-1,self.rect.y,1,self.rect.height-1)
        
    def dibujar(self,superficie):
        superficie.blit(self.image,self.rect) #dibujo el bloque
        