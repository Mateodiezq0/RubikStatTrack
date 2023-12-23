import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Nombre': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Edad': [25, 30, 22, 35, 28],
        'Puntuacion': [85, 92, 78, 95, 89]}

df = pd.DataFrame(data)

# Imprimir el DataFrame
print("DataFrame Original:")
print(df)

# Filtrar personas mayores de 30 años
mayores_de_30 = df[df['Edad'] > 30]
print("\nPersonas mayores de 30:")
print(mayores_de_30)

# Calcular la puntuación promedio
puntuacion_promedio = df['Puntuacion'].mean()
print(f"\nPuntuación promedio: {puntuacion_promedio:.2f}")

# Guardar el DataFrame en un archivo CSV
df.to_csv('datos.csv', index=False)

# Cargar datos desde el archivo CSV
df_cargado = pd.read_csv('datos.csv')
print("\nDataFrame cargado desde CSV:")
print(df_cargado)
