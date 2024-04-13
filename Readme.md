# Sistema de Recomendación de Películas

Este es un sistema de recomendación de películas desarrollado utilizando Python, Pandas, Streamlit y la técnica de Descomposición de Valores Singulares Truncados (SVD) para analizar patrones de preferencia de usuarios en datos de calificaciones de películas.

## Contenido del Repositorio

- **datos/**: Directorio que contiene los conjuntos de datos utilizados por la aplicación.
  - *movies.csv*: Archivo CSV que contiene información sobre las películas.
  - *ratings.csv*: Archivo CSV que contiene las calificaciones de las películas proporcionadas por los usuarios.
- **app.py**: El archivo principal de la aplicación desarrollada con Streamlit.

## Instrucciones de Uso

1. **Instalación de Dependencias**: Es necesario instalar las bibliotecas requeridas antes de ejecutar la aplicación. Puedes instalarlas ejecutando el siguiente comando:

    ```bash
    pip install pandas streamlit scikit-learn
    ```

2. **Ejecución de la Aplicación**: Una vez instaladas las dependencias, puedes ejecutar la aplicación utilizando el siguiente comando en tu terminal:

    ```bash
    streamlit run app.py
    ```

3. **Interacción con la Aplicación**: Después de ejecutar la aplicación, se abrirá en tu navegador web predeterminado. Podrás seleccionar una película que te guste de la lista desplegable y recibirás recomendaciones de películas similares basadas en correlaciones de las calificaciones de los usuarios.

## Consideraciones Importantes

- Este sistema de recomendación utiliza técnicas de aprendizaje no supervisado para generar recomendaciones basadas en las preferencias de los usuarios.
- Las recomendaciones se basan en la correlación entre las calificaciones de las películas proporcionadas por los usuarios.
- La calidad de las recomendaciones puede variar según la cantidad y calidad de los datos de calificación disponibles.

## Contribuciones y Problemas

Si encuentras algún problema o tienes alguna sugerencia para mejorar esta aplicación, no dudes en abrir un problema en este repositorio. ¡Las contribuciones son bienvenidas!
