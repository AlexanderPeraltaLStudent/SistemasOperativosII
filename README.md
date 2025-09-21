# Simulación Productor–Consumidor – SIGET

## 📌 Descripción
Este proyecto implementa una simulación del **problema clásico Productor–Consumidor** adaptado al contexto del **Sistema de Gestión de Tráfico (SIGET)**.  
La idea principal es mostrar cómo varios **sensores de tráfico (productores)** generan datos que deben ser procesados por **módulos de análisis (consumidores)** de manera concurrente, utilizando mecanismos de sincronización para evitar condiciones de carrera o bloqueos.

## ⚙️ Tecnologías utilizadas
- **Lenguaje:** Python 3.x  
- **Bibliotecas:** `threading`, `time`, `random`  

## 🏗️ Diseño de la solución
- **Productores:** simulan sensores que generan datos de tráfico.  
- **Consumidores:** simulan módulos de análisis que procesan esos datos.  
- **Búfer compartido:** memoria intermedia de capacidad limitada.  
- **Sincronización:**  
  - *Mutex (Lock):* asegura la exclusión mutua al acceder al búfer.  
  - *Semáforos:* controlan espacios vacíos y llenos en el búfer.  
  - *Centinelas:* señalan a los consumidores cuándo deben finalizar.  

## ▶️ Ejecución

## 📄 Simulador de Planificación de Procesos

Se ha añadido el archivo `Simulador-de-planificacion-de-procesos.py`, que implementa y simula tres algoritmos clásicos de planificación de procesos:

- **FIFO (First In, First Out):** Atiende los procesos en el orden de llegada.
- **Round Robin:** Atiende los procesos por turnos con un quantum definido.
- **SJF (Shortest Job First):** Atiende primero los procesos con menor ráfaga de CPU.

### Ejecución del simulador
1. Clonar el repositorio o descargar el archivo `Simulador-de-planificacion-de-procesos.py`.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el programa:

  ```bash
  python Simulador-de-planificacion-de-procesos.py
  ```

El programa mostrará en consola la simulación de los tres algoritmos con procesos de ejemplo.

---

## ▶️ Ejecución del Productor-Consumidor
1. Clonar el repositorio o descargar el archivo `siget_productor_consumidor.py`.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el programa:

  ```bash
  python siget_productor_consumidor.py
  ```
