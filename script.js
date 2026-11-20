const form = document.getElementById('copy-form');
const inputFrase = document.getElementById('frase');
const inputCantidad = document.getElementById('cantidad');
const btnGenerar = document.getElementById('btn-generar');
const estado = document.getElementById('estado');
const lista = document.getElementById('copy-list');

const API_URL = location.protocol === 'file:' ? 'http://127.0.0.1:8000' : '';

document.getElementById('anio').textContent = new Date().getFullYear();

form.addEventListener('submit', async (evento) => {
    evento.preventDefault();

    const frase = inputFrase.value.trim();
    const cantidad = Number(inputCantidad.value);

    btnGenerar.disabled = true;
    estado.textContent = 'Generando...';
    lista.innerHTML = '';

    try {
        const respuesta = await fetch(`${API_URL}/variaciones`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ frase, cantidad }),
        });

        const datos = await respuesta.json();

        if (!respuesta.ok) {
            throw new Error(typeof datos.detail === 'string' ? datos.detail : 'Revisá los datos ingresados');
        }

        datos.variaciones.forEach((texto) => {
            const li = document.createElement('li');

            const span = document.createElement('span');
            span.textContent = texto;

            const btnCopiar = document.createElement('button');
            btnCopiar.type = 'button';
            btnCopiar.className = 'btn-copy';
            btnCopiar.textContent = 'Copiar';
            btnCopiar.addEventListener('click', async () => {
                await navigator.clipboard.writeText(texto);
                btnCopiar.textContent = '¡Copiado!';
                setTimeout(() => (btnCopiar.textContent = 'Copiar'), 1500);
            });

            li.append(span, btnCopiar);
            lista.appendChild(li);
        });

        estado.textContent = '';
    } catch (error) {
        estado.textContent = `Error: ${error.message}`;
    } finally {
        btnGenerar.disabled = false;
    }
});
