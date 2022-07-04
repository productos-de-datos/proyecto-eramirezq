"""
Modulo realizar pronostico importando el modelo entrenado generado en train_daily_model

------------------------------------------------------------------------------------------------------
Se pronostica a patir del año 2019.
"""

import pandas as pd
import joblib as jb
def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    modelo=jb.load('src/models/precios-diarios.pkl')
    
    datos = pd.read_csv('data_lake/business/precios-diarios.csv', decimal=',')
    datos_salida=datos
    datos['fecha'] = pd.to_datetime(datos['fecha'], format='%Y/%m/%d')
    
    datos= datos.set_axis(['x','y'], axis=1)
    datos = datos.set_index('x')
    datos = datos.asfreq('D')
    datos = datos['y']
    
    steps=365
    datos_test  = datos[-steps:]
    
    steps=365
    predicciones = modelo.predict(steps=steps)
    predicciones = pd.Series(data=predicciones, index=datos_test.index)
    
    datos_salida['fecha'] = pd.to_datetime(datos_salida['fecha'], format='%Y/%m/%d')
    predicciones = predicciones.rename_axis('fecha').reset_index()
    predicciones= predicciones.set_axis(['fecha','precio_prom_pron'], axis=1)
    predicciones['fecha']=pd.to_datetime(predicciones['fecha'], format='%Y/%m/%d')
    
    salida=datos_salida.merge(predicciones, on='fecha',how='left')
    
    salida.to_csv('data_lake/business/forecasts/precios-diarios.csv', index=False, decimal=',')

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    make_forecasts()
    import doctest

    doctest.testmod()
