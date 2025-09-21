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
1. Clonar el repositorio o descargar el archivo `siget_productor_consumidor.py`.
2. Abrir una terminal en la carpeta del proyecto.
3. Ejecutar el programa:

   ```bash
   python siget_productor_consumidor.py
