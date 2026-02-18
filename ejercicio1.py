"""
Ejercicio 1: Conexión básica a Gemini
Explica qué es la Inferencia en IA en menos de 50 palabras.
"""

import os
from dotenv import load_dotenv
from google import genai


def configurar_cliente():
    """
    Carga la API Key desde el archivo .env
    e inicializa el cliente de Gemini.
    """
    load_dotenv()
    api_key = os.getenv("GENAI_API_KEY")

    if not api_key:
        raise ValueError("No se encontró GENAI_API_KEY en el archivo .env")

    return genai.Client(api_key=api_key)


def explicar_inferencia(cliente):
    """
    Realiza una consulta simple al modelo Gemini.
    """
    prompt = (
        "Explica qué es la Inferencia en Inteligencia Artificial "
        "en menos de 50 palabras."
    )

    try:
        response = cliente.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if response and response.text:
            print("\n📘 Respuesta del modelo:\n")
            print(response.text)
        else:
            print("No se recibió respuesta del modelo.")

    except Exception as e:
        print("Error al consultar el modelo:", e)


if __name__ == "__main__":
    cliente = configurar_cliente()
    explicar_inferencia(cliente)
