import pprint
#productos disponibles de comprar

ropa={'Equipación  madrid':15.99,'Equipación  atleti':13.99,'Equipación  barsa':15.99,'Equipación  Celta':10.99,'Equipación  Leganés':8.99,'Botas  adidas':20.99,'Botas  Nike':20.99,'Botas  Joma':15.99,'Botas  puma':16.99,}

class Bienvenidos:
    def __init__(self,nombre,apellidos,edad,tlf,correo): #formulario de los datos del cliente
#aqui estamos dando valor a las variables
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.tlf = tlf
        self.correo = correo
    print('Te damos la bienvenida a Deportes trovis')
#Aqui en esta función  mostramos el registro
    def registro(self):
        print('')
        print('Usted ha sido registrado como...')
#Este print lo que hace es mostrar los datos de los clientes que han sido rellenados por ellos
        print(f'nombre: {self.nombre}\napellidos: {self.apellidos}\nedad: {self.edad}\ntlf: {self.tlf}\ncorreo {self.correo}')
#Esta variable while que he creado es para que si el cliente no ha rellenado bien los datos los pueda corregir
        validar = input('Confirme sus datos')
        while validar.lower()!='si':
            print()
            print('Vuelva a rellenar sus datos correctamente')
            cliente1=Bienvenidos(input('Nombre:'),input('apellidos:'),input('edad:'),int(input('tlf:')),input('correo:'))
            print()
            print('Registro:')
            print(f'nombre: {self.nombre}\napellidos: {self.apellidos}\nedad: {self.edad}\ntlf: {self.tlf}\ncorreo {self.correo}')
            validar = input('Confirme que los datos estan correctos')
            print(f'Vamos a comprar ya no? {self.nombre}')
            print()
            print('Aqui tenemos la ropa de la roja')

cliente1 = Bienvenidos(input('Nombre:'), input('apellidos:'), input('edad:'), int(input('tlf:')), input('correo:'))
cliente1.registro()

#esto lo que hace es sacar la lista de productos
pprint.pprint(ropa)
#Ahora creo dos listas vacias donde se guardan los productos que digamos
carrito={}
lista_reyes={}

#La funcion productos hara que podamos guardar donde queramos nuestros productos
def productos():
    nomp=input('Escoge el producto que desea:')
    agrega = float(input(f'quieres meter {nomp} a la cesta (1) o a la ista para los reyes magos (2) '))
    #Si lo metemos a la cesta
    if agrega == 1:
        # Guarda el valor en la cesta
        carrito[nomp] = ropa[nomp]
        # nos mostrara lo que tenemos en la cesta
        print(f'Cesta: {carrito}')
        #Nos dara el total de lo de la cesta pero sin sumar el iva
        print(f'Total: {sum(carrito.values())}')
        #Si lo mandamos a la lista de los reyes magos
    elif agrega == 2:
        #almacena el valor en lista reyes
        lista_reyes[nomp] = ropa[nomp]
        #y nos enseña la lista de los reyes magos
        print(f'lista reyes magos: {lista_reyes}')
        #y nos muestra el valor total de lo que hay en lista reyes pero sin el iva
        print(f'Total: {sum(lista_reyes.values())}')
        #Si no eliges ni 1 ni 2 nos volvera a preguntar
    elif agrega >= 3:
        print('Introduce la opcion valida')

productos()

#Esta funcion lo que va a hacer es recordar al cliente que tiene productos en la lista reyes magos
def scompra():
    print()
    seguir_comprando=input('¿Quieres seguir comprando?\n')
    #Si damos  si nos volvera a decir la lista de productos y podremos volver a seleccionar los productos y volver a añadirlos al carro o a la lista de los reyes magos
    if seguir_comprando.lower() == 'si':
        #Sacamos la lista de productos
        pprint.pprint(ropa)
        #Sacamos la opciones para poder seleccionar y añadir los productos
        productos()
        scompra()
        #si no queremos seguir con la compra nos recuerda que tenemos que mover los productos a la lista
    elif seguir_comprando.lower() == 'no':
        print('Recuerda mover los productos de la lista de los reyes a la cesta')
        mfavoritos=float(input('¿Quieres añadir los productos de la lista de los reyes magos a la cesta? SI (1) NO (2)\n'))
        #El macth case lo uso para cuando elijamos 1 nos los mueva a la cesta y nos muestre el total y si elegimos 2 nos lleavara al pago
        match mfavoritos:
            case 1:
                pprint.pprint(lista_reyes)
                cambio=input('Agregar productos a la cesta:\n')
                carrito[cambio] =ropa[cambio]
                print(f'cesta: {carrito}')
                print(f'Total: {sum(carrito.values())}')
            case 2:
                print(' pagar')
    else:
        print('Tienes que escribir si o no')
        scompra()
