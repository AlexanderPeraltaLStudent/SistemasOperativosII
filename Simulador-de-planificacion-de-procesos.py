import time, queue

# Clase que representa un proceso del SIGET
class Proceso:
    def __init__(self, id, rafaga, prioridad):
        self.id = id                  # Identificador del proceso
        self.rafaga = rafaga          # Tiempo de ejecución requerido (burst time)
        self.prioridad = prioridad    # Nivel de prioridad (para posibles extensiones)
        self.estado = "Nuevo"         # Estado inicial del proceso

    def __repr__(self):
        return f"P{self.id}(rafaga={self.rafaga}, prioridad={self.prioridad}, estado={self.estado})"

# ------------------------------
# Algoritmo FIFO (First In, First Out)
# ------------------------------
def fifo(procesos):
    print("\n=== Planificación FIFO ===")
    for p in procesos:
        p.estado = "Listo"
        print(f"{p} entra en la cola de listos")

        time.sleep(0.5)

        p.estado = "En ejecución"
        print(f"{p} está en ejecución")
        time.sleep(p.rafaga * 0.5)

        p.estado = "Terminado"
        print(f"{p} ha terminado")

# ------------------------------
# Algoritmo Round Robin
# ------------------------------
def round_robin(procesos, quantum=2):
    print("\n=== Planificación Round Robin ===")
    cola = queue.Queue()

    for p in procesos:
        p.estado = "Listo"
        cola.put(p)

    while not cola.empty():
        p = cola.get()

        if p.rafaga > 0:
            p.estado = "En ejecución"
            ejecucion = min(quantum, p.rafaga)
            print(f"{p} ejecuta {ejecucion} unidades de tiempo")
            time.sleep(ejecucion * 0.5)

            p.rafaga -= ejecucion

            if p.rafaga > 0:
                p.estado = "Listo"
                cola.put(p)
            else:
                p.estado = "Terminado"
                print(f"{p} ha terminado")

# ------------------------------
# Algoritmo SJF (Shortest Job First)
# ------------------------------
def sjf(procesos):
    print("\n=== Planificación SJF (Shortest Job First) ===")

    # Ordenar procesos por ráfaga de CPU más corta primero
    procesos_ordenados = sorted(procesos, key=lambda p: p.rafaga)

    for p in procesos_ordenados:
        p.estado = "Listo"
        print(f"{p} entra en la cola de listos")

        time.sleep(0.5)

        p.estado = "En ejecución"
        print(f"{p} está en ejecución")
        time.sleep(p.rafaga * 0.5)

        p.estado = "Terminado"
        print(f"{p} ha terminado")

# ------------------------------
# Programa principal
# ------------------------------
if __name__ == "__main__":
    # Procesos de ejemplo: id, ráfaga, prioridad
    procesos_fifo = [Proceso(1, 5, 2), Proceso(2, 3, 1), Proceso(3, 7, 3)]
    procesos_rr   = [Proceso(1, 5, 2), Proceso(2, 3, 1), Proceso(3, 7, 3)]
    procesos_sjf  = [Proceso(1, 5, 2), Proceso(2, 3, 1), Proceso(3, 7, 3)]

    fifo(procesos_fifo)
    round_robin(procesos_rr, quantum=2)
    sjf(procesos_sjf)

    print("\nSimulación completada")
