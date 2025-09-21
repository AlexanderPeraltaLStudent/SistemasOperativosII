import threading, time, random

# Clase que representa el búfer compartido
class Buffer:
    def __init__(self, capacidad):
        # Capacidad máxima del búfer
        self.capacidad = capacidad
        # Lista que almacenará los datos producidos
        self.cola = []
        # Mutex (candado) para exclusión mutua
        self.mutex = threading.Lock()
        # Semáforo que cuenta espacios vacíos disponibles
        self.vacios = threading.Semaphore(capacidad)
        # Semáforo que cuenta espacios ocupados
        self.llenos = threading.Semaphore(0)

    # Método para insertar un elemento en el búfer
    def poner(self, item):
        self.vacios.acquire()          # Esperar un espacio libre
        with self.mutex:               # Sección crítica protegida por el candado
            self.cola.append(item)
        self.llenos.release()          # Incrementar contador de espacios ocupados

    # Método para retirar un elemento del búfer
    def sacar(self):
        self.llenos.acquire()          # Esperar que haya al menos un elemento
        with self.mutex:               # Sección crítica protegida
            item = self.cola.pop(0)
        self.vacios.release()          # Liberar un espacio vacío
        return item

# Función que simula un productor (sensor de tráfico)
def productor(id_prod, buffer, cantidad):
    for i in range(cantidad):
        # Cada productor genera un dato con identificador único
        dato = f"Sensor{id_prod}-Dato{i}"
        buffer.poner(dato)  # Insertar en el búfer
        print(f"[Productor {id_prod}] generó {dato}")
        time.sleep(random.uniform(0.1, 0.4))  # Simular tiempo de espera
    # Insertar un valor centinela (None) para indicar finalización
    buffer.poner(None)

# Función que simula un consumidor (módulo de análisis del SIGET)
def consumidor(id_cons, buffer):
    while True:
        item = buffer.sacar()
        # Si recibe el centinela, se detiene
        if item is None:
            buffer.poner(None)  # Reinsertar centinela para otros consumidores
            print(f"[Consumidor {id_cons}] terminó")
            break
        # Procesamiento del dato extraído
        print(f"[Consumidor {id_cons}] procesó {item}")
        time.sleep(random.uniform(0.2, 0.5))  # Simular tiempo de análisis

# Programa principal
if __name__ == "__main__":
    # Crear un búfer de capacidad 5
    buffer = Buffer(capacidad=5)

    # Crear 2 hilos productores y 2 hilos consumidores
    productores = [threading.Thread(target=productor, args=(i, buffer, 5)) for i in range(2)]
    consumidores = [threading.Thread(target=consumidor, args=(i, buffer)) for i in range(2)]

    # Iniciar todos los hilos
    for p in productores: p.start()
    for c in consumidores: c.start()

    # Esperar a que todos terminen
    for p in productores: p.join()
    for c in consumidores: c.join()

    print("Simulación terminada")
