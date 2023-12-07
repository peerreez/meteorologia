import pandas as pd
import matplotlib.pyplot as plt
# Especifica la codificación al leer el archivo CSV y utiliza punto y coma como delimitador
archivo_csv = r"C:\Users\****\meteorologia\IMIDA_dia_2020.csv"
ruta_guardado = r"C:\Users\****\meteorologia\IMIDA_dia_2020_modify.csv"
df = pd.read_csv(archivo_csv, encoding='latin-1', delimiter=';', decimal = ',')

# Imprime los nombres de las columnas
print("COLUMNAS")
print(df.columns)
print("################################################################################")
# Imprime las primeras 5 filas
print("CABEZERA")
print(df.head())
print("################################################################################")

# Imprime todas las temperaturas
print(df["TMAX"])
print("################################################################################")

# Imprime la temperatura media
media_tmax = df["TMAX"].mean()
print(f"La media de TMAX es: {media_tmax}")
print("################################################################################")

# Imprime la desviación estándar de la humedad relativa
desv_estan= df["HRMED"].std()
print(f"La desviacion estandar es: {desv_estan}")
print("################################################################################")

# Crea una nueva columna con la evapotranspiración potencial
df["ETO"] = df["TMED"] * 0.0056 * (df["TMAX"] - df["TMIN"]) * 1000

# Imprime la media de la evapotranspiración potencial
print("Columna con la media de la nueva columna evapotranspiración")
evotranspiracion = df["ETO"].mean()
print(f"La desviacion media de la evapotranspiración es: {evotranspiracion}")
print("################################################################################")

# Crea un gráfico de la temperatura máxima en función de la humedad relativa
df.plot(x="HRMED", y="TMAX")
plt.show()

df.to_csv(ruta_guardado, index=False)
