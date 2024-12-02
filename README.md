# Desarrollo de un Sistema Integral de Análisis de Datos que Permite Identificar Tempranamente a los Estudiantes en Riesgo de Enfrentar Problemas Académicos o de Abandonar sus Estudios


## Tabla de Contenidos
* [Ubicación Entregables](#ubicación-entregables)
* [Descripción de la solución](#descripción-de-la-solución)
* [Conclusiones](#conclusiones)
* [Requerimientos](#requerimientos)
* [Instalación](#instalación)
* [Autores](#autores)
* [Asociados](#autores)

## Ubicación Entregables

El documento de reporte de resultados se encuentra en el siguiente directorio:

[Ciencia-de-Datos-Aplicada-Proyecto-Final/docs/Primera Entrega Proyecto Final.pdf](https://github.com/Daniel27110/Ciencia-de-Datos-Aplicada-Proyecto-Final/blob/main/docs/Primera%20Entrega%20Proyecto%20Final.pdf) 

En la misma carpeta también se pueden encontrar otros archivos relacionados con la primera entrega del proyecto final, como el mockup del dashboard de analítica y el diccionario de datos realizado.

## Descripción de la solución

Este proyecto aborda la problemática de la deserción estudiantil en instituciones de educación superior, centrándose en la identificación temprana de estudiantes en riesgo de enfrentar problemas académicos o abandonar sus estudios. El objetivo es desarrollar un sistema de análisis de datos que permita detectar señales de alerta temprana y personalizar las intervenciones de apoyo, mejorando así la retención y el rendimiento académico.

El sistema utilizará técnicas avanzadas de analítica y aprendizaje automático para construir un modelo predictivo que identifique a los estudiantes en riesgo. Esto permitirá implementar estrategias de intervención personalizadas, optimizar el uso de los recursos institucionales y fortalecer la toma de decisiones basadas en datos.

## Conclusiones

 * Se encontró una alta correlación entre el promedio del último semestre, semestre cursado y estrato sobre la tasa de deserción de los estudiantes de ENDEPORTE.

 * Se evidenció que los estudiantes residentes en municipios aledaños a Cali tienen una mayor tasa de deserción, posiblemente relacionada con el tiempo de desplazamiento hasta la entidad.

 * Los estudiantes que desertaron mostraron un promedio en su último semestre que se sitúa 0.47 desviaciones estándar por debajo del promedio general de todos los estudiantes. Asimismo, se observó que la mayor tasa de deserción ocurre durante los primeros tres semestres, lo que podría atribuirse a la dificultad de las materias de ciencias básicas que se cursan en ese periodo.

 * Con el análisis realizado, se evidencia que los estratos 2 y 3 presentan una tasa de deserción significativamente mayor, lo que sugiere la necesidad de implementar estrategias de apoyo específicas para estos grupos.

 

### Validación Estadística: 

* Se comprobó la significancia estadística de todas las conclusiones para las cuales se pudo realizar una prueba, con un p-value menor al 0.05.​ 

* En efecto, todas las conclusiones para las cuales fue posible llevar a cabo una prueba resultaron estadísticamente significativas. 

 

### Acciones próximas: 

* Compartir los hallazgos con la entidad, con el fin de ser orientados en el refinamiento del modelo. 

* Complementar el conocimiento que tiene la entidad sobre la problemática de deserción y así apoyar la toma de decisiones al respecto.​ 

* Experimentar diferentes técnicas de modelado estadístico que permitan identificar el modelo que mejor se ajuste al contexto de los datos y la naturaleza del problema a solucionar. 

## Requerimientos

### Librerías Empleadas
A continuación se detallan las librerías utilizadas en el proyecto, junto con sus respectivas versiones. Estas son esenciales para el correcto funcionamiento de la solución:

- `pandas==2.2.3`: Manejo de estructuras de datos y análisis.
- `seaborn==0.13.2`: Visualización de datos basada en Matplotlib.
- `matplotlib==3.9.2`: Generación de gráficos y visualizaciones.
- `scipy==1.14.1`: Operaciones avanzadas de cálculo científico y matemático.
- `numpy==2.1.2`: Soporte para operaciones con arreglos multidimensionales y matemáticas de alto nivel.
- `scikit-learn==1.5.2`: Herramientas de machine learning y análisis predictivo.
- `uvicorn`
- `fastapi`
- `joblib`
- `python-multipart`
- `imblearn`
- `plotly`
- `smote`
- `Markdown`

### Requerimientos Hardware
Para ejecutar el proyecto en un entorno óptimo, se recomienda el siguiente hardware mínimo:

- Procesador: Intel i5 o superior.
- Memoria RAM: 8 GB (recomendado 16 GB para grandes volúmenes de datos).
- Almacenamiento: Al menos 500 MB de espacio libre para las dependencias del proyecto y los datos.
- Tarjeta gráfica: No es necesaria, pero una GPU puede acelerar procesos de visualización o análisis grandes.

### Requerimientos Software
El software necesario para ejecutar el proyecto incluye:

- **Sistema Operativo**: Compatible con Windows 10, macOS 10.15 o distribuciones de Linux.
- **Python**: Versiones >= 3.9. Se recomienda utilizar un entorno virtual para evitar conflictos de dependencias.
- **Librerías**: Las mencionadas anteriormente. Asegúrese de instalar todas las dependencias utilizando el archivo `requirements.txt` proporcionado.

## Instalación

### Paso a paso para la instalación en Python:

1. **Clonar el repositorio**:
   Primero, asegúrese de tener `git` instalado en su máquina. Luego, clone el repositorio en su entorno local:
   ```bash
   git clone https://gitlab.com/CAOBA-Central/pruebas-concepto/uniandes/pruebas-concepto-g5-c9/poc-082-endeporte-deteccion-riesgos-academicos-fase1.git
   ```
   Cambie al directorio del proyecto:
   ```bash
   cd poc-082-endeporte-deteccion-riesgos-academicos-fase1
   ```

2. **Crear un entorno virtual** (opcional pero recomendado):
   Crear un entorno virtual para aislar las dependencias del proyecto:
   ```bash
   python -m venv env
   ```
   Luego, activar el entorno:
   - En Windows:
     ```bash
     .\env\Scripts\Activate.ps1
     ```
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```

3. **Instalar las dependencias** desde el archivo `requirements.txt`:
   Una vez que el entorno virtual esté activado, ejecute el siguiente comando para instalar todas las librerías necesarias:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verificar la instalación**:
   Tras la instalación, puede verificar que todas las librerías se instalaron correctamente ejecutando:
   ```bash
   pip freeze
   ```


## Despliegue

1. Instalar un ambiente virtual
   ```python
   pip install virtualenv
   ```

2. Crear un entorno virtual:
   ```bash
   python -m venv env
   ```

3. Activar el entorno:
   - En Windows:
     ```bash
     .\env\Scripts\Activate.ps1
     ```
   - En macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. Instalar las dependencias
   ```bash
   pip install -r requirements.txt
   ```

5. Posteriormente, ingresar a la carpeta `deploy` y activar el servidor:
   ```bash
   uvicorn main:app --reload
   ```

6. Una vez el servidor presente el mensaje de inicio correcto, similar al siguiente:
   ```
   INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
   INFO:     Started reloader process [15952] using StatReload
   INFO:     Started server process [10220]
   INFO:     Waiting for application startup.
   INFO:     Application startup complete.
   ```
7. Luego de evidenciar el servidor en ejecución, se debe ingresar a un navegador e ingresar a la siguiente URL: http://127.0.0.1:8000/inicio , donde se carga una interfaz para diligenciar la información.
   - Si se requiere consumir el modelo por un servicio REST, se puede probar el servicio con una herramienta como Postman, enviando:
```
   POST /predict HTTP/1.1
   Host: 127.0.0.1:8000
   Content-Type: application/json
   [
      {
         "ESTRATO": 1,
         "SEMESTRE": 1,
         "PROMEDIOSEMESTRE": 3.8,
         "EDAD2": 18,
         "PROGRAMA": 53212,
         "GENERO": 1,
         "CIUDADRESIDENCIA": 76001,
         "CIUDADNACIMIENTO": 76001
      }
   ]
```

Los valores de:
- **PROGRAMA** corresponden a los códigos presentes en el archivo ubicado en `data/raw/programas.csv`
- **CIUDADRESIDENCIA** el código corresponde al `Codigo_Municipio` presente en el archivo de **DIVIPOLA** ubicado en `data/raw/DIVIPOLA-_C_digos_municipios_20241127.csv`
- **CIUDADNACIMIENTO** el código corresponde al `Codigo_Municipio` presente en el archivo de **DIVIPOLA** ubicado en `data/raw/DIVIPOLA-_C_digos_municipios_20241127.csv`

**NOTA** En caso de requerir realizar predicciones grupales, se deberá completar la estructura del archivo ubicado en la ruta `deploy/estudiantes.csv` con los datos correspondientes. Una vez diligenciado el archivo, deberá cargarse en la sección de la interfaz gráfica denominada *"Predicción Grupal"*, seleccionando el archivo *estudiantes.csv* previamente completado, para obtener las predicciones individuales de cada estudiante registrado en dicho archivo.

## Proceso de reentrenamiento del modelo

Para ingresar nueva información y entrenar el modelo con esta, se debe:
1. La fuente debe ser en formato *csv*, comprimida en `gz` y tener la misma cantidad de columnas y nombres como la fuente denominada `Demograficos.csv.gz` que se encuentra en `data/raw`.
2. Si existen programas nuevos en la Institución y se desea incluir en la predicción, se debe agregar al archivo denominado `programas.csv` ubicado en la ruta `data/raw/` manteniendo los tipos de datos y estructura definida.
> **NOTA** No eliminar registros existentes en el archivo `programas.csv` a menos que el programa ya no exista o no se quiera incluir en el modelo; lo anterior dado que el modelo toma este insumo y con ello hace los cruces respectivos de valores.
3. Una vez se han realizado los anteriores pasos, se procede a ejecutar los notebooks ubicados en la ruta `data/analytics` en el siguiente orden:
   1. `preparacion_de_datos.ipynb`: notebook que ajusta los datos y genera el archivo de salida para el modelo en la ruta `data/stage/clean.csv`
   2. `seleccion_de_modelo.ipynb`: noteboook para visualizar valores estadísticos del archivo generado en el notebook anterior.
   3. `modelo.ipynb`: notebook que ejecuta el modelo y genera el archivo compilado `deploy/rf_model.joblib` para ejecución en el despliegue.

## Instrucciones de Uso

Para realizar la predicción grupal de estudiantes, siga estos pasos una vez haya desplegado la herramienta web en **http://127.0.0.1:8000/inicio**:

1. **Acceder a la sección 'Predicción Grupal'**: 
   Una vez que la herramienta web esté cargada, diríjase a la sección **"Predicción Grupal"** en la interfaz.

2. **Cargar el archivo de estudiantes**:
   En esta sección, deberá cargar un archivo con los datos de los estudiantes en el formato esperado. Puede utilizar como ejemplo el archivo **`estudiantes.csv`** que se encuentra en el directorio **`deploy`**. Este archivo contiene un conjunto de datos de estudiantes con la estructura correcta para la predicción.

3. **Visualización de predicciones**:
   Después de cargar el archivo, podrá ver la predicción de si cada uno de los estudiantes registrados en el archivo va a desertar o no. Además, se mostrará una caracterización de los estudiantes que tienen mayor probabilidad de desertar.

4. **Análisis detallado de cada estudiante**:
   Si desea un análisis más profundo de un estudiante en particular, puede hacer clic en el listado de estudiantes. Esto le permitirá acceder a un análisis detallado que muestra las razones individuales que podrían llevar a cada uno de esos estudiantes a desertar.

## Autores

| Organización   | Nombre del Miembro | Correo electrónico | 
|----------|-------------|-------------|
| Universidad de los Andes - Bogotá |  Adriana María Rios: Desarrollador(a)/Estudiante  | am.rios2@uniandes.edu.co |
| Universidad de los Andes - Bogotá |  Andrés Francisco Borda Rincón: Desarrollador(a)/Estudiante  | af.borda@uniandes.edu.co |
| Universidad de los Andes - Bogotá  |  Daniel Felipe Vargas Ulloa: Desarrollador(a)/Estudiante  | d.vargasu@uniandes.edu.co |
| Universidad de los Andes - Bogotá  |  Diego Alberto Rodríguez Cruz: Desarrollador(a)/Estudiante  | da.rodriguezc123@uniandes.edu.co |

## Asociados

| Organización   | Nombre del Miembro | Correo electrónico | 
|----------|-------------|-------------|
| PUJ-Bogotá |  Liliana María Pantoja Rojas: Líder proyecto CAOBA | lm_pantoja@javeriana.edu.co |
| Institución Universitaria Escuela Nacional del Deporte |  Andrés Felipe Cárdenas Borrero: Lider del negocio  | andresf.cardenas@endeporte.edu.co |
