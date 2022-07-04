def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png

    """
    import matplotlib.pyplot as plt
    import pandas as pd
    
    df = pd.read_csv('data_lake/business/precios-mensuales.csv', decimal=',')
    df.fecha = pd.to_datetime(df.fecha, errors='coerce')
    df = df.set_index('fecha')  
    _= df.plot( color='tab:blue', figsize=(17,6), marker='.')
    plt.title('Precio energia promedio mensual ')
    plt.savefig("data_lake/business/reports/figures/monthly_prices.png")
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    make_monthly_prices_plot()
    import doctest

    doctest.testmod()