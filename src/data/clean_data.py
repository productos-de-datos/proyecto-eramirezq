"""
Modulo limpieza de datos
---------------------------------------------------------------------------------
Realiza limipieza de datos; agrupa los archivos .csv ubicados en data_lake/raw

Borra las filas totalmente nulas. 
Agrupa en tres columnas: Fecha, hora y precio; ordenados por fecha y hora
Elimina las fechas duplicadas
Elimina filas de precios con valor nulo. 

"""

import pandas as pd
import os
import numpy as np
import pandas._testing as tm
from pandas import DataFrame

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    
    
    array = np.linspace(0, 23, 24,dtype=int)
    array = array.astype(str)
    
    cols=['Fecha']+list(array)
    
    precios_horarios=pd.DataFrame(columns=cols)
    dir = "data_lake/raw"
    for path in os.listdir(dir):
        
        df = pd.read_csv(f'data_lake/raw/{path}',sep=',',thousands=None, decimal=',', header=0, names=cols, usecols=cols)
        precios_horarios=pd.concat(objs=[precios_horarios,df], ignore_index=True)
            
    
    precios_horarios['Fecha']=pd.to_datetime(precios_horarios['Fecha'], format="%Y/%m/%d")
    precios_horarios=precios_horarios.dropna(how='all')
    lista_datos = transponer(precios_horarios)
    lista_datos=lista_datos.set_axis(['fecha','hora','precio'], axis=1)
    lista_datos['hora']=lista_datos['hora'].astype(int)
    lista_datos['precio']=pd.to_numeric(lista_datos['precio'],downcast='float')
    lista_datos=lista_datos.sort_values(by=['fecha','hora'])
    lista_datos.drop_duplicates(inplace=True)
    lista_datos=lista_datos[lista_datos['precio'].notna()]
    lista_datos.to_csv(f'data_lake/cleansed/precios-horarios.csv', index=False, decimal=',')
    
    #raise NotImplementedError("Implementar esta función")
    
def transponer(data):
    resultado=pd.melt(data, id_vars=['Fecha'])
    return resultado

def test_trasponer():
    datos = {
    'Fecha' : ['1995-07-20', '1995-07-21', '1995-07-22', '1995-07-23'],
    '0': [5, 12, 3, 15],
    '3': [6, 8, 9, 17],
    '4': [7, 8, 7, 1],
    '2': [8, 7, 13, 5],
    '1': [10, 56, 14, 6],
    }
    df1 = pd.DataFrame(datos)
    result=transponer(df1)
    expected = DataFrame(
            {
                "Fecha": ['1995-07-20','1995-07-21','1995-07-22','1995-07-23','1995-07-20','1995-07-21','1995-07-22','1995-07-23','1995-07-20','1995-07-21','1995-07-22','1995-07-23','1995-07-20','1995-07-21','1995-07-22','1995-07-23','1995-07-20','1995-07-21','1995-07-22','1995-07-23'],
                "variable": ['0', '0', '0', '0', '3', '3', '3', '3', '4', '4', '4', '4', '2', '2', '2', '2', '1', '1', '1', '1'],
                "value": [5, 12, 3, 15, 6, 8, 9, 17, 7, 8, 7, 1, 8, 7, 13, 5, 10, 56, 14, 6],
                
            },

        )
    tm.assert_frame_equal(result, expected)

if __name__ == "__main__":
    
    clean_data()
    import doctest
    
    doctest.testmod()
