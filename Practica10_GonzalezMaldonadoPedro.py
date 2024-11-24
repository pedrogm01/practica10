import threading
import random
import time

# Tamaño máximo del estacionamiento
MAX_CAPACITY = 12

# Lista que representa el estacionamiento
estacionamiento = []

# Lock para evitar condiciones de carrera
lock = threading.Lock()

def agregar_auto():
    """Función que añade autos al estacionamiento con mayor frecuencia."""
    while True:
        frecuencia = random.choice([0.5, 0.7, 1])  # Más probabilidad de entrada rápida
        time.sleep(frecuencia)
        with lock:
            if len(estacionamiento) < MAX_CAPACITY:
                auto = f"Auto-{len(estacionamiento) + 1}"
                estacionamiento.append(auto)
                print(f"Entrada: {auto} añadido. Autos actuales: {len(estacionamiento)}")
            else:
                print("Entrada: Estacionamiento lleno, no se puede añadir más autos.")

def retirar_auto():
    """Función que retira autos del estacionamiento con menor frecuencia."""
    while True:
        frecuencia = random.choice([1.5, 2, 2.5])  # Menos probabilidad de salida rápida
        time.sleep(frecuencia)
        with lock:
            if estacionamiento:
                auto = estacionamiento.pop(0)
                print(f"Salida: {auto} retirado. Autos actuales: {len(estacionamiento)}")
            else:
                print("Salida: Estacionamiento vacío, no se pueden retirar autos.")

# Crear los hilos para entrada y salida
hilo_entrada = threading.Thread(target=agregar_auto, daemon=True)
hilo_salida = threading.Thread(target=retirar_auto, daemon=True)

# Iniciar los hilos
hilo_entrada.start()
hilo_salida.start()

# Mantener el programa en ejecución
try:
    while True:
        time.sleep(1)  # Mantener el programa corriendo para los hilos
except KeyboardInterrupt:
    print("Programa finalizado.")
