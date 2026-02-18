# 🏦 Sistema de Transferencias Bancarias

Sistema de gestión de transferencias bancarias desarrollado en Python como proyecto del Módulo 3 del Bootcamp. Permite registrar cuentas, iniciar sesión, realizar transferencias entre cuentas y consultar el historial de movimientos.

## 🚀 Cómo ejecutar

```bash
python3 main.py
```

## 📁 Estructura del proyecto

```
Proyecto de Modulo/
├── main.py              # Menú principal y punto de entrada
├── datos.py             # Datos precargados y estructuras de datos
├── validaciones.py      # Funciones de validación de entrada
├── utilidades.py        # Funciones auxiliares y recursión
├── cuentas.py           # Registro, login y perfil de cuentas
├── transferencias.py    # Transferencias, depósitos e historial
└── README.md            # Documentación del proyecto
```

## 🔧 Funcionalidades

- **Registro de cuenta**: Nombre, alias, banco, email y contraseña con validaciones
- **Inicio de sesión**: Autenticación por email y contraseña
- **Ver perfil**: Datos de la cuenta y saldo actual
- **Transferencias**: Enviar dinero a otra cuenta por alias o número de cuenta
- **Depósitos**: Agregar saldo a la cuenta
- **Historial**: Consultar movimientos realizados (envíos, recepciones y depósitos)
- **Simulador de interés compuesto**: Proyección de saldo con función recursiva

## 🧪 Cuentas de prueba

| Nombre        | Email           | Contraseña | Alias         | Saldo         |
| ------------- | --------------- | ---------- | ------------- | ------------- |
| Victor Rincon | victor@mail.com | victor123  | victor.rincon | $1,500,000.00 |
| Cesar Astorga | cesar@mail.com  | cesar123   | cesar.astorga | $85,000.50    |
| Carlos Garcia | carlos@mail.com | carlos123  | carlos.garcia | $2,000.75     |

## 🛠️ Tecnologías

- Python 3

## 👤 Autor

V
