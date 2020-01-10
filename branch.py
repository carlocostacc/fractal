astring = 'F+F+F+F'
actuallvl = 0
def fractal(serie, level, actuallvl):
    if actuallvl >= level:
        return serie
    else:
        actuallvl = actuallvl + 1
        serie = serie.replace('F', 'F+F-F-FF+F+F-F')
        return fractal(serie, level, actuallvl)

astring =(fractal(astring, 2, actuallvl))
print(astring)