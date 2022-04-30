import csv
from PlanAhorro import PlanAhorro

class ManejadorPlan:
    __listaPlanes=[]
    def __init__(self):
        self.__listaPlanes=[]
    def agregarPlan(self,plan):
        if type(plan)==PlanAhorro:
            self.__listaPlanes.append(plan)
        else:
            print('Error, no se pudo agregar un plan a la lista, el tipo de datos es incorrecto.')
    def cargarDesdeArchivo(self):
        nombreArchivo='planes.csv'
        archivo=open(nombreArchivo)
        reader=csv.reader(archivo,delimiter=';')
        banderaCuotas=True
        for fila in reader:
            if banderaCuotas:
                banderaCuotas= not banderaCuotas
                PlanAhorro.setCuotasDelPlan(int(fila[4]))
                PlanAhorro.setCuotasParaLicitar(int(fila[5]))
            self.agregarPlan(PlanAhorro(int(fila[0]),fila[1],fila[2],float(fila[3])))
        archivo.close()
        print('Fin de la carga desde: ',nombreArchivo)
    def actualizarValores(self):
        for plan in self.__listaPlanes:
            print(plan)
            nuevoValor=float(input('Ingrese el valor del vehiculo:\n'))
            plan.actualizarValorDelVehiculo(nuevoValor)
    def mostrarPlanesPorValorCuota(self,valor):
        for plan in self.__listaPlanes:
            if plan.calcularImporteCuota()<valor:
                print(plan)
    def buscarCodigoPlan(self,codigo):
        resultado=-1
        bandera=True
        i=0
        tamañoLista=len(self.__listaPlanes)
        while i<tamañoLista and bandera:
            if self.__listaPlanes[i].verificarCodigo(codigo):
                bandera= not bandera
                resultado=i
            else:
                i+=1
        return resultado
    def mostrarMontoParaLicitar(self,codigo):
        iPlan=self.buscarCodigoPlan(codigo)
        if iPlan!=-1:
            print('Monto para licitar el vehiculo: {:.2f}'.format(self.__listaPlanes[iPlan].calcularMontoParaLicitar()))
        else:
            print('No se encontro el plan')
    def test(self):
        print('Comienza test ManejadorPlan')
        manejador=ManejadorPlan()
        print('Metodo cargarDesdeArchivo()')
        manejador.cargarDesdeArchivo()
        print('Metodo agregarPlan()')
        manejador.agregarPlan(PlanAhorro(222,'Ranger','4x2 D/C',4500000))
        print('Metodo mostrarPlanesPorValorCuota()')
        manejador.mostrarPlanesPorValorCuota(525001)
        print('Metodo buscarCodigoPlan()')
        print(manejador.buscarCodigoPlan(222))
        print('mostrarMontoParaLicitar()')
        manejador.mostrarMontoParaLicitar(222)
        manejador.mostrarMontoParaLicitar(300)
        print('Fin test ManejadorPlan. \n')