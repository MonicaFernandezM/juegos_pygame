import pygame as pg 
pg.init()

class Bola:
    def __init__(self, padre: pg.Surface, x, y, color = (255, 255, 255), radio = 10):
        self.x = x  #atributos(instancia dentro de una clase)
        self.y = y 
        self.color = color
        self.radio = radio 
        self.vx = 1
        self.vy = 1
        self.padre = padre


    def mover(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio: #si es positivo o negativo se controla desde aqui del sentido 
            self.vx *= -1       

        #if self.radio >= self.x >= limDer - self.radio (es lo mismo de arriba)

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1

    def dibujar(self): #superficie donde se va a dibujar 
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio) #tupla 

class Game: 
    def __init__(self, ancho=600, alto=800): #generico los valor de ancho y alto 
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(self.pantalla, ancho // 2, alto // 2, (255, 255, 0))
        self.bola1 = Bola(self.pantalla, 350, 250, radio = 60)
        self.bola1.vx = -1
        self.bola1.vy = -3

    def bucle_ppal(self): #su trabajo es montarme la pantalla en infinito
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:``
                    game_over =True 

            self.bola.mover()
            self.bola1.mover()
            self.pantalla.fill((255, 0, 0))
            self.bola.dibujar()
            self.bola1.dibujar()

            pg.display.flip()


if __name__ == '__main__':
    pg.init()

    game = Game() #instancia game, objeto de tipo game 
    game.bucle_ppal() 

    pg.quit()

