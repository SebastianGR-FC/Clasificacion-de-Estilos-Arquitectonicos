# ![Logo Facultad de Ciencias](images/logoFC.png) Clasificación de Estilos Arquitectónicos

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![TensorFlow Version](https://img.shields.io/badge/TensorFlow-2.14-orange.svg)](https://www.tensorflow.org/)

## Integrante:
Sebastian García Rodríguez

## Entregables:

1. [Memoria Técnica](dev_model/MEMORIA-TECNICA.md)
2. [Documentación API](app/documentacion-api.md)

## Contexto

La clasificación de estilos arquitectónicos es un campo que aplica técnicas de visión por computadora y aprendizaje automático para identificar y categorizar edificios en función de su estilo arquitectónico. Este enfoque tiene aplicaciones tanto en el análisis histórico como en la preservación del patrimonio arquitectónico.

## Objetivo del Proyecto

El objetivo de este proyecto es desarrollar un modelo de aprendizaje automático que pueda clasificar imágenes de edificios según su estilo arquitectónico. El modelo debe ser capaz de reconocer y diferenciar entre varios estilos arquitectónicos con alta precisión.

## Descripción General del Conjunto de Datos

Este proyecto utiliza un conjunto de datos compuesto por 10,113 imágenes de 25 estilos arquitectónicos diferentes. Este conjunto de datos es una combinación de dos fuentes principales:
	1.	Imágenes extraídas de Google Images (g-images), que fueron recopiladas específicamente para este proyecto.
	2.	Conjunto de datos del artículo “Architectural Style Classification using Multinomial Latent Logistic Regression” (ECCV 2014), realizado por Zhe Xu. Este conjunto de datos está disponible en Kaggle.

La fuente original del conjunto de datos creada por Zhe Xu incluye 25 estilos arquitectónicos, pero en este proyecto solo se utilizaron 10 clases específicas de este conjunto de datos para la clasificación de estilos arquitectónicos.

Las 10 clases utilizadas en este proyecto son:
	1.	Ancient Egyptian architecture: 406 imágenes
	2.	American Foursquare architecture: 362 imágenes
	3.	Baroque architecture: 456 imágenes
	4.	Byzantine architecture: 313 imágenes
	5.	Colonial architecture: 480 imágenes
	6.	Deconstructivism: 335 imágenes
	7.	Gothic architecture: 331 imágenes
	8.	Novelty architecture: 382 imágenes
	9.	Postmodern architecture: 322 imágenes
	10.	Russian Revival architecture: 352 imágenes

En total, el conjunto de datos utilizado para este proyecto abarca 3,739 imágenes de las 10 clases seleccionadas.

## Enlaces Relevantes

- [Conjunto de Datos para la Clasificación de Estilos Arquitectónicos en Kaggle](https://www.kaggle.com/datasets/dumitrux/architectural-styles-dataset)
