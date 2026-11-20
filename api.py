from dotenv import load_dotenv
import anthropic
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

load_dotenv()
client = anthropic.Anthropic()

app = FastAPI(title="Generador de copys")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST", "GET"],
    allow_headers=["*"],
)


class Pedido(BaseModel):
    frase: str = Field(..., min_length=3, max_length=500)
    cantidad: int = Field(3, ge=1, le=10)


class Respuesta(BaseModel):
    variaciones: list[str]


@app.get("/")
def pagina():
    return FileResponse("index.html")


@app.get("/style.css")
def estilos():
    return FileResponse("style.css")


@app.get("/script.js")
def script():
    return FileResponse("script.js")


@app.get("/estado")
def estado():
    return {"ok": True, "mensaje": "API del generador de copys funcionando"}


@app.post("/variaciones", response_model=Respuesta)
def generar_variaciones(pedido: Pedido):
    prompt = f"""Sos un copywriter de anuncios para Meta y Google Ads en Argentina.
Escribí {pedido.cantidad} variaciones de esta frase, en español rioplatense, cada una con un enfoque distinto.
Devolvé una variación por línea, sin números, sin viñetas y sin nada más.
Frase: {pedido.frase}"""

    try:
        response = client.messages.create(
            model="claude-haiku-5-5",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
    except anthropic.APIError as e:
        raise HTTPException(status_code=502, detail=f"Error de la API de Claude: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"{type(e).__name__}: {e}")

    texto = "".join(b.text for b in response.content if b.type == "text")
    variaciones = [linea.strip() for linea in texto.split("\n") if linea.strip()]
    return {"variaciones": variaciones[: pedido.cantidad]}
