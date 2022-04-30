from PlanAhorro import PlanAhorro

class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            '1':self.opcion1,
            '2':self.opcion2,
            '3':self.opcion3,
            '4':self.opcion4,
            '5':self.test,
            '6':self.salir
        }
    def lanzarMenu(self,manejador):
        #Menu opciones
        i=str(len(self.__opciones))
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1 para actualizar el valor del vehiculo de cada plan.')
            print('-Ingrese 2 para dado un valor, mostrar datos de los planes cuyo valor de cuota sea inferior al ingresado.')
            print('-Ingrese 3 para mostrar el monto que se debe haber pagado para licitar el vehiculo.')
            print('-Ingrese 4 para modificar la cantidad de cuotas para licitar.')
            print('-Ingrese 5 para ejecutar test.')
            print('-Ingrese 6 para salir.')
            opcion=input('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion=='1' or opcion=='2' or opcion=='3' or opcion=='5':
                ejecutar(manejador)
            else:
                ejecutar()
    def opcion1(self,manejador):
        manejador.actualizarValores()
    def opcion2(self,manejador):
        valor=float(input('Ingrese valor:\n'))
        manejador.mostrarPlanesPorValorCuota(valor)
    def opcion3(self,manejador):
        codigo=int(input('Ingrese codigo del vehiculo:\n'))
        manejador.mostrarMontoParaLicitar(codigo)
    def opcion4(self):
        cuotasLicitar=int(input('Ingrese la cantidad de cuotas para licitar:\n'))
        PlanAhorro.setCuotasParaLicitar(cuotasLicitar)
    def test(self,manejador):
        manejador.test()
        plan=PlanAhorro(20,'Prueba','Version Prueba',100000)
        plan.test()
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')