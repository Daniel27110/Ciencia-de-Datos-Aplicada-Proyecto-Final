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
   git clone https://github.com/usuario/nombre-del-repositorio.git
   ```
   Cambie al directorio del proyecto:
   ```bash
   cd nombre-del-repositorio
   ```

2. **Crear un entorno virtual** (opcional pero recomendado):
   Crear un entorno virtual para aislar las dependencias del proyecto:
   ```bash
   python -m venv env
   ```
   Luego, activar el entorno:
   - En Windows:
     ```bash
     .\env\Scripts\activate
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

4. **Ejecutar los archivos de exploración**:

   Para esta primera entrega, los archivos de exploración de datos se encuentran en el directorio del repositorio:

       Ciencia-de-Datos-Aplicada-Proyecto-Final/analytics/primera entrega/

   En particular, el archivo 'EDA consolidado final.ipynb' contiene los resultados consolidados de nuestro proceso de análisis de datos. 

   Para la entrega final, la ejecución del tablero de control estará disponible en

       Ciencia-de-Datos-Aplicada-Proyecto-Final/analytics/entrega final/


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
