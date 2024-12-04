# Memoria Técnica

## Portada
- **Nombre del Proyecto**: Clasificación de Estilos Arquitectónicos 
- **Fecha**: 4 de diciembre de 2024.
- **Integrante**:  
  - Sebastian García Rodríguez

## Índice
- [Portada](#portada)
- [Alcance del proyecto](#alcance-del-proyecto)
  - [Objetivo](#objetivo)
  - [Introducción](#introducción)
- [Fuentes de información y procedimientos aplicados](#fuentes-de-información-y-procedimientos-aplicados)
  - [Construcción del modelo](#construcción-del-modelo)
  - [Resultados modelo](#resultados-modelo)
  - [Pruebas sobre el modelo](#pruebas-sobre-el-modelo)
  - [Conclusiones](#conclusiones)
- [Conclusiones generales](#conclusiones-generales)
- [Anexos](#anexos)
- [Glosario](#glosario)

## Alcance del proyecto

### Objetivo
El objetivo de este proyecto es desarrollar un modelo de clasificación de imágenes que pueda identificar y categorizar con precisión 10 estilos arquitectónicos seleccionados a partir de un conjunto de datos de imágenes.

### Introducción

## Fuentes de información y procedimientos aplicados

Este proyecto utiliza un conjunto de datos compuesto por imágenes de 10 estilos arquitectónicos diferentes. Este conjunto de datos proviene de dos fuentes principales:
1. Imágenes extraídas de Google Images (g-images): Estas imágenes fueron recopiladas específicamente para este proyecto con el objetivo de cubrir una amplia gama de estilos arquitectónicos.
2. Conjunto de datos del artículo “Architectural Style Classification using Multinomial Latent Logistic Regression” (ECCV 2014): Este conjunto de datos fue creado por Zhe Xu y está disponible en Kaggle. El artículo original incluye 25 estilos arquitectónicos, pero en este proyecto solo se utilizan 10 clases específicas para la tarea de clasificación.

Las 10 clases seleccionadas son las siguientes:
	•	Ancient Egyptian architecture: 406 imágenes
	•	American Foursquare architecture: 362 imágenes
	•	Baroque architecture: 456 imágenes
	•	Byzantine architecture: 313 imágenes
	•	Colonial architecture: 480 imágenes
	•	Deconstructivism: 335 imágenes
	•	Gothic architecture: 331 imágenes
	•	Novelty architecture: 382 imágenes
	•	Postmodern architecture: 322 imágenes
	•	Russian Revival architecture: 352 imágenes


### Observaciones:




## Pipeline de Preparación

### 1. Descarga del Conjunto de datos

El conjunto de datos fue descargado desde Kaggle utilizando el comando:

kagglehub.dataset_download('dumitrux/architectural-styles-dataset')

### 2. Definición de Directorios y Categorías

El directorio principal del conjunto de datos se encuentra en la siguiente ubicación:

dataset_dir = '/root/.cache/kagglehub/datasets/dumitrux/architectural-styles-dataset/versions/3/architectural-styles-dataset'

Las categorías específicas seleccionadas para la clasificación de estilos arquitectónicos son:

categories = [
    'American Foursquare architecture', 'Ancient Egyptian architecture',
    'Baroque architecture', 'Byzantine architecture', 'Colonial architecture',
    'Deconstructivism', 'Gothic architecture', 'Novelty architecture',
    'Postmodern architecture', 'Russian Revival architecture'
]

### 3. Creación de Directorios de Datos y División de Imágenes

El directorio data se crea y se dividen las imágenes en tres particiones: entrenamiento, validación y prueba. El proceso incluye:
* División de Datos: Los datos se dividen en 80% para entrenamiento, 15% para validación y 5% para prueba. Esto se realiza utilizando train_test_split de Scikit-learn.
* Organización de Directorios: Se crean subdirectorios para cada partición de datos y cada categoría, y las imágenes se mueven a los directorios correspondientes.

### 4. Distribución de Imágenes
El conjunto de datos final consta de las siguientes cantidades de imágenes en cada partición:
* Conjunto de Entrenamiento: 3,174 imágenes distribuidas entre las 10 clases.
* Conjunto de Validación: 475 imágenes distribuidas entre las 10 clases.
* Conjunto de Prueba: 90 imágenes distribuidas entre las 10 clases.


## Construcción del modelo

### Aquitectura

### Funcionamiento del Modelo

### Justificación 

## Resultados modelo

### **Precisión (Accuracy)**:

### **Pérdida (Loss)**:
 

## Pruebas sobre el modelo

### **Matriz de Confusión**

## **Métricas de Evaluación**

### **1. Precisión (Precision)**

### **2. Recall (Sensibilidad)**

### **3. F1-Score**

## Conclusiones

## Conclusiones generales

## Anexos
- [Repositorio Github](https://github.com/SebastianGR-FC/Clasificacion-de-Estilos-Arquitectonicos)
- [Conjunto de Datos para la Clasificación de Estilos Arquitectónicos en Kaggle](https://www.kaggle.com/datasets/dumitrux/architectural-styles-dataset)
