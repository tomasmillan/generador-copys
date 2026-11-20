from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-haiku-5-5",
    max_tokens=300,
    messages=[{"role": "user", "content": "Dame 3 hooks para un anuncio de un cargador inalambrico portatil"}],
)

print (response.content[0].text)