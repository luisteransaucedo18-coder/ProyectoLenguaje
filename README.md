# Sistema web recomendador de juegos

Aplicacion web hecha con Flask para recomendar videojuegos segun las preferencias del usuario. El proyecto usa Supabase PostgreSQL como base de datos, procesamiento funcional para puntuar juegos y reglas logicas con pyDatalog para reforzar recomendaciones.

## Requisitos

- Python 3.11 o superior
- pip
- Una cuenta/proyecto en Supabase

## Instalacion

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
```

## Variables de entorno

Copia `.env.example` como `.env` y usa estas variables:

```env
NEXT_PUBLIC_SUPABASE_URL=https://yishbkgdsxvosxyqfvlu.supabase.co
NEXT_PUBLIC_SUPABASE_PUBLISHABLE_KEY=sb_publishable_kaEBLkwbaKyhOhjwiR1vkQ_9EEFnEbL
```

El proyecto tambien acepta `SUPABASE_URL` y `SUPABASE_PUBLISHABLE_KEY` como nombres alternativos, pero se dejaron las variables `NEXT_PUBLIC_` porque fueron las solicitadas.

## Base de datos en Supabase

1. Entra a tu proyecto de Supabase.
2. Abre `SQL Editor`.
3. Copia todo el contenido de `database_schema.sql`.
4. Ejecuta el script.

Ese archivo crea la tabla `public.games`, activa RLS, agrega una politica de lectura para `anon` y `authenticated`, y carga los juegos iniciales con `insert ... on conflict`.

## Ejecucion

```powershell
py app.py
```

Luego abre:

```text
http://127.0.0.1:5000
```

Si Supabase no responde o la tabla no existe, la aplicacion usa los juegos locales de `src/data.py` como respaldo para que el recomendador siga funcionando.

## Estructura

```text
app.py
database_schema.sql  Script PostgreSQL para crear tablas y datos en Supabase
src/
  controller.py      Controlador principal de Flask
  database.py        Conexion y lectura de juegos desde Supabase
  data.py            Base local de respaldo con mas de 10 juegos
  logic_rules.py     Reglas e inferencias con pyDatalog
  processor.py       Ranking funcional y normalizacion de preferencias
templates/
  index.html         Interfaz web
static/
  css/styles.css     Estilos visuales oscuros similares a Steam
```

## Paradigmas usados

- Imperativo/OO: `GameRecommendationController` coordina rutas, flujo, peticiones y respuestas.
- Funcional: `processor.py` usa funciones puras, `map()`, `filter()`, `reduce()` y `lambda` para puntuar y ordenar juegos.
- Logico: `logic_rules.py` usa `pyDatalog` para inferir recomendaciones por reglas como relajarse, reto o juego social.
