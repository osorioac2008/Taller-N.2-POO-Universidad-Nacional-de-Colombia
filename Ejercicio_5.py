from enum import Enum

class TipoCuenta(Enum):
    AHORROS = "ahorros"
    CORRIENTE = "corriente"
    

class CuentaBancaria:
    def __init__(self, nombre, apellido, numero_cuenta, tipo_cuenta : TipoCuenta, saldo = 0):
        self.nombre = nombre
        self.apellido = apellido
        self._saldo = saldo
        
        if len(str(numero_cuenta)) != 11:
            raise ValueError("El numero no concuerda con el formato")
        self.numero_cuenta = numero_cuenta
        
        if not isinstance(tipo_cuenta, TipoCuenta):
            raise ValueError("No señor, esa no es una opcion")
        self.tipo_cuenta = tipo_cuenta
       
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, total):
        self._saldo = total 
        
    def cuenta(self):
        print(f"Usuario: {self.nombre}, apellido: {self.apellido}, numero Bancario: {self.numero_cuenta}, tipo: {self.tipo_cuenta}, saldo: {self.saldo}")
        
    def Consultar_salario(self):
        print(f"Su sueldo establece: {self.saldo}")
    
    def consignacion(self, valor):
        if valor <= 0:
            raise ValueError("No puede consignar un valor negativo")
        self._saldo += valor
        print(f"A consignado {valor}$ a la cuenta")
        
    def retiro(self, valor):
        if valor <= 0:
            raise ValueError("Necesita un minimo de retiro")
        elif valor > self._saldo:
            raise ValueError("No puede retirar mas del valor de la cuenta")
        self._saldo -= valor
        print(f"Se a retirado {valor}$ de la cuenta")
        
cuenta = CuentaBancaria("Jose", "Analiso", 87639403948, TipoCuenta.CORRIENTE)
cuenta.cuenta()
cuenta.Consultar_salario()
cuenta.consignacion(6767)
cuenta.retiro(67)
cuenta.Consultar_salario()
