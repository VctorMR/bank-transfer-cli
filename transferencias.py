# ============================================================
# transferencias.py — Módulo de transferencias
# Funciones para realizar transferencias, depósitos
# y consultar el historial de movimientos.
# ============================================================

from datos import historial_transferencias
from cuentas import buscar_cuenta_por_alias, buscar_cuenta_por_numero
from validaciones import validar_monto, pedir_opcion
from utilidades import mostrar_encabezado, formatear_saldo, mostrar_separador


def realizar_transferencia(cuenta_origen):
    """Realiza una transferencia desde la cuenta de origen a otra cuenta."""
    mostrar_encabezado("REALIZAR TRANSFERENCIA")

    print(f"  Saldo disponible: {formatear_saldo(cuenta_origen['saldo'])}\n")

    if cuenta_origen["saldo"] <= 0:
        print("❌ No tiene saldo disponible para transferir.")
        return

    # --- Elegir método de búsqueda ---
    print("  ¿Cómo desea buscar al destinatario?")
    print("  1. Por alias")
    print("  2. Por número de cuenta")
    opcion = pedir_opcion("  Seleccione una opción: ", ["1", "2"])

    cuenta_destino = None

    if opcion == "1":
        alias = input("  Ingrese el alias del destinatario: ").strip().lower()
        cuenta_destino = buscar_cuenta_por_alias(alias)
    elif opcion == "2":
        try:
            numero = int(input("  Ingrese el número de cuenta del destinatario: "))
            cuenta_destino = buscar_cuenta_por_numero(numero)
        except ValueError:
            print("❌ Debe ingresar un número válido.")
            return

    # --- Verificar que se encontró la cuenta ---
    if cuenta_destino is None:
        print("❌ No se encontró la cuenta del destinatario.")
        return

    # --- Verificar que no sea la misma cuenta ---
    if cuenta_destino["numero_cuenta"] == cuenta_origen["numero_cuenta"]:
        print("❌ No puede transferir a su propia cuenta.")
        return

    # --- Mostrar datos del destinatario ---
    print(f"\n  Destinatario encontrado:")
    print(f"    Nombre: {cuenta_destino['nombre']}")
    print(f"    Alias:  {cuenta_destino['alias']}")
    print(f"    Banco:  {cuenta_destino['banco']}")

    # --- Pedir y validar monto ---
    monto = None
    while monto is None:
        monto = validar_monto(input("\n  Ingrese el monto a transferir: "))

    # --- Verificar saldo suficiente ---
    if monto > cuenta_origen["saldo"]:
        print(f"❌ Saldo insuficiente. Su saldo es {formatear_saldo(cuenta_origen['saldo'])}")
        return

    # --- Confirmar transferencia ---
    print(f"\n  Resumen de la transferencia:")
    print(f"    De:    {cuenta_origen['nombre']} ({cuenta_origen['alias']})")
    print(f"    Para:  {cuenta_destino['nombre']} ({cuenta_destino['alias']})")
    print(f"    Monto: {formatear_saldo(monto)}")

    confirmar = pedir_opcion("\n  ¿Confirmar transferencia? (s/n): ", ["s", "n"])

    if confirmar == "n":
        print("❌ Transferencia cancelada.")
        return

    # --- Ejecutar transferencia ---
    cuenta_origen["saldo"] -= monto
    cuenta_destino["saldo"] += monto

    # Guardar en historial como tupla (inmutable)
    registro = (
        cuenta_origen["alias"],
        cuenta_destino["alias"],
        monto,
        "transferencia"
    )
    historial_transferencias.append(registro)

    print(f"\n✅ Transferencia exitosa!")
    print(f"   Nuevo saldo: {formatear_saldo(cuenta_origen['saldo'])}")
    mostrar_separador()


def depositar(cuenta):
    """Deposita dinero en la cuenta del usuario."""
    mostrar_encabezado("DEPOSITAR DINERO")

    print(f"  Saldo actual: {formatear_saldo(cuenta['saldo'])}\n")

    monto = None
    while monto is None:
        monto = validar_monto(input("  Ingrese el monto a depositar: "))

    cuenta["saldo"] += monto

    # Guardar en historial como tupla
    registro = (
        "deposito",
        cuenta["alias"],
        monto,
        "deposito"
    )
    historial_transferencias.append(registro)

    print(f"\n✅ Depósito exitoso!")
    print(f"   Nuevo saldo: {formatear_saldo(cuenta['saldo'])}")
    mostrar_separador()


def ver_historial(cuenta):
    """Muestra el historial de transferencias de la cuenta."""
    mostrar_encabezado("HISTORIAL DE MOVIMIENTOS")

    alias_usuario = cuenta["alias"]
    movimientos_encontrados = 0

    for registro in historial_transferencias:
        origen, destino, monto, tipo = registro

        # Usar continue para saltar registros que no pertenecen a esta cuenta
        if origen != alias_usuario and destino != alias_usuario:
            continue

        movimientos_encontrados += 1

        if tipo == "deposito":
            print(f"  📥 DEPÓSITO")
            print(f"     Monto: {formatear_saldo(monto)}")
        elif origen == alias_usuario:
            print(f"  📤 TRANSFERENCIA ENVIADA")
            print(f"     Para: {destino}")
            print(f"     Monto: {formatear_saldo(monto)}")
        else:
            print(f"  📥 TRANSFERENCIA RECIBIDA")
            print(f"     De: {origen}")
            print(f"     Monto: {formatear_saldo(monto)}")

        mostrar_separador()

    if movimientos_encontrados == 0:
        print("  No hay movimientos registrados.")
        mostrar_separador()
