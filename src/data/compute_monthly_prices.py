"""
Modulo computar promedio precios por mes-año.

----------------------------------------------

"""

import pandas as pd
import datetime as dt

def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    
    
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv',sep=',',thousands=None, decimal=',', header=0)
    
    df['fecha']=pd.to_datetime(df['fecha'], format="%Y/%m")
    
    df['fecha']=df['fecha'].dt.strftime('%Y-%m')
    promedio_precios_mes=df.groupby('fecha')['precio'].mean()
    
    promedio_precios_mes.to_csv('data_lake/business/precios-mensuales.csv', index=True, decimal=',')
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    compute_monthly_prices()
    
    import doctest

    doctest.testmod()
