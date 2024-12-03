from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
from app.models.classifier import Classifier

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Montar archivos del frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Cargar el modelo
classifier = Classifier("model.keras")

# Mostrar index.html
@app.get("/", response_class=HTMLResponse)
async def index():
    try:
        # Abrir de forma segura el contenido de index.html
        with open("frontend/index.html", "r") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="index.html no encontrado")

# Ruta de predicción
@app.post("/predict/")
async def predecir(file: UploadFile = File(...)):
    try:
        # Leer la imagen subida
        image_bytes = await file.read()

        try:
            # Abrir la imagen usando PIL
            image = Image.open(BytesIO(image_bytes))
        except Exception:
            raise HTTPException(status_code=400, detail="No se pudo abrir la imagen.")

        # Preprocesar la imagen
        img_array = classifier.preprocess_image(image)

        # Obtener el resultado de la predicción
        resultado = classifier.predict(img_array)

        # Devolver los resultados de la predicción
        return JSONResponse(content={
            "clase": resultado["clase"],
            "confianza": resultado["confianza"]
        })

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")