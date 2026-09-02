# Especificación del Proyecto: Sistema Comunitario de Préstamo de Herramientas

## 📌 Planteamiento del Problema
En muchos barrios se acostumbra compartir herramientas para reducir costos. Sin embargo, suele perderse el control sobre devoluciones, daños, ubicaciones y disponibilidad. 

La junta comunal requiere un **programa de consola en Python** que centralice la gestión de herramientas, vecinos y préstamos, eliminando el uso de cuadernos y llamadas telefónicas.

---

## 🛠️ Requerimientos Funcionales

### 1. Gestión de Herramientas
* **Datos requeridos:**
  * `id`: Identificador único.
  * `nombre`: Nombre de la herramienta.
  * `categoría`: Construcción, jardinería, etc.
  * `cantidad_disponible`: Unidades en stock.
  * `estado`: Activa, en reparación, fuera de servicio.
  * `valor_estimado`: Precio referencial.
* **Operaciones:** Crear, listar, buscar, actualizar y eliminar/inactivar.

### 2. Gestión de Usuarios (Vecinos)
* **Datos requeridos:**
  * `id`: Documento / Identificador.
  * `nombres` y `apellidos`.
  * `teléfono` y `dirección`.
  * `tipo_usuario`: Residente o Administrador.
* **Operaciones:** Crear, listar, buscar, actualizar y eliminar.

### 3. Gestión de Préstamos
* **Datos requeridos:**
  * `id_prestamo`: Identificador del préstamo.
  * `usuario_id`: Usuario que solicita.
  * `herramienta_id`: Herramienta prestada.
  * `cantidad`: Unidades solicitadas.
  * `fecha_inicio`: Fecha de salida.
  * `fecha_estimada_devolucion`: Fecha esperada.
  * `estado`: Pendiente, aprobado, devuelto, vencido.
  * `observaciones`: Comentarios adicionales.
* **Reglas de negocio:**
  * Al prestar, verificar stock disponible y descontar la cantidad prestada.
  * Al devolver, actualizar el estado del préstamo y restaurar el stock.

### 4. Consultas y Reportes
* Tools con stock bajo (menos de 3 unidades).
* Préstamos activos y vencidos.
* Historial de préstamos por usuario.
* Herramientas más solicitadas.
* Usuarios con mayor número de préstamos.

### 5. Registro de Eventos (Logs)
* Registrar en un archivo de texto (`.log` o `.txt`) errores y eventos críticos (ej. intento de préstamo sin stock suficiente, accesos denegados, fallos de validación).

---

## 🔐 Control de Acceso y Permisos

| Rol | Permisos |
| :--- | :--- |
| **Administrador** | Registrar/editar usuarios y herramientas, aprobar o rechazar solicitudes de préstamo, gestionar el sistema completo. |
| **Usuario (Residente)** | Consultar herramientas disponibles, ver quién las posee y cuándo se liberan, crear solicitudes de préstamo. |

---

## 📦 Entregables del Proyecto

1. **Código Fuente (`/src`):** Archivos `.py` organizados modularmente (ej. `main.py`, `herramientas.py`, `usuarios.py`, `prestamos.py`, `persistencia.py`).
2. **Archivos de Persistencia:** Datos guardados en formato `.json`, `.csv` o `.txt`.
3. **Archivo de Logs:** Registro continuo de eventos en `app.log` o similar.
4. **Documentación (`README.md`):** Instrucciones claras sobre cómo ejecutar la aplicación de consola.
5. **Carpeta de Pruebas (`/tests`):** Casos de prueba con entradas y salidas esperadas.

---

## 📂 Estructura de Archivos Recomendada

```text
sistema_herramientas/
│
├── specs.md                  # Este archivo de especificaciones
├── README.md                 # Guía de uso y ejecución
├── main.py                   # Punto de entrada del programa
│
├── data/                     # Archivos de persistencia
│   ├── herramientas.json
│   ├── usuarios.json
│   ├── prestamos.json
│   └── app.log               # Archivo de logs
│
├── modules/                  # Lógica del sistema
│   ├── __init__.py
│   ├── herramientas.py
│   ├── usuarios.py
│   ├── prestamos.py
│   ├── reportes.py
│   └── logger.py
│
└── tests/                    # Casos de prueba
    ├── test_inputs.txt
    └── test_outputs.txt