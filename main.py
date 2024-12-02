from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
from models.classifier import Classifier

app = FastAPI()

# Permitir solicitudes desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes, cambia esto si necesitas restringirlo a tu sitio web
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos de solicitud
    allow_headers=["*"],  # Permitir todos los tipos de encabezados
)

# Montar archivos estáticos (como imágenes y archivos CSS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Cargar el modelo de predicción de imágenes
classifier = Classifier("model.keras")

# Ruta para proporcionar el archivo HTML
@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        # Intentar abrir el archivo index.html
        with open("/static/index.html", "r") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        # Si no se encuentra el archivo, devolver un error 404
        raise HTTPException(status_code=404, detail="index.html no encontrado")

# Ruta para hacer predicciones con una imagen cargada
@app.post("/predict/")
async def predecir(file: UploadFile = File(...)):
    try:
        # Leer la imagen cargada por el usuario
        image_bytes = await file.read()

        try:
            # Intentar abrir la imagen con PIL
            image = Image.open(BytesIO(image_bytes))
        except Exception:
            # Si no se puede abrir la imagen, devolver un error 400
            raise HTTPException(status_code=400, detail="No se pudo abrir la imagen.")

        # Preprocesar la imagen para que el modelo pueda hacer la predicción
        img_array = classifier.preprocess_image(image)

        # Realizar la predicción con el modelo
        resultado = classifier.predict(img_array)

        # Devolver el resultado con el estilo predicho y la confianza
        return JSONResponse(content={
            "clase": resultado["class"],  # Nombre del estilo arquitectónico predicho
            "confianza": resultado["confianza"]  # Confianza de la predicción
        })

    except Exception as e:
        # Si ocurre algún error en el servidor, devolver un mensaje de error
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")