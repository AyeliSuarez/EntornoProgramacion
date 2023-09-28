import pandas as pd


class CSVReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.datos = pd.read_csv(file_path)

    def primeras_lineas(self, n):
        return self.datos.head(n)

    def ultimas_lineas(self, n):
        return self.datos.tail(n)

    def aleatorio_lineas(self, n):
        return self.datos.sample(n)

    @property
    def nombres_columnas(self):
        return self.datos.columns.tolist()

    @property
    def tipos_datos_columnas(self):
        return self.datos.dtypes.tolist()

    @property
    def dimensiones(self):
        return self.datos.shape


csv_reader = CSVReader('archivo.csv')
