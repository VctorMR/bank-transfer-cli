# ============================================================
# cuentas.py — Módulo de gestión de cuentas
# Funciones para registrar, buscar e iniciar sesión en cuentas.
# ============================================================

from datos import (
    cuentas, BANCOS_DISPONIBLES, alias_registrados,
    emails_registrados, siguiente_numero_cuenta
)
from validaciones import (
    validar_nombre, validar_alias, validar_email,
    validar_contrasena, pedir_opcion
)
from utilidades import (
    mostrar_encabezado, formatear_saldo, mostrar_separador,
    calcular_interes_compuesto
)
import datos


def registrar_cuenta():
    """Registra una nueva cuenta pidiendo todos los datos al usuario."""
    mostrar_encabezado("REGISTRAR NUEVA CUENTA")

    # --- Validar nombre ---
    nombre = None
    while nombre is None:
        nombre = validar_nombre(input("Ingrese su nombre completo: "))

    # --- Validar alias ---
    alias = None
    while alias is None:
        alias = validar_alias(
            input("Ingrese un alias (sin espacios): "),
            alias_registrados
        )

    # --- Seleccionar banco ---
    print("\nBancos disponibles:")
    for i, banco in enumerate(BANCOS_DISPONIBLES):
        print(f"  {i + 1}. {banco}")

    opciones_banco = []
    for i in range(len(BANCOS_DISPONIBLES)):
        opciones_banco.append(str(i + 1))

    opcion_banco = pedir_opcion(
        "Seleccione el número del banco: ",
        opciones_banco
    )
    banco = BANCOS_DISPONIBLES[int(opcion_banco) - 1]

    # --- Validar email ---
    email = None
    while email is None:
        email = validar_email(input("Ingrese su email: "))
        if email is not None and email in emails_registrados:
            print("❌ Ese email ya está registrado.")
            email = None

    # --- Validar contraseña ---
    contrasena = None
    while contrasena is None:
        contrasena = validar_contrasena(input("Ingrese su contraseña (mín. 6 caracteres, al menos 1 número): "))

    # --- Crear la cuenta ---
    nueva_cuenta = {
        "nombre": nombre,
        "alias": alias,
        "banco": banco,
        "numero_cuenta": datos.siguiente_numero_cuenta,
        "saldo": 0.00,
        "mail": email,
        "contrasena": contrasena
    }

    # Actualizar datos globales
    cuentas.append(nueva_cuenta)
    alias_registrados.add(alias)
    emails_registrados.add(email)
    datos.siguiente_numero_cuenta += 1

    print(f"\n✅ Cuenta creada exitosamente!")
    print(f"   Nombre: {nombre}")
    print(f"   Alias: {alias}")
    print(f"   Banco: {banco}")
    print(f"   N° de cuenta: {nueva_cuenta['numero_cuenta']}")
    mostrar_separador()

    return nueva_cuenta


def iniciar_sesion():
    """Pide mail y contraseña, busca en la lista de cuentas."""
    mostrar_encabezado("INICIAR SESIÓN")

    mail = input("Ingrese su email: ").strip().lower()
    contrasena = input("Ingrese su contraseña: ").strip()

    for cuenta in cuentas:
        if cuenta["mail"] == mail and cuenta["contrasena"] == contrasena:
            print(f"\n✅ Bienvenido/a, {cuenta['nombre']}!")
            return cuenta

    print("❌ Email o contraseña incorrectos.")
    return None


def ver_perfil(cuenta):
    """Muestra los datos del perfil de la cuenta."""
    mostrar_encabezado("MI PERFIL")
    print(f"  Nombre:        {cuenta['nombre']}")
    print(f"  Alias:         {cuenta['alias']}")
    print(f"  Banco:         {cuenta['banco']}")
    print(f"  N° de cuenta:  {cuenta['numero_cuenta']}")
    print(f"  Saldo:         {formatear_saldo(cuenta['saldo'])}")
    print(f"  Email:         {cuenta['mail']}")
    mostrar_separador()


def buscar_cuenta_por_alias(alias):
    """Busca una cuenta por alias. Retorna el diccionario o None."""
    alias = alias.strip().lower()
    for cuenta in cuentas:
        if cuenta["alias"] == alias:
            return cuenta
    return None


def buscar_cuenta_por_numero(numero):
    """Busca una cuenta por número. Retorna el diccionario o None."""
    for cuenta in cuentas:
        if cuenta["numero_cuenta"] == numero:
            return cuenta
    return None


def ver_simulador_interes(cuenta):
    """Simula interés compuesto sobre el saldo usando función recursiva."""
    mostrar_encabezado("SIMULADOR DE INTERÉS COMPUESTO")

    if cuenta["saldo"] <= 0:
        print("❌ No tiene saldo para simular. Deposite dinero primero.")
        return

    print(f"  Saldo actual: {formatear_saldo(cuenta['saldo'])}")
    print(f"\n  Simulación con tasa mensual del 5%:\n")

    tasa = 0.05
    for periodo in range(1, 13):
        saldo_futuro = calcular_interes_compuesto(cuenta["saldo"], tasa, periodo)
        ganancia = saldo_futuro - cuenta["saldo"]
        print(f"  Mes {periodo:>2}: {formatear_saldo(saldo_futuro)}  (ganancia: {formatear_saldo(ganancia)})")

    mostrar_separador()
