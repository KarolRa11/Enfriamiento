import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import ipywidgets as widgets
from scipy.integrate import odeint
from IPython.display import display

# Definir la variable independiente (tiempo)
t = sp.Symbol('t')

# Definir la función dependiente (Temperatura en función del tiempo)
T = sp.Function('T')(t)

# Definir la constante de enfriamiento y la temperatura ambiente
k = sp.Symbol('k', positive=True)
T_env = sp.Symbol('T_env')

# Definir la ecuación diferencial de la Ley de Enfriamiento de Newton
diff_eq = sp.Eq(T.diff(t), -k * (T - T_env))

# Resolver la ecuación diferencial
sol = sp.dsolve(diff_eq, T)
print("Solución general de la ecuación diferencial:")
display(sol)

# Crear la función de simulación dinámica
def actualizar_simulacion(T_inicial, T_ambiente, k_valor):
    tiempo = np.linspace(0, 200, 200)  # 200 puntos en un rango de tiempo de 0 a 200 segundos

    # Función diferencial para la simulación
    def enfriamiento(T, t, k, T_ambiente):
        return -k * (T - T_ambiente)

    # Resolver la ecuación diferencial numéricamente
    T_solucion = odeint(enfriamiento, T_inicial, tiempo, args=(k_valor, T_ambiente))

    # Graficar los resultados
    plt.figure(figsize=(8, 5))
    plt.plot(tiempo, T_solucion, label="Temperatura del procesador", color="b")
    plt.axhline(y=T_ambiente, color='r', linestyle='--', label="Temperatura ambiente")
    plt.xlabel("Tiempo (segundos)")
    plt.ylabel("Temperatura (°C)")
    plt.title("Modelo de Enfriamiento del Procesador (Ley de Newton)")
    plt.legend()
    plt.grid()

    # Mostrar la gráfica en VS Code
    plt.show()

# Crear sliders para modificar parámetros - Estos se ven si se ejecuta jupyter notebook, ya que si se ejecuta desde terminal no se verán
T_inicial_slider = widgets.FloatSlider(value=85, min=40, max=100, step=1, description="T Inicial (°C)")
T_ambiente_slider = widgets.FloatSlider(value=25, min=10, max=40, step=1, description="T Ambiente (°C)")
k_valor_slider = widgets.FloatSlider(value=0.1, min=0.01, max=0.5, step=0.01, description="k (Enfriamiento)")

# Mostrar la interfaz interactiva
out = widgets.interactive_output(actualizar_simulacion, {
    'T_inicial': T_inicial_slider,
    'T_ambiente': T_ambiente_slider,
    'k_valor': k_valor_slider
})

# Mostrar los controles y la gráfica
display(T_inicial_slider, T_ambiente_slider, k_valor_slider, out)
