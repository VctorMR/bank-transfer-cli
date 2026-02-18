# ============================================================
# datos.py — Módulo de datos del sistema de transferencias
# Contiene las estructuras de datos principales del sistema:
# listas, diccionarios, tuplas y conjuntos.
# ============================================================

# --- Lista de cuentas (cada cuenta es un diccionario) ---
cuentas = [
    {
        "nombre": "Victor Rincon",
        "alias": "victor.rincon",
        "banco": "Banco Nientiedo",
        "numero_cuenta": 1001,
        "saldo": 1500000.00,
        "mail": "victor@mail.com",
        "contrasena": "victor123"
    },
    {
        "nombre": "Cesar Astorga",
        "alias": "cesar.astorga",
        "banco": "Banco PolyStation",
        "numero_cuenta": 1002,
        "saldo": 85000.50,
        "mail": "cesar@mail.com",
        "contrasena": "cesar123"
    },
    {
        "nombre": "Carlos Garcia",
        "alias": "carlos.garcia",
        "banco": "Banco Esbox",
        "numero_cuenta": 1003,
        "saldo": 2000.75,
        "mail": "carlos@mail.com",
        "contrasena": "carlos123"
    }
]

# --- Tupla de bancos disponibles (inmutable) ---
BANCOS_DISPONIBLES = (
    "Banco Nientiedo",
    "Banco PolyStation",
    "Banco Esbox"
)

# --- Conjuntos para evitar duplicados ---
alias_registrados = {"victor.rincon", "cesar.astorga", "carlos.garcia"}
emails_registrados = {"victor@mail.com", "cesar@mail.com", "carlos@mail.com"}


historial_transferencias = []

siguiente_numero_cuenta = 1004
