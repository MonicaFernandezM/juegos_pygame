from curses import BUTTON1_RELEASED
import pygame as pg 
import random 
pg.init()


FPS = 60
class Vigneta: #sacar una clase que saque los atributos necesarios que haga dibujos en la pantalla
    def __init__(self, padre, x, y, ancho, alto, color =(255, 255, 255)):
        self.padre = padre
        self.x = x
        self.y = y
        self.color = color
        self.ancho = ancho
        self.alto = alto
        self.vx = 0
        self.vy = 0

    @property #decorador: a la funcion que deficines le mete caracteristicas nuevas
    def xcentro(self):
        return self.x + self.ancho // 2

    @property
    def ycentro(self):
        return self.y + self.alto // 2

    def dibujar(self):
        pass

    def mover(self):
        pass


class Ladrillo(Vigneta):
    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

""" def comprobarToque(self, bola):
        #hago cosas al tocarme la bola
        pass
"""

class Raqueta(Vigneta):
    def __init__(self, padre, x, y, ancho, alto, color = (255, 255, 0)):
       super().__init__(padre, x, y, ancho, alto, color)
       self.vx = 5
    
    def dibujar(self):
        pg.draw.rect(self.padre, self.color, (self.x, self.y, self.ancho, self.alto))

    def mover(self): #metodo porque son cosas que se hacen 
        teclas = pg.key.get_pressed()
        if teclas[pg.K_LEFT]:
            self.x -= self.vx
        if teclas[pg.K_RIGHT]: #me devuelve un diccionario un diccionario por eso va entre []
            self.x += self.vx

        if self.x <= 0:
            self.x = 0
        if self.x + self.ancho >= self.padre.get_width():
            self.x = self.padre.get_width() - self.ancho


class Bola(Vigneta):
    def __init__(self, padre, x, y, color = (255, 255, 255), radio = 10):
        super().__init__(padre, x - radio, y - radio, 2 * radio, 2 * radio, color) #la coordenada de la bola es la esquina de la vigneta
        self.radio = radio 
        self.vx = 5
        self.vy = 5

    def mover(self):
        self.x += self.vx
        self.y += self.vy

        if self.x <= 0 or self.x >= self.padre.get_width() - self.ancho: #si es positivo o negativo se controla desde aqui del sentido 
            self.vx *= -1       

        if self.y <= 0 or self.y >= self.padre.get_height() - self.alto:
            self.vy *= -1

    def dibujar(self): #superficie donde se va a dibujar 
        pg.draw.circle(self.padre, self.color, (self.xcentro, self.ycentro), self.radio) #tupla 

    def compruebaChoque(self, otro):
        if (self.x in range(otro.x, otro.x + otro.ancho) or \
           self.x + self.ancho in range(otro.x, otro.x + otro.ancho)) and \
           (self.y in range(otro.y, otro.y + otro.alto) or \
           self.y + self.alto in range(otro.y, otro.y + otro.alto)):

           self.vy *= -1



class Game: 
    def __init__(self, ancho=600, alto=800): #generico los valor de ancho y alto 
        self.pantalla = pg.display.set_mode((ancho, alto))
        self.bola = Bola(self.pantalla, ancho // 20, alto // 2, radio = 10)
        self.raqueta = Raqueta(self.pantalla, ancho//2, alto - 30, 100, 20) #esta intanciada
        self.ladrillos = []
        
        self.crea_ladrillos()

        self.reloj = pg.time.Clock()
        """
        for i in range (random.randint(2,10)):
            radio = random.randint(5, 50)
            self.bolas.append(Bola(random.randint(radio, ancho - radio),
                                    random.randint(radio, alto - radio),
                                    self.pantalla, 
                                    (random.randint(0,255),
                                     random.randint(0,255),
                                     random.randint(0,255)),
                                     radio))
            self.bolas[i].vx = random.randint(5,15) * random.choice[(-1, 1)] 
            self.bolas[i].vy = random.randint(5,15) * random.choice[(-1, 1)] 
        """

    def crea_ladrillos(self):
        for col in range(10):
            for fil in range(4):
                l = Ladrillo(self.pantalla, 5 + 60 * col, 5 + 30 * fil, 50, 20)
                self.ladrillos.append(l)

    def bucle_ppal(self): #su trabajo es montarme la pantalla en infinito
        game_over = False

        while not game_over:
            milisegundos = self.reloj.tick(FPS)

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over =True 
                """
                if evento.type == pg.KEYDOWN:#para que se mueva la raqueta
                    if evento.key == pg.K_LEFT:
                        self.raqueta.vx = -5 
                    
                    if evento.key == pg.K_RIGHT:
                        self.raqueta.vx = 5
                    
                if evento.type == pg.KEYUP:
                    if evento.key in (pg.K_LEFT, pg.K_RIGHT):
                        self.raqueta.vx = 0
                """


            self.pantalla.fill((255, 0, 0)) #rellenar la pantalla.
            
            self.bola.mover()
            self.raqueta.mover()
            self.bola.compruebaChoque(self.raqueta)

            self.bola.dibujar()
            self.raqueta.dibujar()
            for ladrillo in self.ladrillos:
                ladrillo.dibujar()
            pg.display.flip()


if __name__ == '__main__':
    pg.init()

    game = Game() #instancia game, objeto de tipo game 
    game.bucle_ppal() 

    pg.quit()

