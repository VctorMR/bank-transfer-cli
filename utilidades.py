# ============================================================
# utilidades.py — Módulo de funciones auxiliares
# Funciones de formato, presentación y una función recursiva
# para cálculo de interés compuesto.
# ============================================================


def limpiar_pantalla():
    """Imprime líneas en blanco para simular limpiar la consola."""
    print("\n" * 3)


def mostrar_encabezado(titulo):
    """Muestra un encabezado formateado con el título centrado."""
    largo = 50
    print("=" * largo)
    print(f"{titulo:^{largo}}")
    print("=" * largo)


def formatear_saldo(monto):
    """Retorna el monto formateado como moneda. Ejemplo: $1,234.56"""
    return f"${monto:,.2f}"


def mostrar_separador():
    """Imprime una línea separadora."""
    print("-" * 50)


def calcular_interes_compuesto(capital, tasa, periodos):
    """
    Calcula el interés compuesto de forma RECURSIVA.
    capital: monto inicial
    tasa: tasa de interés por período (ejemplo: 0.05 para 5%)
    periodos: cantidad de períodos restantes
    Retorna el capital final después de todos los períodos.
    """
    # Caso base: no quedan períodos
    if periodos == 0:
        return capital

    # Caso recursivo: aplicar un período y llamar de nuevo
    nuevo_capital = capital * (1 + tasa)
    return calcular_interes_compuesto(nuevo_capital, tasa, periodos - 1)


def mostrar_tabla_cuentas(lista_cuentas):
    """Muestra una tabla formateada con los datos públicos de las cuentas."""
    mostrar_encabezado("DIRECTORIO DE CUENTAS")

    if len(lista_cuentas) == 0:
        print("❌ No hay cuentas registradas.")
        return

    for i, cuenta in enumerate(lista_cuentas):
        print(f"  {i + 1}. {cuenta['nombre']}")
        print(f"     Alias: {cuenta['alias']}")
        print(f"     Banco: {cuenta['banco']}")
        print(f"     Cuenta N°: {cuenta['numero_cuenta']}")
        mostrar_separador()
