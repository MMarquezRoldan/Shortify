# Shortify - CLI URL Shortener

Un script sencillo y eficiente en Python para acortar enlaces directamente desde la línea de comandos (CMD) de Windows. Utiliza el servicio `is.gd` para generar enlaces cortos y fiables sin necesidad de claves API.

## Características

- **Fast:** Shorten links in seconds directly from the terminal.
- **Global:** Works from any folder using the `shortify` command.
- **No API Key:** Uses `is.gd` (via `pyshorteners`), so no registration is required.
- **Error Handling:** Detects connection issues and suggests using quotes for complex URLs.

## Requirements

- Python 3.x installed.
- `pyshorteners` library.

## Installation

### 1. Install Dependencies

Open your terminal and run:

```bash
pip install pyshorteners
```

### 2\. Setup Files

Create a dedicated folder (e.g., C:\\Scripts) and place the following two files inside.

**File 1: acortar.py (The main script)**Ensure this file contains the Python logic using pyshorteners.

**File 2: shortify.bat (The launcher)**Create a file named shortify.bat with the following content:

`   @echo off  python "%~dp0shortify.py" %*   `

### 3\. Configure System Path

To use the command globally:

1.  Open Windows Search and type **"Edit the system environment variables"**.
    
2.  Click **Environment Variables**.
    
3.  Under **System variables**, find Path and click **Edit**.
    
4.  Click **New** and paste the path to your folder (e.g., C:\\Scripts).
    
5.  Click **OK** to save changes.
    

> **Note:** You must restart your terminal (CMD) for the changes to take effect.

Usage
-----

### Simple URLs

For standard links, simply type:

Bash

`   shortify [https://www.google.com](https://www.google.com)   `

### Complex URLs (YouTube, Queries)

If the URL contains special characters like &, ?, or =, **you must use quotes**. Windows CMD interprets & as a command separator otherwise.

Bash

`   shortify "[https://www.youtube.com/watch?v=VIDEOID&t=10s](https://www.youtube.com/watch?v=VIDEOID&t=10s)"   `

Troubleshooting
---------------

**Error: "The system cannot find the file specified"**Ensure both acortar.py and shortify.bat are in the same folder.

**Error: "limited" or broken link**This usually happens when shortening URLs with parameters (like &) without quotes. The script only receives the first part of the URL. Always use quotes ("") for long or complex links.
