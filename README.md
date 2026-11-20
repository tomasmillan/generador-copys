# Generador de Copys

Herramienta web que genera variaciones de copys para anuncios de Meta y Google Ads usando inteligencia artificial. Escribís una frase de tu anuncio, elegís cuántas variaciones querés y te devuelve versiones con distintos enfoques, en español rioplatense y listas para copiar.

## Sobre el proyecto

Este proyecto nació como parte del curso de Python e IA que estoy haciendo. Vengo de la publicidad y el diseño web, y testear variaciones de copys es algo que hago en todas las campañas, así que quise construir una herramienta propia para hacerlo más rápido.

Fue mi primer proyecto en Python: arranqué con un script en la terminal, lo convertí en una API y le armé una interfaz web.

## Cómo funciona

1. La página web (HTML, CSS y JavaScript) toma la frase y la cantidad de variaciones.
2. Se las envía a una API hecha en Python con FastAPI.
3. La API le pide las variaciones a Claude, el modelo de IA de Anthropic.
4. Las variaciones vuelven a la página, cada una con su botón para copiarla.

## Tecnologías

- **Backend:** Python, FastAPI, Claude API (Anthropic)
- **Frontend:** HTML, CSS, JavaScript
- **Deploy:** Render

## Correrlo en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo "ANTHROPIC_API_KEY=tu_api_key" > .env
uvicorn api:app --reload
```

Después abrí http://127.0.0.1:8000

## API

`POST /variaciones`

```json
{ "frase": "Iluminá tu cuarto con una luna de verdad", "cantidad": 3 }
```

Respuesta:

```json
{ "variaciones": ["...", "...", "..."] }
```

## Autor

**Tomás Millán**: publicista y desarrollador frontend, fundador de [TML Studio](https://tmlstudio.online).

[LinkedIn](https://www.linkedin.com/in/tomasmillanlanhozo/) · [GitHub](https://github.com/tomasmillan)
