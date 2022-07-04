import pandas as pd
from skforecast.ForecasterAutoreg import ForecasterAutoreg
from sklearn.ensemble import RandomForestRegressor


def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    datos = pd.read_csv('data_lake/business/features/precios_diarios.csv', decimal=',')
    
    datos_modelo = datos.drop(['fecha_pronostico', 'precio_pronostico'], axis=1)
    datos_modelo['fecha'] = pd.to_datetime(datos_modelo['fecha'], format='%Y/%m/%d')
    
    datos_modelo= datos_modelo.set_axis(['x','y'], axis=1)
    datos_modelo = datos_modelo.set_index('x')
    datos_modelo = datos_modelo.asfreq('D')
    datos_modelo = datos_modelo['y']
    
    steps=365 
    datos_train = datos_modelo[:-steps]
    datos_test  = datos_modelo[-steps:]
    
    forecaster_rf = ForecasterAutoreg(
                    regressor=RandomForestRegressor(random_state=123),
                    lags=365 #pronostico con datos historicos un año del ultimo dato descargado. 
                )
    
    forecaster_rf.fit(y=datos_train) #entrenamiento
    
    import joblib as jb
    jb.dump(forecaster_rf,'src/models/precios-diarios.pkl')
    
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    train_daily_model()
    import doctest

    doctest.testmod()
