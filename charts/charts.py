import matplotlib.pyplot as plt

def generar_grafica ():
    etiquetas =['A','B','C']
    valores=[200, 120, 50]
    
    fig, ax= plt.subplots()
    ax.pie(valores,labels=etiquetas)
    plt.savefig('pie.png')
    plt.close()
    