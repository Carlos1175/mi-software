Proyecto Final – Generador de Contraseñas

Autor
Carlos  
Estudiante de Lógica de Programación  

Objetivo del Proyecto
Desarrollar un software interactivo en Python que permita generar contraseñas seguras utilizando distintas reglas, según las elecciones del usuario. Este proyecto integra todos los conocimientos adquiridos durante las 8 semanas del curso de Lógica de Programación.

Funcionalidades Principales

1. Menú principal interactivo
   - Generar contraseña
   - Ver reglas de seguridad
   - Salir del programa

2. Opciones para generar contraseñas
   - Contraseña personalizada por el usuario
   - Contraseña automática fácil de decir (solo letras)
   - Contraseña automática fácil de leer (letras + opción de números/símbolos)
   - Contraseña con todos los caracteres (con opción de personalización)

3. Evaluación de fortaleza de la contraseña
   - Se indica si la contraseña es **fuerte** o **débil** según:
     - Longitud mínima (8)
     - Inclusión de mayúsculas, minúsculas, números y símbolos

4. Guardado opcional de contraseñas generadas
   - Se escriben en un archivo local `contraseñas_guardadas.txt`

---

Conocimientos Aplicados

- Algoritmos y lógica condicional (`if`, `while`)
- Funciones definidas por el usuario (`def`)
- Manejo de strings y estructuras de datos
- Módulos estándar (`random`, `string`)
- Entrada y salida de datos con `input()` y archivos
- Validación de datos y bucles
- Estructura `main()` como punto de ejecución

Ejecución del programa

Este programa está diseñado para ser ejecutado desde una terminal con soporte de entrada por teclado.  
Asegúrate de tener Python instalado (versión 3.6 en adelante).

```bash
python generador_contrasenas.py