scompra()

#la funcion pagar hara que depende el pais nos pongan un iva o otro

def pagar():
    #Escribimos el pais
    pais=input('Dinos de que pais eres\n')
    #si es españa se pone un 21%
    if pais.lower() == 'españa':
        print('El IVA de España es del 21%')
        print(f'El total con IVA incluido es el total de {sum(carrito.values())*1.21}€')

    #si el pais es otro se añadira un 15%

    else:
        print('Al ser un pais internacional el IVA que se sumara es del 15%')
        print(f'El total con iva incluido es de {sum(carrito.values())*1.15}€')

    print()
    print('Para terminar con la compra debe de elegir el formato de pago')
    #Elegimos las formas de pago y tenemos 4 opciones
    fpago=int(input('1| pago con tarjeta\n2| Paypal\n(Formato numero): '))
    #Con este match case lo que hacemos es que  segun la forma de pago que elijan rellenamos unos datos o otros
    match fpago:
        case 1:
            print('Ha decidido pagar con tarjeta')
            ntarjeta=input('Numero de tarjeta: ')
            fcaduca=input('Fecha de caducidad(mm/yy): ')
            cvv=input('CVV: ')
            print(f'Numero de tarjeta: {ntarjeta}\nFecha de caducidad: {fcaduca}\nCVV: {cvv}')
            confirmadat1=input('¿Sus datos estan correctos?')
            #Con estos whiles hacemos que si el cliente falla los datos pueda volver a rellenarlos otra vez
            while confirmadat1.lower() != 'si':
                ntarjeta = input('Numero de tarjeta: ')
                fcaduca = input('Fecha de caducidad(mm/yy): ')
                cvv = input('CVV: ')
                print(f'Numero de tarjeta: {ntarjeta}\nFecha de caducidad: {fcaduca}\nCVV: {cvv}')
                confirmadat1 = input('Sus datos estan correctos?\n')
                fact=input('¿Desea que le llegue la factura al gmail o por sms?\n')
                while fact.lower() != 'email' or fact.lower() != 'sms':
                    print('Ha elegido una opción incorrecta')
                if fact.lower() == 'email':
                    print('La factura ha sido enviado a su gmail')
                    if fact.lower() == 'sms':
                        print('La factura ha sido enviada a por sms')

                else:
                    print('Esta opcion no es la correcta reinicie la pagina')

        case 2:
            print('Usted ha decidido pagar por Paypal rellene los correspondientes datos')
            correo=input('Correo electronico: ')
            contraseña=input('Contraseña: ')
            print(f'correo: {correo}\ncontraseña: {contraseña}')
            confirmadat2 = input('¿Sus datos son correctos?\n')
            while confirmadat2.lower() != 'si':
                print()
                print('Rellene nuevamente sus datos')
                correo = input('Correo electronico: ')
                contraseña = input('Contraseña: ')
                print(f'correo: {correo}\ncontraseña: {contraseña}')
                confirmadat2 = input('¿Sus datos son correctos?')
            fact1 = input('¿Desea que le llegue la factura al gmail o por sms?\n')
            while fact1.lower() != 'email' or fact1.lower() != 'sms':
                print('Ha elegido una opcion incorrecta')
            if fact.lower() == 'email':
                print('La factura ha sido enviado a su gmail')
                if fact.lower() =='sms':
                    print('La factura ha sido enviada a por sms')
            else:
                print('Esta opcion no es la correcta reinicie la pagina')

pagar()



