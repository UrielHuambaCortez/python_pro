import random

# Selecciona un emoji al azar al inicio
emojis = ['😀', '😂', '🥰', '😎', '🤔', '🙃', '😴', '🤯', '🎉', '🔥', '🌈', '🍕', '🚀', '🐱', '🐶']
selected_emoji = random.choice(emojis)

def emoji_string(length):
    # Usa el emoji seleccionado para generar la cadena
    return selected_emoji * length

def secret_function(a, b):
    # Genera una cadena de emojis basada en la longitud total de los argumentos
    total_length = len(str(a)) + len(str(b))
    return emoji_string(total_length)

print(secret_function(1, 2))
print(secret_function("¡Hola, ", "Mundo!"))