# Modelado del Enfriamiento de un Procesador con la Ley de Newton

### UNIVERSIDAD INTERAMERICANA PARA EL DESARROLLO

### CAMPUS ACAPULCO

### J. KAROL RAMÍREZ HERRERA

## 1. Introducción

Este proyecto implementa un modelo matemático basado en la **Ley de Enfriamiento de Newton** para simular la temperatura de un procesador. Se utiliza una **ecuación diferencial de primer orden** que describe cómo la temperatura del procesador cambia con el tiempo al reducir su carga de trabajo del **100% al 30%**.

El modelo ha sido implementado en **Python** utilizando bibliotecas científicas como `SymPy`, `SciPy`, `Matplotlib` e `ipywidgets` para proporcionar una simulación interactiva.

---

## 2. Objetivo

El objetivo principal de este proyecto es desarrollar una simulación computacional que permita visualizar el proceso de enfriamiento de un procesador mediante la **resolución de una ecuación diferencial**. Además, el modelo permite modificar los valores iniciales y observar cómo la temperatura varía con el tiempo bajo distintas condiciones.

---

## 3. Modelo Matemático

El modelo de enfriamiento sigue la ecuación diferencial:

\[
\frac{dT}{dt} = -k (T - T\_{\infty})
\]

Donde:

- \( T \) es la temperatura del procesador en función del tiempo.
- \( T\_{\infty} \) es la temperatura ambiente.
- \( k \) es la constante de enfriamiento del sistema.
- \( \frac{dT}{dt} \) representa la tasa de cambio de la temperatura con el tiempo.

La ecuación diferencial se resuelve utilizando `SymPy`, obteniendo una solución analítica. Posteriormente, `SciPy` se emplea para resolver el modelo numéricamente y visualizar los resultados en una gráfica.

---

## 4. Requisitos

Antes de ejecutar el proyecto, asegúrate de tener **Python 3.8 o superior** instalado. Se requieren las siguientes bibliotecas:

```sh
pip install numpy scipy matplotlib sympy ipywidgets
```
# Enfriamiento
