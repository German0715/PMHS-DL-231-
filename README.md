# IDENTIFICACIÓN DE FALSAS ALARMAS DE ARRITMIAS CARDÍACAS EN UNIDADES DE CUIDADOS INTENSIVOS (PMHS-DL-231)



¡Bienvenidos a PMHS-DL-231! 

Este es nuestro trabajo de grado como estudiantes de Ingeniería Electrónica en la Universidad Industrial de Santander (UIS). Este proyecto busca identificar el número de falsas alarmas de arritmias cardiacas, evitando la supresión de alarmas verdaderas en las UCIs. Este modelo está entrenado a partir de la base de datos del PhysioNet/Computing in Cardiology Challenge 2015. Un set de datos con 750 registros. 

# Consideraciones relevantes en relación a los datos: Aspectos esenciales a tener en cuenta

Los datos se encuentran almacenados en dos formatos distintos, específicamente en dos archivos con extensiones .HEA y .MAT por cada registro, totalizando 750 registros. Con el objetivo de optimizar la velocidad de procesamiento y la eficiencia del uso de la memoria RAM en el entorno de Google Colab, se llevó a cabo la conversión de los archivos con extensión .MAT a un formato alternativo, en este caso, .H5. El código correspondiente a este proceso se encuentra disponible en el archivo denominado "CONVERSOR_MAT_TO_H5".

**El conjunto de datos tiene 5 tipos de arritmias :**

* 1: Asistolia(a)
* 2: Bradicardia extrema(b)
* 3: Taquicardia extrema(t)
* 4: Taquicardia Ventricular(v)
* 5: Aleteo/Fibrilación ventricular(f)

Desde el mismo nombre de archivo del registro, se puede inferir cierta información. Ejemplo: "v100s" se puede descomponer en:


*   La primer letra (en este caso la v) significa el tipo de arritmia que es según la lista ya presentada.
*   Los tres números del medio son el número de dato (van desde el 100 hasta el 849).
*   La última letra (en este caso la s) habla de la duración de la señal. Para s(duración de 300s) y para l (duración de 330s).


El proyecto está compuesto por carpetas principales:

<!--START_SECTION:activity-->
1. 🎉 PRO_(PMHS_DL_231): En este Jupyter notebook se encuentra toda la estructura de la metodología propuesta para el desarrollo exitoso del proyecto. En donde se 
2. 📁 Entrenamiento de los Modelos: Un bot general básico con la clase Cliente, que trae funciones de el código 'bot_logic'.
3. 📁 Archivos Adicionales:
<!--END_SECTION:activity-->
