# Sistema web recomendador de juegos

Aplicacion web hecha con Flask para recomendar videojuegos segun preferencias del usuario.

## Requisitos

- Python 3.11 o superior
- pip

## Instalacion

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Conexion MySQL

La aplicacion usa MySQL en `localhost:3306` con el usuario `root`.

1. Copia `.env.example` como `.env`.
2. Coloca tu contrasena en `MYSQL_PASSWORD`.
3. Ejecuta la aplicacion.

Ejemplo:

```env
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=root
MYSQL_PASSWORD=tu_contrasena
MYSQL_DATABASE=gamematch
```

Al iniciar, el sistema crea automaticamente la base `gamematch`, crea la tabla `games` y carga los juegos iniciales si la tabla esta vacia.

## Ejecucion

```powershell
python app.py
```

Luego abre:

```text
http://127.0.0.1:5000
```

## Estructura

```text
app.py
src/
  controller.py     Controlador principal, flujo imperativo y eventos web
  database.py       Conexion MySQL, creacion de tablas y lectura de juegos
  data.py           Base de conocimiento con mas de 10 juegos
  logic_rules.py    Reglas e inferencias con pyDatalog
  processor.py      Procesamiento funcional, ranking y funciones puras
templates/
  index.html        Interfaz web
static/
  css/styles.css    Estilos visuales
```

## Paradigmas usados

- Imperativo/OO: `GameRecommendationController` coordina rutas, flujo, peticiones y respuestas.
- Funcional: `processor.py` usa funciones puras, `map()`, `filter()`, `reduce()` y `lambda` para puntuar y ordenar juegos.
- Logico: `logic_rules.py` usa `pyDatalog` para inferir recomendaciones por reglas como relajarse, reto o juego social.
