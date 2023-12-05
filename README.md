# Segundo Parcial
## Serivicio Centrado a la critica de Peliculas 

Nombre: Miguel Molina Flores

Codigo: 56197

### 1. Informacion
El presente servicio busca brindar una funcion en la que el cliente pueda introducir una critica de pelicula en formato texto y se le devuelva el sentimiento del mismo. Junto con algunas caracteristicas extra como la clasificacion de palabras y las entidades importantes.

### 2. Guia
* Ingrese una critica en formato texto a cualquiera de los dos metodos */post*, presione ejecutar y mire los resultados.

### 3. Metodos 
* GET /status : Obtiene el estado del servicio presentado para este proyecto.

* POST /sentiment: Analiza los sentimientos de las criticas y devuelve un rango entre -1 y 1 junto con un Label que indica si es negativa o positiva la critica

* POST /analysis: Presenta una funcion con spaCy para el analisis de la critica, obteniendo la descripcion de cada palabra y las entidades relevantes

* GET /reporte csv: Nos brinda el reporte de las calificaciones obtenidas en el primer POST

4. Link del servicio

        https://segundo-parcial-topicos-ia-lkry4ghe7a-uc.a.run.app/docs