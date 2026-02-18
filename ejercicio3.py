"""
Ejercicio 3: Chat de Soporte con Historial (Few-Shot)

Sistema de chat para una tienda de tecnología.

Requisitos:
- system_instruction: La IA actúa como vendedor amable.
- Historial precargado con al menos dos ejemplos.
- Bucle de conversación hasta que el usuario escriba "finalizar".
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


def iniciar_chat():
    """
    Inicia el sistema de chat con historial Few-shot.
    """

    cliente = configurar_cliente()

    # Rol del sistema
    system_instruction = (
        "Eres un vendedor amable y experto de una tienda de tecnología. "
        "Respondes con claridad, das especificaciones técnicas y "
        "recomiendas productos según las necesidades del cliente."
    )

    # Historial Few-shot (mínimo dos ejemplos)
    history = [
        {
            "role": "user",
            "parts": [{"text": "¿Qué características tiene el iPhone 15?"}]
        },
        {
            "role": "model",
            "parts": [{"text": "El iPhone 15 cuenta con pantalla OLED de 6.1 pulgadas, chip A16 Bionic, cámara principal de 48 MP y almacenamiento desde 128 GB. Ofrece excelente rendimiento y calidad fotográfica."}]
        },
        {
            "role": "user",
            "parts": [{"text": "¿Qué laptop recomiendas para programación?"}]
        },
        {
            "role": "model",
            "parts": [{"text": "Para programación recomiendo una laptop con al menos 16 GB de RAM, procesador Intel i7 o Ryzen 7 y SSD de 512 GB. Un modelo como la Dell XPS 13 o MacBook Air M2 es una excelente opción."}]
        }
    ]

    print("💻 Bienvenido al Chat de Soporte - Tienda Tech")
    print("Escribe 'finalizar' para terminar la conversación.\n")

    while True:
        mensaje_usuario = input("🧑 Cliente: ")

        if mensaje_usuario.lower() == "finalizar":
            print("\n👋 Gracias por visitar nuestra tienda. ¡Hasta pronto!")
            break

        # Agregar mensaje del usuario al historial
        history.append({
            "role": "user",
            "parts": [{"text": mensaje_usuario}]
        })

        try:
            response = cliente.models.generate_content(
                model="gemini-2.5-flash",
                contents=history,
                config={
                    "system_instruction": system_instruction
                }
            )

            respuesta_modelo = response.text

            print(f"\n🛍️ Vendedor: {respuesta_modelo}\n")

            # Agregar respuesta del modelo al historial
            history.append({
                "role": "model",
                "parts": [{"text": respuesta_modelo}]
            })

        except Exception as e:
            print("Error en la conversación:", e)


# =========================
# Ejecutar Chat
# =========================
if __name__ == "__main__":
    iniciar_chat()
