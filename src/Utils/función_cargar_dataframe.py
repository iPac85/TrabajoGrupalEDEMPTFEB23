import os
import cv2
import numpy as np
import pandas as pd

def cargar_dataframe(ruta, nombre_archivo):
    """
    Carga imágenes y sus etiquetas desde una carpeta y las une en un DataFrame.

    Esta función recorre una carpeta especificada por la ruta y el nombre de archivo para cargar imágenes y sus etiquetas. 
    Luego, crea un DataFrame con las imágenes y etiquetas correspondientes.

    Args:
        ruta (str): La ruta de la carpeta que contiene las imágenes y etiquetas.
        nombre_archivo (str): El nombre de la carpeta que contiene las imágenes y etiquetas.

    Returns:
        pandas.DataFrame: DataFrame que contiene las imágenes y sus etiquetas.
        numpy.ndarray: Array NumPy con las características (imágenes).
        numpy.ndarray: Array NumPy con las etiquetas.

    Raises:
        FileNotFoundError: Si la ruta o el nombre de archivo no son válidos.

    Example:
        ruta = 'C:\\Users\\Usuario\\Downloads'
        nombre_archivo = 'ImagesV2'
        df, X, y = cargar_dataframe(ruta, nombre_archivo)

    """
    # Combinar la ruta y el nombre de archivo para obtener la ruta completa
    ruta_completa = os.path.join(ruta, nombre_archivo)

    # Listas para almacenar las imágenes y etiquetas
    X = []
    y = []

    # Recorrer las subcarpetas de la carpeta principal
    for folder in os.listdir(ruta_completa):
        # Obtener la etiqueta de la subcarpeta
        label = str(folder)

        # Ruta completa de la subcarpeta
        folder_path = os.path.join(ruta_completa, folder)

        # Iterar sobre los archivos dentro de la subcarpeta
        for file in os.listdir(folder_path):
            # Ruta completa de la imagen
            image_path = os.path.join(folder_path, file)

            # Leer la imagen en escala de grises (2D array)
            image = cv2.imread(image_path, 0)
            
            # Aplanar la imagen en un vector 1D
            image = image.flatten()

            # Agregar la imagen y la etiqueta a las listas
            X.append(image)
            y.append(label)

    # Crear un DataFrame con las imágenes y etiquetas
    df = pd.DataFrame({'image': X, 'label': y})

    # Convertir las listas en arrays NumPy
    X = np.array(X)
    y = np.array(y)

    return df, X, y