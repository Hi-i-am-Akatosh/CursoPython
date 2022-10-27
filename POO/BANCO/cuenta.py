from mimetypes import init


#Constructor
class Cuenta():
    def __init__(self,nombre,saldo,password):  #CONSTRUCTOR
        self.nombre = nombre
        self.saldo = saldo
        self.password = password

    #Funcion deposito
    def deposito(self,monto_depositar,password):
        if password != self.password:
            print('Password Incorrecta')
            return None
    
        if monto_depositar < 0:
            print('No puede depositar una cantidad menor a 0')
            return None

        self.saldo = self.saldo + monto_depositar
        return self.saldo

    #Funcion retirar
    def retirar(self, cantidad_retirar, password):
        if password != self.password:
            print('Password Incorrecta')
            return None
        
        if cantidad_retirar < 0:
            print('No puede depositar una cantidad menor a 0')
            return None

        self.saldo = self.saldo - cantidad_retirar
        return self.saldo
    
    def ObtenerBalance(self, password):
        if password != self.password:
            print('Password Incorrecta')
            return None
        return self.saldo
        

        

