"""
Modulo transformacion de los datos.
--------------------------------------------------------------------------------------------
Transorma archivos .xls y .xlsx en carpeta data_lake/landing, a .csv y los almacena en carpeta data_lake/raw

"""

import os
import pandas as pd

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    
    
    
    dir = "data_lake/landing"
    for path in os.listdir(dir):
            
        extension=os.path.splitext(path)[1]
            
        if extension == '.xlsx':
            df=pd.read_excel(f'data_lake/landing/{path}', engine='openpyxl')
        else:
            if extension == '.xls':
                df=pd.read_excel(f'data_lake/landing/{path}', engine='xlrd')
                
        Cabecera=df.index[(df.iloc[:,0] == 'Fecha')].tolist()
            
        if bool(Cabecera) == True:
            Cabecera=int(Cabecera[0])+1
        else:
            Cabecera=0
                
        if extension == '.xlsx':    
            df = pd.read_excel(f'data_lake/landing/{path}', header=Cabecera, engine='openpyxl')
        else:
            if extension == '.xls':
                df = pd.read_excel(f'data_lake/landing/{path}', header=Cabecera, engine='xlrd') 
               
        file_name = os.path.splitext(path)[0]
        df.to_csv(f'data_lake/raw/{file_name}.csv', sep=',', index=False, decimal=',')
       
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    transform_data()
    
    import doctest

    doctest.testmod()
