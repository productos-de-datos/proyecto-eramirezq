"""
Modulo computar promedio precios por día.

----------------------------------------------

"""


import pandas as pd
import pandas._testing as tm

def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional

    """
    
    df = pd.read_csv('data_lake/cleansed/precios-horarios.csv',sep=',',thousands=None, decimal=',', header=0)
    promedio_precios_dia=average_daily_prices(df)
    
    promedio_precios_dia.to_csv('data_lake/business/precios-diarios.csv', index=True, decimal=',')
        
    #raise NotImplementedError("Implementar esta función")
    
    
def average_daily_prices(data):
    
    prom=data.groupby('fecha')['precio'].mean()
    
    return prom


if __name__ == "__main__":
    
    compute_daily_prices()
    
    import doctest

    doctest.testmod()
