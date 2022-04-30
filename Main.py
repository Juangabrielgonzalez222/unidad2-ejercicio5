
from ManejadorPlan import ManejadorPlan
from Menu import Menu

if __name__== '__main__':
    manejador=ManejadorPlan()
    manejador.cargarDesdeArchivo()
    menu=Menu()
    menu.lanzarMenu(manejador)