from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import time

tokenizer = AutoTokenizer.from_pretrained("karina-aquino/spanish-sentiment-model")
model = AutoModelForSequenceClassification.from_pretrained("karina-aquino/spanish-sentiment-model")
sentiment_a = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

def analizar_pelicula(text: str):
    
    
    tiempo_init = time.time()

    resultado = sentiment_a(text)
    
    puntuacion = (resultado[0]['label'])

    if puntuacion == "1 star":
        puntuacion_tranformada = -1
        label_puntuacion = "Muy negativo"
    elif puntuacion == "2 star":
        puntuacion_tranformada = -0.5
        label_puntuacion = "Negativo"
    elif puntuacion == "3 star":
        puntuacion_tranformada = 0
        label_puntuacion = "Neutral"
    elif puntuacion == "4 star":
        puntuacion_tranformada = 0.5
        label_puntuacion = "Positivo"
    else: 
        puntuacion_tranformada = 1
        label_puntuacion = "Muy positivo"

    tiempo_fin = time.time() - tiempo_init

    respuesta = {
        'sentimiento': str(puntuacion_tranformada),
        'label_sentimiento': str(label_puntuacion),
        'tiempo_ejecucion': str(tiempo_fin)
    }
    return respuesta