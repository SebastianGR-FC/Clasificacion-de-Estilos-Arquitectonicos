from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array  # type: ignore

class Classifier:
    def __init__(self, model_path: str):
        # Carga el modelo preentrenado desde el archivo .keras
        self.model = tf.keras.models.load_model(model_path, compile=False)
        
        # Diccionario que mapea las clases de arquitectura con un índice numérico
        self.class_indices = {
            0: 'American Foursquare architecture',
            1: 'Ancient Egyptian architecture',
            2: 'Baroque architecture',
            3: 'Byzantine architecture',
            4: 'Colonial architecture',
            5: 'Deconstructivism',
            6: 'Gothic architecture',
            7: 'Novelty architecture',
            8: 'Postmodern architecture',
            9: 'Russian Revival architecture'
        }

    def preprocess_image(self, image: Image.Image):
        # Redimensionar la imagen para que tenga el tamaño esperado por el modelo (224x224 píxeles)
        image = image.resize((224, 224))
        
        # Convertir la imagen en un arreglo NumPy y normalizar los valores (de 0 a 255 a 0.0 a 1.0)
        image = img_to_array(image) / 255.0
        
        # Expandir las dimensiones de la imagen para que tenga el formato correcto
        return np.expand_dims(image, axis=0)

    def predict(self, img_array: np.ndarray):
        # Realizar la predicción con el modelo
        predictions = self.model.predict(img_array)
        
        # Obtener el índice de la clase predicha con la mayor probabilidad
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        
        # Obtener el nombre de la clase a partir del índice
        predicted_class = self.class_indices[predicted_class_index]
        
        # Obtener la probabilidad máxima (la confianza en la predicción)
        confidence = np.max(predictions)

        # Devolver el resultado con la clase y la confianza redondeada a dos decimales
        return {
            "class": predicted_class,  # Nombre de la clase predicha
            "confianza": round(float(confidence), 2)  # Confianza de la predicción
        }