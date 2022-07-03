def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import os
    import numpy as np
    
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
    lista_datos = pd.melt(precios_horarios, id_vars=['Fecha'])
    lista_datos=lista_datos.set_axis(['fecha','hora','precio'], axis=1)
    lista_datos['hora']=lista_datos['hora'].astype(int)
    lista_datos['precio']=pd.to_numeric(lista_datos['precio'],downcast='float')
    lista_datos=lista_datos.sort_values(by=['fecha','hora'])
    lista_datos.drop_duplicates(inplace=True)
    lista_datos=lista_datos[lista_datos['precio'].notna()]
    lista_datos.to_csv(f'data_lake/cleansed/precios-horarios.csv', index=False, decimal=',')
    
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    clean_data()
    import doctest
    
    doctest.testmod()
