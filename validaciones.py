# ============================================================
# validaciones.py — Módulo de validación de entradas
# Funciones para validar datos ingresados por el usuario.
# Cada función retorna True/False o el valor validado.
# ============================================================


def validar_monto(texto):
    """Valida que el texto sea un número positivo. Retorna el monto o None."""
    try:
        monto = float(texto)
        if monto <= 0:
            print("❌ El monto debe ser mayor a cero.")
            return None
        return monto
    except ValueError:
        print("❌ Debe ingresar un número válido.")
        return None


def validar_email(texto):
    """Valida formato básico de email (contiene @ y .)."""
    texto = texto.strip().lower()
    if "@" not in texto or "." not in texto:
        print("❌ El email debe contener '@' y '.' (ejemplo: usuario@mail.com)")
        return None
    if len(texto) < 5:
        print("❌ El email es demasiado corto.")
        return None
    return texto


def validar_contrasena(texto):
    """Valida que la contraseña tenga al menos 6 caracteres y un número."""
    if len(texto) < 6:
        print("❌ La contraseña debe tener al menos 6 caracteres.")
        return None

    tiene_numero = False
    for caracter in texto:
        if caracter.isdigit():
            tiene_numero = True
            break

    if not tiene_numero:
        print("❌ La contraseña debe contener al menos un número.")
        return None

    return texto


def validar_nombre(texto):
    """Valida que el nombre no esté vacío y solo contenga letras y espacios."""
    texto = texto.strip()
    if len(texto) == 0:
        print("❌ El nombre no puede estar vacío.")
        return None

    for caracter in texto:
        if not caracter.isalpha() and caracter != " ":
            print("❌ El nombre solo puede contener letras y espacios.")
            return None

    return texto


def validar_alias(texto, alias_registrados):
    """Valida que el alias no esté vacío, sin espacios y no esté duplicado."""
    texto = texto.strip().lower()
    if len(texto) == 0:
        print("❌ El alias no puede estar vacío.")
        return None
    if " " in texto:
        print("❌ El alias no puede contener espacios.")
        return None
    if texto in alias_registrados:
        print("❌ Ese alias ya está registrado. Elija otro.")
        return None
    return texto


def pedir_opcion(mensaje, opciones_validas):
    """Pide al usuario una opción válida. Repite hasta obtenerla."""
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        else:
            print(f"❌ Opción no válida. Las opciones son: {', '.join(opciones_validas)}")
