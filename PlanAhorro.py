class PlanAhorro:
    __codigoDelPlan=0
    __modelo=''
    __versionDelVehiculo=''
    __valorDelVehiculo=0.0
    __cuotasDelPlan=0
    __cuotasParaLicitar=0 
    def __init__(self,codigoDelPlan=0,modelo='',versionDelVehiculo='',valorDelVehiculo=0.0):
        self.__codigoDelPlan=codigoDelPlan
        self.__modelo=modelo
        self.__versionDelVehiculo=versionDelVehiculo
        self.__valorDelVehiculo=valorDelVehiculo
    @classmethod
    def getCuotasDelPlan(cls):
        return cls.__cuotasDelPlan
    @classmethod
    def getCuotasParaLicitar(cls):
        return cls.__cuotasParaLicitar  
    @classmethod
    def setCuotasDelPlan(cls,cuotas):
        cls.__cuotasDelPlan=cuotas
    @classmethod
    def setCuotasParaLicitar(cls,cuotasLicitar):
        cls.__cuotasParaLicitar=cuotasLicitar
    def verificarCodigo(self,codigo):
        return self.__codigoDelPlan==codigo
    def actualizarValorDelVehiculo(self,nuevoValor):
        self.__valorDelVehiculo=nuevoValor
    def calcularImporteCuota(self):
        return (self.__valorDelVehiculo/self.getCuotasDelPlan())+(self.__valorDelVehiculo*0.10)
    def calcularMontoParaLicitar(self):
        return self.getCuotasParaLicitar()*self.calcularImporteCuota()
    def __str__(self):
        return 'Codigo:{}, Modelo:{}, Version:{}'.format(self.__codigoDelPlan,self.__modelo,self.__versionDelVehiculo)
    def test(self):
        print('Comienza test PlanAhorro')
        plan=PlanAhorro(222,'Ranger','4x2 D/C',3000000)
        cPlan=PlanAhorro.getCuotasDelPlan()
        cLicitar=PlanAhorro.getCuotasParaLicitar()
        print('Metodos setCuotasDelPlan() y setCuotasParaLicitar()')
        PlanAhorro.setCuotasDelPlan(70)
        PlanAhorro.setCuotasParaLicitar(20)
        print('Metodos getCuotasDelPlan() y getCuotasParaLicitar()')
        print(PlanAhorro.getCuotasDelPlan())
        print(PlanAhorro.getCuotasParaLicitar())
        print('Metodo verificarCodigo()')
        print(plan.verificarCodigo(222))
        print('Metodo actualizarValorDelVehiculo()')
        plan.actualizarValorDelVehiculo(4500000)
        print('Metodo calcularImporteCuota()')
        print(plan.calcularImporteCuota())
        print('Metodo calcularMontoParaLicitar()')
        print(plan.calcularMontoParaLicitar())
        print('Metodo __str__()')
        print(plan)
        PlanAhorro.setCuotasDelPlan(cPlan)
        PlanAhorro.setCuotasParaLicitar(cLicitar)
        print('Fin test PlanAhorro. \n')