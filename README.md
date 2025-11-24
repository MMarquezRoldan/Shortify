# Shortify - CLI URL Shortener

Un script sencillo y eficiente en Python para acortar enlaces directamente desde la línea de comandos (CMD) de Windows. Utiliza el servicio `is.gd` para generar enlaces cortos y fiables sin necesidad de claves API.

## Características

- **Rápido:** Acorta enlaces en segundos desde la terminal.
- **Global:** Funciona desde cualquier carpeta usando el comando `shortify`.
- **Sin API Key:** Usa `is.gd` (vía `pyshorteners`), por lo que no requiere registro.
- **Manejo de Errores:** Detecta problemas de conexión y sugiere el uso de comillas para URLs complejas.

## Requisitos

- Python 3.x instalado.
- Librería `pyshorteners`.

## Instalación

### 1. Instalar dependencias

Abre tu terminal y ejecuta:

```bash
pip install pyshorteners
```
