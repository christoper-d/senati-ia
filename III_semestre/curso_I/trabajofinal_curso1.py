class trabajador:

    def __init__(self,name=str,lastname=str,categoria=str,horasExtr=int,tardanza=int):
        self.name       = name
        self.lastname   = lastname
        self.categoria  = categoria
        self.horasExtr  = horasExtr
        self.tardanza   = tardanza
    
    def nombreCompleto(self):
        return f'\n Nombre                 : {self.name} {self.lastname} \n Categoria              : {self.categoria}\n Horas Extra            : {self.horasExtr}\n Tardanza (minutos)     : {self.tardanza}'

class boleta(trabajador):
    def __init__(self, name=str, lastname=str, categoria=str, horasExtr=int, tardanza=int):
        super().__init__(name, lastname, categoria, horasExtr, tardanza)
        #---
        self.sueldoBasico   = 0
        self.desTardanza    = 0
        self.pagoHorasExtr  = 0
        self.sueldoNeto     = 0

    def calculo(self):
        #---
        sueldos = [3000,2500,2000]
        cat     = ['A','B','C']
        #---
        ph = 0
        posicion = cat.index(self.categoria)

        self.sueldoBasico   =  sueldos[posicion]
        ph                  =  self.sueldoBasico/240
        self.desTardanza    =  round(ph*(self.tardanza/60),2)
        self.pagoHorasExtr  =  round(ph*self.horasExtr,2)
        self.sueldoNeto     =  round((self.sueldoBasico - self.desTardanza) + self.pagoHorasExtr,2)
    
    def printBoleta(self):
        return f'\n Nombre                 : {self.name} {self.lastname} \n Categoria              : {self.categoria}\n Sueldo Basico          : {self.sueldoBasico}\n Descuento Tardanzas    : {self.desTardanza}\n Pago Horas Extras      : {self.pagoHorasExtr}\n Sueldo Neto            : {self.sueldoNeto}'

def main():

    print("\n FERROTEK SAC \n ")
    print(f' 1|-Ingresar nuevos datos \n 2|-Exit \n')
    opcion = int(input('> '))
    if opcion == 1:
        nombre          = str(input('\n Nombre                 : '))
        Apellido        = str(input(' Apellido               : '))
        categoria       = str(input(' Categoria (A | B | C)  : '))
        horasExtra      = int(input(' Horas Extra            : '))
        minTardanza     = int(input(' Tardanza (minutos)     : '))

        trb = trabajador(nombre, Apellido,categoria,horasExtra,minTardanza)
        boleta1 = boleta(trb.name,trb.lastname,trb.categoria,trb.horasExtr,trb.tardanza)
        boleta1.calculo()

        print(f'\n 1|-Imprimir datos ingresados \n 2|-Imprimir boleta \n 3|-Ingresar nuevos datos \n 4|-Exit \n')
        opcion = int(input('> '))
    
        if opcion == 1 :
            print(trb.nombreCompleto())
            print(f'\n 1|-Imprimir boleta \n 2|-Ingresar nuevos datos \n ')
            opcion = int(input('> '))
            if opcion == 1:
                print(boleta1.printBoleta())
                print(f'\n 1|-Ingresar nuevos datos \n ')
                opcion = int(input('> '))
                if opcion == 1:
                    main()
            elif opcion == 2:
                main()

        elif opcion == 2:
            print(boleta1.printBoleta())
            print(f'\n 1|-Ingresar nuevos datos \n ')
            opcion = int(input('> '))
            if opcion == 1:
                main()
        elif opcion == 3:
            main()
        elif opcion == 4:
            print(f'Adios {nombre}')
            quit
    elif opcion == 2:
        quit

main()


