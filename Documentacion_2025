# 📚 Documentación para el Uso de Ollama

## 📋 Descripción del Proyecto

Este documento explica cómo usar **Ollama** para ejecutar modelos de lenguaje grandes (LLM) de manera local. Incluye ejemplos de código y comentarios para facilitar la integración.

---

## 🛠️ Requisitos Previos

1. Tener Python 3.10+ instalado.
2. Crear una cuenta en Ollama y obtener tu API Key.
3. Instalar el paquete `ollama`:

```bash
pip install ollama
```

---

## 🚀 Primeros Pasos

### 🔑 Configurar la API Key

Primero, debes configurar tu API Key. Esto se hace a través de una variable de entorno:

```bash
export OLLAMA_API_KEY="tu-api-key"
```

En Windows, usa:

```bash
set OLLAMA_API_KEY="tu-api-key"
```

---

## 📚 Funcionalidades Básicas

### 📝 Generación de Texto con Manejo de Errores

Puedes generar texto usando la función `chat()` para simular una conversación. Aquí hay un ejemplo más completo con manejo de errores y comentarios para facilitar la comprensión:

```python
import ollama

# Definir el prompt y el modelo
prompt = "Escribe un código de Python que imprima los números del 1 al 100 en una función."
modelo = "llama3.2"

try:
    # Enviar el mensaje al modelo
    response = ollama.chat(
        model=modelo,
        messages=[{'role': 'user', 'content': prompt}]
    )
    
    # Extraer y mostrar el contenido de la respuesta
    if 'message' in response and 'content' in response['message']:
        print("📋 Respuesta del Modelo:\n")
        print(response['message']['content'])
    else:
        print("⚠️ No se encontró contenido en la respuesta.")

except Exception as e:
    print(f"❌ Error al generar respuesta: {e}")
```

#### 🧪 Prueba Rápida

Ejecuta el código anterior para verificar que tu configuración es correcta. Deberías recibir una respuesta generada por el modelo, o un mensaje de error en caso de que algo falle.

---

### 📋 Entrenamiento Personalizado

Puedes entrenar tu propio modelo para respuestas personalizadas:

```python
import ollama

# Datos de entrenamiento personalizados
datos = [
    {"input": "Hola, ¿cómo estás?", "output": "Bien, gracias."},
    {"input": "¿Cuál es tu nombre?", "output": "Soy un modelo personalizado."}
]

# Entrenando el modelo
ollama.train(model_name="mi-modelo", data=datos)
```

#### 🧪 Prueba de Entrenamiento

Después de entrenar el modelo, prueba con:

```python
prompt = "¿Cómo estás?"
modelo = "mi-modelo"

response = ollama.chat(model=modelo,
                       messages=[{'role': 'user', 'content': prompt}])

print(response['message']['content'])
```

---


