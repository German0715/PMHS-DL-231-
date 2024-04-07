import scipy.io
import h5py
import os

def convertir_mat_a_h5(ruta_entrada, ruta_salida):
    # Carga el archivo .mat
    mat_file = scipy.io.loadmat(ruta_entrada)

    # Crea un archivo HDF5 en la ruta de salida
    with h5py.File(ruta_salida, 'w') as h5_file:
        # Itera sobre las variables en el archivo .mat y guárdalas en el archivo .h5
        for key in mat_file:
            h5_file.create_dataset(key, data=mat_file[key])

# Rutas de entrada y salida
ruta_directorio_entrada = 'MAT_data'
ruta_directorio_salida = 'H5_data'

# Iterar sobre los archivos en el directorio de entrada
for nombre_archivo in os.listdir(ruta_directorio_entrada):
    if nombre_archivo.endswith('.mat'):
        ruta_entrada = os.path.join(ruta_directorio_entrada, nombre_archivo)
        nombre_salida = nombre_archivo.replace('.mat', '.h5')
        ruta_salida = os.path.join(ruta_directorio_salida, nombre_salida)

        convertir_mat_a_h5(ruta_entrada, ruta_salida)
