"""
Ejercicio 2: Procesador de Textos Inteligente

Permite al usuario ingresar:
- Un texto
- Una tarea a realizar (resumir, profesionalizar u otra)

Usa system_instruction definiendo a la IA como
"Editor Editorial de prestigio".
"""

import os
from dotenv import load_dotenv
from google import genai


def configurar_cliente():
    """
    Configura el cliente de Gemini usando la API Key
    almacenada en el archivo .env
    """
    load_dotenv()
    api_key = os.getenv("GENAI_API_KEY")

    if not api_key:
        raise ValueError("No se encontró GENAI_API_KEY en el archivo .env")

    return genai.Client(api_key=api_key)


def procesar_articulo(texto, tarea):
    """
    Procesa un texto según la tarea indicada.

    Parámetros:
    - texto (str): Texto a procesar.
    - tarea (str): Instrucción que define qué hacer con el texto.

    Retorna:
    - Texto generado por el modelo.
    """

    cliente = configurar_cliente()

    # Rol del sistema
    system_instruction = (
        "Eres un Editor Editorial de prestigio. "
        "Redactas textos con precisión, claridad, coherencia "
        "y alto nivel profesional."
    )

    # Construcción dinámica del prompt
    instruccion_usuario = (
        f"Realiza la siguiente tarea: {tarea}\n\n"
        f"Texto:\n{texto}"
    )

    try:
        response = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=instruccion_usuario,
            config={
                "system_instruction": system_instruction
            }
        )

        if response and response.text:
            return response.text
        else:
            return "No se recibió respuesta del modelo."

    except Exception as e:
        return f"Error al procesar el texto: {e}"


# =========================
# Ejecución interactiva
# =========================
if __name__ == "__main__":

    print("=== Procesador de Textos Inteligente ===\n")

    texto_usuario = input("📄 Ingresa el texto a procesar:\n\n")
    tarea_usuario = input("\n🛠 Ingresa la tarea a realizar (resumir, profesionalizar u otra):\n\n")

    resultado = procesar_articulo(texto_usuario, tarea_usuario)

    print("\n📌 Resultado:\n")
    print(resultado)
