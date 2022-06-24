import pygame #importo librería
from constantes import * #importo constantes

class Pelota(pygame.sprite.Sprite): #defino la clase pelota
    def __init__(self): #constructor de la clase
        pygame.sprite.Sprite.__init__(self) #llamo al constructor de la clase padre

        self.image=pygame.Surface([ancho_pelota,alto_pelota]) #creo superficie
        self.image.fill(color_pelota) #color de pelota
        self.rect=self.image.get_rect() #obtengo rectángulo de la superficie
        self.rect.y=alto_ventana-alto_piso-alto_pelota-alto_jugador+1 #posición en y
        self.rect.x=ancho_ventana//2-ancho_pelota//2 #posición en x
        self.velocidad=velocidad_pelota #velocidad de la pelota
        self.velocidad_x=velocidad_pelota #velocidad en x
        self.velocidad_y=velocidad_pelota #velocidad en y
        self.subiendo=False #pelota subiendo
        self.bajando=False #pelota bajando
        self.moviendo_izquierda=False #pelota izquierda
        self.moviendo_derecha=False #pelota derecha
        self.abajo=pygame.Rect(self.rect.x,self.rect.y+alto_pelota-1,self.rect.width,1)
    
    def dibujar(self,superficie): #dibujo la pelota
        superficie.blit(self.image,self.rect) #dibujo la superficie

    def derecha(self,velocidad):
        self.rect.x+=velocidad #muevo la pelota a la derecha
        self.abajo.x+=velocidad #muevo la rectángulo abajo a la derecha
    
    def izquierda(self,velocidad):
        self.rect.x-=velocidad #muevo la pelota a la izquierda
        self.abajo.x-=velocidad

    def subir(self,velocidad):
        self.rect.y-=velocidad #muevo la pelota hacia arriba
        self.abajo.y-=velocidad

    def bajar(self,velocidad): 
        self.rect.y+=velocidad #muevo la pelota hacia abajo
        self.abajo.y+=velocidad