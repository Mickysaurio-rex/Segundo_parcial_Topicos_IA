import csv
import datetime
from fastapi import (
    FastAPI,
    HTTPException,
    Response,
    status
)
from fastapi.responses import FileResponse
from src.sentiment_movies import analizar_pelicula
from src.analysis import spacy_analysis

app = FastAPI(title = "Procesador de Texto - Segundo Parcial")

list_sentiment = []

@app.get("/status")
def inicializarServicio(
    nombre: str
) -> dict[str, str]:
    return {
        "mensaje_bienvenida": f"Hola {nombre} bievenido al servicio de procesamiento de texto. A continuación se presentarán funciones que brindarán información específica de textos que usted coloque",
        "modelo_1": "spanish-sentiment-model by karina-aquino",
        "modelo_2": "spaCy by Matt Honnibal",
        "status": "En línea, listo para trabajar" 
    }

@app.post("/sentiment")
def generate_sentiment_analysis(critica: str) :
    if len(critica) > 20000:
        raise HTTPException(status_code=400, detail="El texto debe tener menos de 5000 caracteres.")
    elif len(critica) < 400:
        raise HTTPException(status_code=400, detail="El texto debe tener al menos de 400 caracteres.")
    else:
        analisis_sentimiento = analizar_pelicula(critica)

        dict_temp={
            'sentimiento': analisis_sentimiento['sentimiento'],
            'label_sentimiento': analisis_sentimiento['label_sentimiento'],
            'tiempo_ejecucion': analisis_sentimiento['tiempo_ejecucion'],
            'fecha': [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
        }

        list_sentiment.append(dict_temp)
    return analisis_sentimiento

@app.post("/analysis")
def generate_spacy_analysis(critica: str):
    if len(critica) > 20000:
        raise HTTPException(status_code=400, detail="El texto debe tener menos de 5000 caracteres.")
    elif len(critica) < 400:
        raise HTTPException(status_code=400, detail="El texto debe tener al menos de 400 caracteres.")
    else:
        analisis_sentimiento = analizar_pelicula(critica)
        analysis = spacy_analysis(critica)
        #frases_clave = extraccion_frases_clave(critica)

    return {"analisis_sentimiento": analisis_sentimiento, "analisis_spacy": analysis}
@app.get("/reporte csv", response_class=Response, responses={200: {"content": {"text/csv": {}}}})
def generate_reports():
    if not list_sentiment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No se pudo generar el reporte"
        )

    csv_file_path = "reporteSentiment.csv"

    with open(csv_file_path, mode="w", newline="") as csv_file:
        fieldnames = list_sentiment[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(list_sentiment)

    return FileResponse(csv_file_path, filename="reporteSentiment.csv", media_type="text/csv")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", reload=True)
