import pygame as pg
from settings1 import setting
pg.init()

# clock
clock = pg.time.Clock()
clock.tick(10)


def screen_info_and_setfsrcreen():
    fullscreen_sz = pg.display.Info().current_w, pg.display.Info().current_h
    print('screen size =', fullscreen_sz)
    if pg.display.Info().current_w != setting.windowX or pg.display.Info().current_h != setting.windowY:
        setting.screensize = (pg.display.Info().current_w - 100, pg.display.Info().current_h - 100)


screen_info_and_setfsrcreen()

screen = pg.display.set_mode(setting.screensize, pg.RESIZABLE)
# drawline for branches


class Branches:
    def __init__(self, initposx, initposy, endposx, endposy, directrion):
        self.initposx = initposx
        self.initposy = initposy
        self.endposx = endposx
        self.endposy = endposy
        self.directrion = directrion
        self.endpos = pg.Vector2()
        self.endpos.xy = (endposx, endposy)
        self.initpos = pg.Vector2()
        self.initpos.xy = (initposx, initposy)
        pg.draw.line(screen, setting.BLACK, self.initpos, self.endpos)


# recursive function and string reader
astring = 'F+F+F+F'
actuallvl = 0


def fractal(serie, level, actualvl):
    if actualvl >= level:
        return serie
    else:
        actualvl = actualvl + 1
        serie = serie.replace('F', 'F+F-F-FF+F+F-F')
        return fractal(serie, level, actualvl)


astring = (fractal(astring, 2, actuallvl))
print (astring)
# creating the magnitude of F
fvecx = pg.Vector2()
fvecx.xy = (1, 0)
fvecy = pg.Vector2()
fvecy.xy = (0, 1)


def drawfractal(serie):
    angle = 0
    finalcoordinates = pg.Vector2()
    finalcoordinates.xy = ((pg.display.Info().current_w - 100)/2, (pg.display.Info().current_h - 100)/2)
    for x in serie:
        if x == 'F':
            if angle == 0 or angle == 360:
                Branches(finalcoordinates.x, finalcoordinates.y, finalcoordinates.x + fvecx.x*setting.fl, finalcoordinates.y,
                         angle)
                finalcoordinates = finalcoordinates + fvecx * setting.fl
            if angle == 90 or angle == -270:
                Branches(finalcoordinates.x, finalcoordinates.y, finalcoordinates.x, finalcoordinates.y - fvecy.y*setting.fl,
                         angle)
                finalcoordinates = finalcoordinates - fvecy * setting.fl
            if angle == 180 or angle == -180:
                Branches(finalcoordinates.x, finalcoordinates.y, finalcoordinates.x - fvecx.x*setting.fl, finalcoordinates.y,
                         angle)
                finalcoordinates = finalcoordinates - fvecx * setting.fl
            if angle == 270 or angle == -90:
                Branches(finalcoordinates.x, finalcoordinates.y, finalcoordinates.x, finalcoordinates.y + fvecy.y*setting.fl,
                         angle)
                finalcoordinates = finalcoordinates + fvecy * setting.fl
        if x == '+':
            angle = (angle + 90) % 360

        if x == '-':
            angle = (angle - 90) % 360

        print (angle)


# main loop
screen.fill(setting.WHITE)
displaying = True
while displaying:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            displaying = False

    drawfractal(astring)
    pg.display.flip()

pg.quit()
