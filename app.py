# main.py
import pandas as pd
import matplotlib.pyplot as plt
from rich.console import Console

# Tu lógica de la aplicación aquíwowowo

def main():
    # Ejemplo: Crear un DataFrame con pandas
    data = {'Nombre': ['Alice', 'Bob', 'Charlie'],
            'Edad': [25, 30, 35],
            'Puntuación': [85, 90, 88]}

    df = pd.DataFrame(data)

    # Mostrar DataFrame con rich
    console = Console()
    console.print("[bold]Datos del DataFrame:[/bold]")
    console.print(df)

    # Ejemplo: Crear un gráfico con matplotlib
    plt.bar(df['Nombre'], df['Puntuación'])
    plt.xlabel('Nombre')
    plt.ylabel('Puntuación')
    plt.title('Puntuación por Nombre')
    plt.show()

if __name__ == "__main__":
    main()
