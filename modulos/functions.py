# Aqui vamos a colocar funciones que relizan las validaciones para los inputs, asi no toca repetir el codigo en cada modulo
import json, os
from datetime import datetime

def leer_entero(mensaje):
    """Pide un entero en bucle hasta recibir una entrada válida."""
    while True:
        entrada = input(mensaje).strip()
        try:
            return int(entrada)
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


def leer_flotante(mensaje):
    """Pide un decimal en bucle (acepta coma o punto)."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            return float(entrada)
        except ValueError:
            print("Error: Debe ingresar un número válido (ej.: 12.5).")


def leer_fecha(mensaje, permitir_vacio=False):
    """Pide una fecha real en formato AAAA-MM-DD en bucle.

    Si permitir_vacio es True, una entrada vacía devuelve "" (para que el
    llamador aplique un valor por defecto como la fecha actual).
    """
    while True:
        entrada = input(mensaje).strip()
        if permitir_vacio and entrada == "":
            return ""
        try:
            datetime.strptime(entrada, "%Y-%m-%d")
            return entrada
        except ValueError:
            print("Error: Debe ingresar una fecha válida en formato AAAA-MM-DD (ej.: 2026-10-01).")


def cargar_json_lista(ruta):
    """Lee un JSON y garantiza devolver una lista (vacía si falta/corrompe/no es lista)."""
    if not os.path.exists(ruta):
        return []
    try:
        with open(ruta, "r", encoding="utf-8") as f:
            datos = json.load(f)
    except (json.JSONDecodeError, OSError):
        return []
    return datos if isinstance(datos, list) else []
