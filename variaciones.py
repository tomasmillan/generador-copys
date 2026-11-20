from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

phrase = input("Escribí tu frase: ")
quantity = input("¿Cuántas variaciones deseas generar? ")

response = client.messages.create(

    model="claude-haiku-5-5",
    max_tokens=1000,
    messages= [{
        "role": "user",
        "content": f"""Sos un copywriter de anuncion para Meta y Google Ads en Argentina. Escribi {quantity} variaciones de esta frase, en español rioplatente, cada una con un enfoque distinto. Numeralas y no agregues nada mas.
        Frase: {phrase}"""
    }],
)

print("\n" + response.content[0].text)
