import requests
from Pilotos import Piloto
from Constructores import Constructors
from Circuitos import Circuitos
from Carreras import Carreras
from Podium import Podium
from Alimentos import Alimentos
from Restaurant import Restaurant

class Cargar_datos:
    def __init__(self, constructores, pilotos, carreras, circuito, restaurant,lugares):
        self.constructores = constructores
        self.pilotos = pilotos 
        self.carreras = carreras
        self.circuito = circuito
        self.restaurant = restaurant
        self.lugares = lugares
    
    #Funcion para cargar los conductores de la API
    def cargar_datos_Constructores(self):
        print("\nEspere...\n")
        
        #Pre-cargar datos de la API
        response = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/constructors.json")
        data = response.json()

        #Crear objeto de la clase constructor, el cual tendrá toda su info
        for t in data:
            nombre = t["name"]
            nacionalidad = t["nationality"]
            team = t["id"]
            lista_pilotos = []
            
            constructor = Constructors(nombre, nacionalidad, team, lista_pilotos) 
            self.constructores.append(constructor)

        print("Datos de los constructores cargados con exito!\n")
    
    #Esta función nos permitirá el Pre-cargo de la API de los pilotos.
    def cargar_datos_Pilotos(self):
        
        print("\nEspere...\n")
        
        #Pre-cargar datos de la API
        response2 = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/drivers.json")
        data2 = response2.json()

        #Crear los objetos
        for t in data2:
            nombre = t["firstName"]
            apellido = t["lastName"]
            fecha_nacimiento = t["dateOfBirth"]
            lugar_nacimiento = t["nationality"]
            numero = t["permanentNumber"]
            
            piloto = Piloto(nombre, apellido, fecha_nacimiento, lugar_nacimiento, numero)
            
            self.pilotos.append(piloto)

            for c in self.constructores:
                if c.team == t["team"]:
                    c.lista_pilotos.append(piloto)

        print("Datos de los Pilotos cargados con exito!\n")
    
    #Esta función nos permitirá el Pre-cargo de la API de las carreras.
    def cargar_datos_CarreraCircuitos(self):
        
        print("\nEspere...\n")
        
        #Pre-cargar datos de la API
        response3 = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json")
        data3 = response3.json()

        #Crear los objetos
        for t in data3:
            nombre = t["name"]
            numero = t["round"]
            fecha = t["date"]
            mapa = t["map"]
            podium = Podium(mapa)
            
            nombre2 = t["circuit"]["name"]
            pais = t["circuit"]["location"]["country"]
            localidad = t["circuit"]["location"]["locality"]
            lat_long = [t["circuit"]["location"]["lat"],t["circuit"]["location"]["long"]]

            circuito = Circuitos(nombre2, pais, localidad, lat_long)
            self.circuito.append(circuito)

            carrera = Carreras(nombre,numero,fecha,circuito,podium)
            self.carreras.append(carrera)
                
        print("Datos de las carreras cargados con exito!\n")
    
    def cargar_restaurants(self):
        print("\nEspere...\n")
        
        #Pre-cargar datos de la API
        response4 = requests.get("https://raw.githubusercontent.com/Algorimtos-y-Programacion-2223-2/api-proyecto/main/races.json")
        data4 = response4.json()
        
        for z in data4:
            for rest in z["restaurants"]:
                name = rest["name"]
                clave = z["name"]
                list_prod = []
                
                for prod in rest["items"]:
                    nombre3 = prod["name"]
                    
                    precio3 = prod["price"]
                    
                    lista_t = prod["type"].split(":")
                    
                    tipo = lista_t[0]
                    tipo_especifc = lista_t[1]
                    
                    alimento = Alimentos(nombre3,tipo,tipo_especifc,precio3)
                    list_prod.append(alimento)
                
                restaurant = Restaurant(name,list_prod,clave)
                self.restaurant.append(restaurant)
                
        print("Prodcutos cargados con exito!\n")
    
    def cargar_lugares(self):
        for i in range(1,len(self.pilotos)+1):
            self.lugares.append(i)

    def cargar_datos(self):
        self.cargar_datos_Constructores()
        self.cargar_datos_Pilotos()
        self.cargar_datos_CarreraCircuitos()
        self.cargar_restaurants()
        self.cargar_lugares()

