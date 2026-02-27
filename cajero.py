print("Bienvenidos al cajero automático")
saldo = 1000
n_de_operaciones = int(input("por favor ingrese cuantas operaciones quiere realizar: "))

         
#menu
for i in range(n_de_operaciones):
    print ("1 → Consultar saldo")
    print ("2 → Retirar dinero")
    print ("3 → Depositar dinero")
    opcion = input("por favor ingrese la opcion: ")
    
 #opcion 1
if opcion == "1":
         print (saldo)

elif opcion == "2":
        #opcion 2
        retirar = int(input("por favor ingrese cuanto desea retirar: "))
        while retirar < 0:
            retirar = float(input("es un numero negativo, ingresa una cantidad valida"))
        
        if retirar > saldo:
            print("monto insuficiente")
        elif retirar <= saldo: 
            saldo -= retirar
            print (f"saldo actual: {saldo} ")