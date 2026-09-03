# Sistema Comunitario de Préstamo de Herramientas

## 📌 Planteamiento del Problema

En muchos barrios existe la costumbre de compartir herramientas entre vecinos para evitar que cada persona tenga que comprarlas todas. El problema es que, con el tiempo, se pierde el control: algunas herramientas no se devuelven a tiempo, otras se dañan y no se sabe quién las tiene, o simplemente no hay registro claro de cuántas hay disponibles.

La junta comunal de tu barrio ha decidido organizar este proceso mediante un **programa de consola** que registre las herramientas, los vecinos y los préstamos realizados. Con esta solución, esperan que cualquier integrante de la comunidad pueda consultar la información sin depender de cuadernos ni llamadas telefónicas.

---

## 📋 Requerimientos del Sistema

### 1. Gestión de Herramientas
* **Atributos:**
  * `ID`
  * `Nombre`
  * `Categoría` *(ej. construcción, jardinería)*
  * `Cantidad disponible`
  * `Estado` *(activa, en reparación, fuera de servicio)*
  * `Valor estimado`
* **Operaciones:** Crear, listar, buscar, actualizar y eliminar/inactivar herramientas.

### 2. Gestión de Usuarios
* **Atributos:**
  * `ID`
  * `Nombres`
  * `Apellidos`
  * `Teléfono`
  * `Dirección`
  * `Tipo de usuario` *(ej. residente, administrador)*
* **Operaciones:** Crear, listar, buscar, actualizar y eliminar usuarios.

### 3. Gestión de Préstamos
* **Atributos:**
  * `ID del préstamo`
  * `Usuario`
  * `Herramienta`
  * `Cantidad`
  * `Fecha de inicio`
  * `Fecha estimada de devolución`
  * `Estado`
  * `Observaciones`
* **Lógica del negocio:**
  * El sistema debe verificar la disponibilidad de la herramienta y ajustar la cantidad en stock al registrar un préstamo.
  * Cuando se devuelva la herramienta, se debe actualizar el estado del préstamo y restaurar la cantidad disponible.

### 4. Consultas y Reportes
* Herramientas con stock bajo *(menos de 3 unidades)*.
* Préstamos activos y vencidos.
* Historial de préstamos de un usuario específico.
* Herramientas más solicitadas por la comunidad.
* Usuarios que más herramientas han solicitado.

### 5. Registro de Eventos (Logs)
* Todo error o evento relevante *(ejemplo: intentar prestar más herramientas de las disponibles)* debe quedar registrado en un archivo de texto (`.log` / `.txt`) para el seguimiento de la administración.

---

## 🔐 Permisos y Roles de Usuario

* **Administrador:** Se encarga de registrar a los usuarios y las herramientas con el fin de evitar suplantación de identidad. Aprueba las solicitudes de préstamo.
* **Usuario (Residente):**
  * Consulta el estado de las herramientas, su disponibilidad futura y quién la posee actualmente.
  * Crea solicitudes de herramientas *(que deben ser aprobadas por el administrador)*.

---

## 📦 Entregables Esperados

1. **Código fuente:** Archivos `.py` organizados modularmente.
2. **Persistencia de datos:** Archivos de almacenamiento generados por el programa (`.json`, `.csv` o `.txt`).
3. **Archivo de logs:** Registro continuo de eventos relevantes.
4. **Documentación:** Archivo `README.md` con instrucciones claras de instalación y ejecución.
5. **Casos de prueba:** Carpeta de pruebas con archivos de entradas y salidas esperadas.