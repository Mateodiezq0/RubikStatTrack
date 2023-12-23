# main.py
import pandas as pd
import time
from rich.console import Console
import sys

class Timer:
    def __init__(self):
        self.times_df = pd.DataFrame(columns=['Time'])

    def start_timer(self):
        self.start_time = time.time()

    def stop_timer(self):
        new_time = time.time() - self.start_time
        self.times_df = self.times_df.append({'Time': new_time}, ignore_index=True)

    def get_times(self):
        return self.times_df

    def save_times_to_csv(self, filename):
        self.times_df.to_csv(filename, index=False)

    def load_times_from_csv(self, filename):
        self.times_df = pd.read_csv(filename)

class PerformanceAnalyzer:
    def __init__(self, times_df):
        self.times_df = times_df

    def calculate_average_time(self):
        return self.times_df['Time'].mean()

    def generate_histogram(self):
        # Utiliza funciones de Pandas o matplotlib para generar un histograma de tiempos
        pass

class SpeedCubingApp:
    def __init__(self):
        self.timer = Timer()
        self.performance_analyzer = PerformanceAnalyzer(self.timer.get_times())

    def run(self):
        console = Console()
        console.print("¡Bienvenido a SpeedCubingApp!", style="bold green")

        while True:
            input("Presiona Enter para comenzar el cronómetro...")
            self.timer.start_timer()

            # Lógica para ejecutar el speedcubing 
            sys.stdin.read(1)

            self.timer.stop_timer()
            console.print(f"Tiempo registrado: {self.timer.get_times()['Time'].iloc[-1]:.2f} segundos", style="bold blue")

            response = input("¿Quieres continuar (s/n)? ").lower()
            if response != 's':
                break

        average_time = self.performance_analyzer.calculate_average_time()
        console.print(f"Tiempo promedio: {average_time:.2f} segundos", style="bold magenta")
        self.performance_analyzer.generate_histogram()

if __name__ == "__main__":
    app = SpeedCubingApp()
    app.run()
