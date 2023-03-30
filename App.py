import random
from operator import itemgetter, attrgetter
from Cargar_datos import Cargar_datos
from Busquedas import Busquedas
from Cliente import Cliente
from Podium import Podium
from Factura_Carrera import Factura_Carrera

class App():
    def __init__(self):
        self.constructores = []
        self.pilotos = []
        self.circuitos = []
        self.carreras = []
        self.restaurant = []
        self.clientes = []
        self.facturas_restaurant = []
        self.facturas_carreras = []
        self.lugares = []
        self.estado_entradas = False
        

    

    #MENú para el punto 1 "GESTION DE CARRERAS Y EQUIPO"
    def menu_gestion(self):
        while True:
            print("\n============================")
            print("GESTION DE CARRERAS Y EQUIPO")
            print("============================")
            print("1. Cargar Datos\n2. Busquedas\n3. Finalizar Carreras\n4. Salir")
                        
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,5)):
                print("Error!!! Dato Inválido.")
                option = input("Ingrese el número correspondiente a la acción que desea realizar: ")
                    
            if option == "1":
                cargar_datos = Cargar_datos(self.constructores, self.pilotos, self.carreras, self.circuitos, self.restaurant,self.lugares)
                cargar_datos.cargar_datos()

                print(len(self.lugares))
            elif option == "2":
                self.menu_busquedas()
            elif option == "3":
                self.menu_finalizar()
            else:
                break
    
    #Menú para realizar las busquedas
    def menu_busquedas(self):

        while True:
            
            busqueda = Busquedas(self.constructores, self.pilotos, self.carreras, self.circuitos, self.restaurant)
            
            print("\n============================")
            print("         BUSQUEDAS")
            print("============================")
            print("1. Buscar los constructores por país\n2. Buscar los pilotos por constructor\n3. Buscar carreras por país del circuito\n4. Buscar todas las carreras que ocurren según el mes\n5. Salir")
            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,6)):
                print("Error!!! Opción Inválida.")
                option = input("Ingrese el número correspondiente a la acción que desea realizar: ")
                    
            if option == "1":
                busqueda.buscar_conductores()
            elif option == "2":
                busqueda.buscar_pilotos()
            elif option == "3":
                busqueda.buscar_carreras()
            elif option == "4":
                busqueda.buscar_carreras_mes()
            else:
                break
    
    
    #Menú para finalizar carreras
    def menu_finalizar(self):

        print("\n==============================")
        print("          CARRERAS")
        print("==============================")
        
        #MOSTRAR LAS CARRERAS CON UN NUMERO AL LADO PARA IDENTIFICARLAS
        i = 1
        for carrera in self.carreras:
            print(f"{i}. {carrera.nombre}")
            i = i+1
        
        #ELEGIR LA CARRERA QUE SE DESEA FINALIZAR
        op = input("\nElige la carrera que deseas finalizar: ")
        while (not op.isnumeric()) or (not int(op) in range(1,i+1)):
            print("Error!!! Opción Inválida.")
            op = input("\nElige la carrera que deseas finalizar: ")
        
        j = 1
        for carrera2 in self.carreras:
            if j == int(op):
                #MOSTRAR LA CARRERA QUE SE DESEA FINALIZAR
                if carrera2.estado == True:
                    print(f"\n{j}. {carrera2.nombre}")
                    print("\n1. Finalizar\n2.No finalizar\n") #CONFIRMAR QUE SE DESEA FINALIZAR
                    
                    option1 = input("Escoja la opción a realizar: ")
                    while (not option1.isnumeric()) or (not int(option1) in range(1,3)):
                        print("Error!!! Opción Inválida.")
                        option1 = input("\nEscoja la opción a realizar: ")
                    
                    if option1 == "1":
                        carrera2.estado = False #FINALIZAR CARRERA
                        
                        #ASIGNAR UN LUGAR A CADA PILOTO DE MANERA AL AZAR DE LA LISTA DE LUGARES
                        for piloto in self.pilotos:
                            
                            #GUARDAR EL VALOR DEL LUGAR SELECCIONADO DE FORMA ALEATORIA
                            num = random.choice(self.lugares) 
                            
                            #REMOVER EL LUGAR ASIGNADO PARA QUE NO SE REPITA
                            self.lugares.remove(num) 
                            
                            #ASIGNAR LUGAR AL PILOTO
                            piloto.lugar = num
                        
                        #ASIGNAR PUNTOS A LOS PILOTOS SEGÚN EL LUGAR OBTENIDO Y MOSTRAR LOS PRIMEROS 10
                        for piloto2 in self.pilotos:
                            if piloto2.lugar == 1:
                                piloto2.puntos += 25
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 2:
                                piloto2.puntos += 18
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 3:
                                piloto2.puntos += 15
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 4:
                                piloto2.puntos += 12
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 5:
                                piloto2.puntos += 10
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 6:
                                piloto2.puntos += 8
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 7:
                                piloto2.puntos += 6
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 8:
                                piloto2.puntos += 4
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 9:
                                piloto2.puntos += 2
                                piloto2.mostrar_piloto2()
                            if piloto2.lugar == 10:
                                piloto2.puntos += 1
                                piloto2.mostrar_piloto2()
                        break
                    else:
                        break
                
                #SI LA CARRERA YA FINALIZÓ MOSTRAR ESTE MENSAJE
                else:
                    print("La carrera ya ha terminado")
            j = j+1
        
        #VOLVER A LLENAR LA LISTA DE LUGARES
        for i in range(1,len(self.pilotos)+1):
            self.lugares.append(i)
        
        #REINICIAR LOS LUGARES EN 0 PARA PODER ASIGNARLE UN VALOR DISTINTO SIN QUE SE REPITA EN OTRA CARRERA
        for pilotos in self.pilotos:
            pilotos.lugares = 0


    # MENÚ DE GESTION DE VENTA DE ENTRADAS
    def menu_gestion_entradas(self):
        while True:
            print("\n============================")
            print("GESTION DE VENTA DE ENTRADAS")
            print("============================\n")
            
            #Ingresar los datos del cliente
            print("-----------------")
            print("Datos del Cliente")
            print("-----------------")

            nombre = input("Ingrese el nombre del cliente: ")
            
            edad = input("Ingrese la edad: ")
            while (not edad.isnumeric()) or (not int(edad) in range(1,101)):
                print("Error!!! Dato Inválido.")
                edad = input("Ingrese la edad: ")
                    
            cedula = input("Ingrese su cedula: ")
            while (not cedula.isnumeric()) or (not int(cedula) > 0):
                print("Error!!! Dato Inválido.")
                cedula = input("Ingrese su cedula: ")
                
                
            cliente = Cliente(nombre,edad,cedula)
            self.clientes.append(cliente)
                    
            for i,carrera in enumerate(self.carreras):
                print("---",i+1,"---")
                print(carrera.mostrar_carreras())
                          
                
            num = input("Ingrese el numero correspondiente al partido que desea ver: ")          
            #while (not num.isnumeric()) or (not int(num) in range(1,len(self.carreras)+1)):
            #    print("Error!!! Dato Inválido.")
            #    num = input("Ingrese el numero correspondiente al partido que desea ver: ")

            print("\n---------------")
            print("TIPO DE ENTRADA")
            print("---------------")
                            
            print("1. General\n2. VIP.\n")

            tipo_entrada = input("Ingrese el tipo de entrada que desea comprar: ")
            while (not tipo_entrada.isnumeric()) or (not int(tipo_entrada) in range(1,3)):
                print("Error!!! Dato Inválido.")
                tipo_entrada = input("Ingrese el tipo de entrada que desea comprar: ")

            puesto_uno = input("Ingrese la primera coordenada del puesto que desea: ")
            puesto_dos = input("Ingrese la segunda coordenada del puesto que desea: ")

            puesto_ocup = [int(puesto_uno), int(puesto_dos)]

            if tipo_entrada == "1":
                tipo_entrada = "general"
                for j,carrera in enumerate(self.carreras):
                    if j == num:
                        for podium in carrera.podium:
                            if podium == "general":
                                fila = carrera.podium[mapa][0]                                    
                                columna = carrera.podium[mapa][1]
                                for f in range(fila):
                                    for c in range(columna):
                                        if f == puesto_uno and c == puesto_dos:
                                            f = "*"
                                            c = "*"
                                            print([f,c], end = " ")
                                            print("")
                                        else:
                                           print([f,c], end = " ") 
                                           print("")   
                        print("")
            else:
                tipo_entrada = "vip"
                for j,carrera in enumerate(self.carreras):
                    if j == num:
                        for podium in carrera.podium:
                            if podium == "vip":
                                fila = carrera.podium[mapa][0]                                    
                                columna = carrera.podium[mapa][1]
                                for f in range(fila):
                                    for c in range(columna):
                                        if f == puesto_uno and c == puesto_dos:
                                            f = "*"
                                            c = "*"
                                            print([f,c], end = " ")
                                            print("")
                                        else:
                                           print([f,c], end = " ") 
                                           print("")   
                        print("")                
            
            clave = len(self.facturas_carreras) + 1000
            factura = Factura_Carrera(clave,cliente,num,tipo_entrada,puesto_ocup)
            factura.mostrar_factura()
            print("Factura creada con exito.")
            
            print("\n1. Compra de entrada\n2. Salir")
            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,3)):
                print("Error!!! Dato Inválido.")
                option = input("Ingrese el número correspondiente a la acción que desea realizar: ")
                        
            if option == "2":
                break                     
    
    #Funcion menu de gestion de restaurant 
    def menu_gestion_rest(self):
        while True:
            busqueda = Busquedas(self.constructores, self.pilotos, self.carreras, self.circuitos, self.restaurant)
            
            print("\n======================")
            print("GESTION DE RESTAURANTES")
            print("=======================")
            print("1. Buscar Productos\n2. Salir")
                            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,3)):
                print("Error!!! Dato Inválido.")
                option = input("Ingrese el número correspondiente a la acción que desea realizar: ")
                        
            if option == "1":
                busqueda.buscar_productos() 
            else:
                break
            
    def menu_gestion_venta_restaurante(self):
        print("\n==============================")
        print("  Gestion de venta Restaurant")
        print("==============================")
        
        cedula = input("Ingrese la cedula del cliente: ")   
        while (not cedula.isnumeric()) or (not int(cedula) > 0):
            print("Error!!! Dato Inválido.")
            cedula = input("Ingrese su cedula: ")
        
        i = 0
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                i = 1
                break
        
        if i == 1:
          for factura in self.facturas_carreras:
              if factura.cliente.cedula == cedula and factura.tipo_entrada == "vip":
                  break
            
        else:
            print("El cliente no ha sido registrado")  

    #MENÚ DE ESTADÍTICA
    def menu_estadisticas(self):
        while True:
            print("\n==========================")
            print("ESTADÍSTICAS DE FORMULA 1")
            print("==========================")
            print("1. Promedio de gasto de cliente VIP\n2. Tabla de Asistencia a las carreras\n3. Carrera con mayor asistencia\n4. Carrera con mayor voletos vendidos\n5. Top 3 productos del restaurant\n6. Top 3 de clientes\n7.Graficos de Estadísticas\n8. Salir")
                    
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,9)):
                print("Error!!! Dato Inválido.")
                option = input("Ingrese el número correspondiente a la acción que desea realizar: ")
            
            if option == "1":
                pass
            elif option == "2":
                pass
            elif option == "3":
                pass
            elif option == "4":
                pass
            elif option == "5":
                pass
            elif option == "6":
                pass
            elif option == "7":
                pass
            else:
                break  



    
    #Menú Principal
    def incio(self):
        while True:
            print("\n=========================")
            print("BIENVENIDOS A FORMULA 1")
            print("=========================")
            print("1. Gestion de carreras y equipo\n2. Gestion de ventas de entrada\n3. Gestion de Asistencia a las carreras\n4. Gestion de Restaurante\n5. Gestion de venta de Restaurant\n6. Estadísticas\n7. Salir")
            
            option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            while (not option.isnumeric()) or (not int(option) in range(1,8)):
                print("Error!!! Dato Inválido.")
                option = input("\nIngrese el número correspondiente a la acción que desea realizar: ")
            
            if option == "1":
                self.menu_gestion()
            elif option == "2":
                self.menu_gestion_entradas()
            elif option == "3":
                pass
            elif option == "4":
                self.menu_gestion_rest()
            elif option == "5":
                pass
            
            elif option == "6":
                self.menu_estadisticas()
            else:
                print("\nAdiós.")
                break