"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------
Función para descargar archivos .xls y .xlsx de repo github

"""

import requests
def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """

    for num in range(1995,2022):
        if num in range(2016,2018):
            url_descarga = 'https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/precio_bolsa_nacional/xls/{}.xls'.format(num)
        else:
            url_descarga = 'https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/precio_bolsa_nacional/xls/{}.xlsx'.format(num)
        
        nombre_archivo = url_descarga.rsplit('/', 1)[1]
        
        with open('data_lake/landing/' + nombre_archivo, 'wb') as file:
            file.write(requests.get(url_descarga).content)
        
    #raise NotImplementedError("Implementar esta función")
    
if __name__ == "__main__":
    
    ingest_data()
    
    import doctest

    doctest.testmod()
