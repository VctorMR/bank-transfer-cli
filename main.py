# ============================================================
# main.py — Punto de entrada del Sistema de Transferencias
# Menú principal que integra todos los módulos del sistema.
# ============================================================

from utilidades import mostrar_encabezado, limpiar_pantalla, mostrar_separador
from validaciones import pedir_opcion
from cuentas import registrar_cuenta, iniciar_sesion, ver_perfil, ver_simulador_interes
from transferencias import realizar_transferencia, depositar, ver_historial


def mostrar_menu_bienvenida():
    """Muestra el menú de bienvenida del sistema."""
    mostrar_encabezado("SISTEMA DE TRANSFERENCIAS BANCARIAS")
    print("  1. Iniciar sesión")
    print("  2. Registrarse")
    print("  3. Salir")
    mostrar_separador()


def mostrar_menu_principal(cuenta):
    """Muestra el menú principal después de iniciar sesión."""
    mostrar_encabezado(f"MENÚ PRINCIPAL — {cuenta['nombre']}")
    print("  1. 👤 Ver mi perfil")
    print("  2. 💸 Realizar transferencia")
    print("  3. 💰 Depositar dinero")
    print("  4. 📋 Ver historial de movimientos")
    print("  5. 📈 Simulador de interés compuesto")
    print("  6. 🚪 Cerrar sesión")
    mostrar_separador()


def menu_sesion(cuenta):
    """Menú principal del usuario logueado. Bucle hasta cerrar sesión."""
    while True:
        limpiar_pantalla()
        mostrar_menu_principal(cuenta)
        opcion = pedir_opcion("  Seleccione una opción: ", ["1", "2", "3", "4", "5", "6"])

        if opcion == "1":
            ver_perfil(cuenta)
            input("\n  Presione Enter para continuar...")

        elif opcion == "2":
            realizar_transferencia(cuenta)
            input("\n  Presione Enter para continuar...")

        elif opcion == "3":
            depositar(cuenta)
            input("\n  Presione Enter para continuar...")

        elif opcion == "4":
            ver_historial(cuenta)
            input("\n  Presione Enter para continuar...")

        elif opcion == "5":
            ver_simulador_interes(cuenta)
            input("\n  Presione Enter para continuar...")

        elif opcion == "6":
            print("\n  👋 Sesión cerrada. ¡Hasta pronto!")
            break


def main():
    """Función principal del programa."""
    while True:
        limpiar_pantalla()
        mostrar_menu_bienvenida()
        opcion = pedir_opcion("  Seleccione una opción: ", ["1", "2", "3"])

        if opcion == "1":
            cuenta = iniciar_sesion()
            if cuenta is not None:
                menu_sesion(cuenta)

            input("\n  Presione Enter para continuar...")

        elif opcion == "2":
            registrar_cuenta()
            input("\n  Presione Enter para continuar...")

        elif opcion == "3":
            print("\n  👋 ¡Gracias por usar el Sistema de Transferencias!")
            print("  Hasta pronto. 🚀")
            break


# --- Punto de entrada ---
if __name__ == "__main__":
    main()
