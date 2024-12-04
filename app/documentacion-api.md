
# Documentación General de la API

## Tabla de Contenidos
1. [Introducción](#introducción)
2. [Requisitos Previos](#requisitos-previos)
3. [Instalación](#instalación)
   - [Clonación del Repositorio](#clonación-del-repositorio)
   - [Configuración del Entorno](#configuración-del-entorno)
4. [Uso de Docker](#uso-de-docker)
   - [Construcción de la Imagen](#construcción-de-la-imagen)
   - [Ejecución del Contenedor](#ejecución-del-contenedor)
   - [Detener y Eliminar Contenedores](#detener-y-eliminar-contenedores)
5. [Endpoints de la API](#endpoints-de-la-api)
   - [POST /clasification_image](#post-clasification_image)
6. [Manejo de Errores](#manejo-de-errores)

---

## Introducción
Esta API permite la clasificación de imágenes de estilos arquitectónicos usando un modelo preentrenado basado en redes neuronales. La API proporciona un endpoint para cargar una imagen y obtener la predicción del estilo arquitectónico en el que se clasifica.

El modelo puede identificar 10 estilos arquitectónicos diferentes y devolver la clase predicha junto con el nivel de confianza en la predicción.

## Requisitos Previos
- Docker y Docker Compose instalados.
- Git instalado.
- Python 3.10 o superior (para desarrollo).
- Configuración básica del sistema operativo.

## Instalación

### Clonación del Repositorio
Clona el repositorio del proyecto:
```bash
git clone https://github.com/SebastianGR-FC/Clasificacion-de-Estilos-Arquitectonicos.git
cd Clasificacion-de-Estilos-Arquitectonicos
```
## Carga del modelo

El archivo de modelo necesario para ejecutar la API es bastante pesado y no está incluido directamente en el repositorio. Puedes descargarlo desde el siguiente enlace:
 
[Descargar modelo image_classifier_model.keras](https://drive.google.com/file/d/1dDQc0MbJ7ISSx5R4_XZDaKuU0P8YSR7M/view?usp=sharing)

Por favor, guarda el modelo image_classifier_model.keras dentro del folder Clasificacion-de-Estilos-Arquitectonicos
 
## Uso de Docker

### Construcción de la Imagen
Construye la imagen de Docker:
```bash
docker build -t clasificador-api .
```

### Ejecución del Contenedor
Inicia el contenedor con Docker:
```bash
docker run -d -p 8000:8000 clasificador-api
```
Accede a la API en `http://localhost:8000/docs` para la documentación interactiva.

### Detener y Eliminar Contenedores
Para detener un contenedor:
```bash
docker stop id_contenedor
```
Para eliminarlo:
```bash
docker rm id_contenedor
```

---

## Endpoints de la API

La API está disponible en http://127.0.0.1:8000 o http://localhost:8000 de forma local.

### POST /predict
**Descripción:** Este endpoint recibe una imagen y devuelve el estilo arquitectónico clasificado junto con el nivel de confianza de la predicción.

**Request Body:**
- `file`: La imagen que se desea clasificar. Debe ser un archivo de imagen válido (JPEG, PNG, etc.).

**Ejemplo:**
```bash
curl -X POST -F "file=@ruta/a/tu/imagen.jpg" http://127.0.0.1:8000/predict/
```

**Response:**
```json
{
  "clase": "Gothic architecture",
  "confianza": 0.92
}
```

---

## Manejo de Errores
La API devuelve respuestas HTTP con códigos de error estándar:
- **400**: No se pudo abrir la imagen.
- **404**: index.html no encontrado.
- **500**: Error interno del servidor.

## Observaciones

- Los modelos deben estar entrenados y disponibles en el directorio `Clasificacion-de-Estilos-Arquitectonicos`.
