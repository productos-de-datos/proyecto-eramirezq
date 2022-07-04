
def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import os
    import pandas as pd
    import xlwt 
    
    dir = "data_lake/landing"
    for path in os.listdir(dir):
            
            extension=os.path.splitext(path)[1]
            
            if extension == '.xlsx':
                df=pd.read_excel(f'data_lake/landing/{path}', engine='openpyxl')
            else:
                df=pd.read_excel(f'data_lake/landing/{path}')
                
            Header=df.index[(df.iloc[:,0] == 'Fecha')].tolist()
            
            if bool(Header) == True:
                Header=int(Header[0])+1
            else:
                Header=0
                
            if extension == '.xlsx':    
                df = pd.read_excel(f'data_lake/landing/{path}', header=Header, engine='openpyxl')
            else:
                df = pd.read_excel(f'data_lake/landing/{path}', header=Header) 
               
            file_name = os.path.splitext(path)[0]
            df.to_csv(f'data_lake/raw/{file_name}.csv', sep=',', index=False, decimal=',')
       
    
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    
    transform_data()
    
    import doctest

    doctest.testmod()
