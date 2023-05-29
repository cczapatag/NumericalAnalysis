import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
import matplotlib.pyplot as plt
import mpld3
from math import *

class Graficas:

    def graph_function(f):
        # Generar los datos de la gráfica

        intervalo = np.arange(-5,8,0.1)
        
        y = []

        print(f)

        for x in intervalo:
        
            valorX = { 'x' : x}

            value = eval(f, globals(), valorX)

            y.append(value)

        fig, ax = plt.subplots()

        ax.plot(intervalo, y, color='#6F42C1')
        ax.grid(True, lw=0.5, color='gray')
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.text(0, max(y), 'Y', ha='center', va='center', fontweight='bold')
        ax.text(max(intervalo), 0, 'X', ha='center', va='center', fontweight='bold')

        # Convertir la gráfica a una imagen en formato PNG
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())

        # Insertar la imagen en el template HTML
        img_uri = 'data:image/png;base64,' + urllib.parse.quote(string)

        plt.close('all')

        return img_uri

