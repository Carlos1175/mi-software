# Proyecto Final - Generador de Contraseñas
# Autor: Carlos
# Objetivo: Versión interactiva por consola con input()

import random
import string

def es_contrasena_fuerte(contra):
    """Evalúa si una contraseña es fuerte según criterios de seguridad"""
    mayus = any(c.isupper() for c in contra)
    minus = any(c.islower() for c in contra)
    nums = any(c.isdigit() for c in contra)
    simb = any(c in string.punctuation for c in contra)
    largo = len(contra) >= 8
    return largo and sum([mayus, minus, nums, simb]) >= 3

def contrasena_personalizada():
    """Permite al usuario crear su propia contraseña"""
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    while True:
        contra = input(f"Ingrese su contraseña personalizada de {longitud} caracteres: ")
        if len(contra) == longitud:
            return contra
        print("La contraseña no cumple con la longitud indicada.")

def facil_de_decir(longitud):
    """Genera contraseña solo con letras (fácil de pronunciar)"""
    return ''.join(random.choice(string.ascii_letters) for _ in range(longitud))

def facil_de_leer(longitud):
    """Genera contraseña personalizable sin caracteres confusos"""
    chars = string.ascii_letters
    if input("¿Incluir números? (s/n): ").lower() == 's':
        chars += string.digits
    if input("¿Incluir símbolos? (s/n): ").lower() == 's':
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(longitud))

def todos_los_caracteres(longitud):
    """Genera contraseña con todos los tipos de caracteres o personalizada"""
    print("Por defecto se usará una combinación de mayúsculas, minúsculas, números y símbolos.")
    usar_defecto = input("¿Usar combinación por defecto? (s/n): ").lower()
    
    if usar_defecto == 's':
        chars = string.ascii_letters + string.digits + string.punctuation
    else:
        chars = ''
        if input("¿Incluir mayúsculas? (s/n): ").lower() == 's':
            chars += string.ascii_uppercase
        if input("¿Incluir minúsculas? (s/n): ").lower() == 's':
            chars += string.ascii_lowercase
        if input("¿Incluir números? (s/n): ").lower() == 's':
            chars += string.digits
        if input("¿Incluir símbolos? (s/n): ").lower() == 's':
            chars += string.punctuation
    
    if not chars:
        print("Debe seleccionar al menos un tipo de carácter.")
        return None
    
    return ''.join(random.choice(chars) for _ in range(longitud))

def menu_generador():
    """Muestra el menú de opciones de generación"""
    print("\n--- Menú del Generador ---")
    print("1. Yo genero mi propia contraseña")
    print("2. Contraseña automática fácil de decir")
    print("3. Contraseña automática fácil de leer")
    print("4. Todos los caracteres")
    
    op = input("Seleccione una opción: ")
    
    if op == '1':
        return contrasena_personalizada()
    
    try:
        longitud = int(input("Ingrese la longitud de la contraseña: "))
        if longitud <= 0:
            print("La longitud debe ser un número positivo.")
            return None
    except ValueError:
        print("Por favor ingrese un número válido.")
        return None
    
    if op == '2':
        return facil_de_decir(longitud)
    elif op == '3':
        return facil_de_leer(longitud)
    elif op == '4':
        return todos_los_caracteres(longitud)
    else:
        print("Opción inválida.")
        return None

def main():
    """Función principal del programa"""
    print("=== Bienvenido al Generador de Contraseñas ===")
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Generar contraseña")
        print("2. Reglas del generador")
        print("3. Salir")
        
        op = input("Seleccione una opción: ")
        
        if op == '1':
            contra = menu_generador()
            if contra:
                print(f"\nContraseña generada: {contra}")
                nivel = "FUERTE" if es_contrasena_fuerte(contra) else "DÉBIL"
                print(f"Nivel de seguridad: {nivel}")
                
                if nivel == "DÉBIL":
                    print("💡 Sugerencia: Para mayor seguridad, use al menos 8 caracteres")
                    print("   y combine mayúsculas, minúsculas, números y símbolos.")
                
                guardar = input("¿Desea guardar la contraseña? (si/no): ").lower()
                if guardar in ['si', 's', 'sí']:
                    try:
                        with open("contraseñas_guardadas.txt", "a", encoding="utf-8") as f:
                            f.write(f"{contra}\n")
                        print("✅ Contraseña guardada en 'contraseñas_guardadas.txt'")
                    except Exception as e:
                        print(f"❌ Error al guardar: {e}")
        
        elif op == '2':
            print("\n📋 REGLAS DEL GENERADOR:")
            print("• Mínimo 8 caracteres para ser considerada segura")
            print("• Combinar mayúsculas, minúsculas, números y símbolos")
            print("• Se requieren mínimo 3 tipos diferentes de caracteres")
            print("• Evitar información personal o palabras comunes")
            print("• Usar contraseñas únicas para cada cuenta")
        
        elif op == '3':
            print("\n¡Gracias por usar el Generador de Contraseñas!")
            print("Mantén tus contraseñas seguras. 🔐")
            break
        
        else:
            print("❌ Opción inválida. Por favor seleccione 1, 2 o 3.")

if __name__ == '__main__':
    main()