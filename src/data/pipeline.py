"""
Modulo pipeline de Luigi

---------------------------------------------------------------------------
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
from luigi import LocalTarget, Task


class ingestData(Task):
    
    def output(self):
        return LocalTarget('data_lake/landing/archivo.txt')
    
    def run(self):
        from ingest_data import ingest_data
        with self.output().open('w'):
            ingest_data()
        
class transformData(Task):
    
    def requires(self):
        return ingestData()
    
    def output(self):
        return LocalTarget('data_lake/raw/archivo.txt')
    
    def run(self):
        from transform_data import transform_data
        with self.output().open('w'):
            transform_data()

class cleanData(Task):
    
    def requires(self):
        return transformData()
    
    def output(self):
        return LocalTarget('data_lake/cleansed/archivo.txt')
    
    def run(self):
        from clean_data import clean_data
        with self.output().open('w'):
            clean_data()
        
class computeDailyPrices(Task):
    
    def requires(self):
        return cleanData()
    
    def output(self):
        return LocalTarget('data_lake/business/archivo.txt')
    
    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open('w'):
            compute_daily_prices()

class computeMonthlyPrices(Task):
    
    def requires(self):
        return computeDailyPrices()
    
    def output(self):
        return LocalTarget('data_lake/business/archivo.txt')
    
    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w'):
            compute_monthly_prices()
        
               
if __name__ == "__main__":
    
    luigi.run(["computeMonthlyPrices", "--local-scheduler"])

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    
    import doctest

    doctest.testmod()
