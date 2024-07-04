import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft
from mpl_toolkits.mplot3d import Axes3D

# tiempo t
t = np.arange(0, 501)

# señales x1, x2 y x3
x1 = 2 * np.sin(2 * np.pi * (1/4) * t)
x2 = 0.5 * np.sin(2 * np.pi * (1/10) * t)
x3 = np.sin(2 * np.pi * (1/3) * t)

# Combinamos las señales en una sola señal sumada
x_combined = x1 + x2 + x3

# Aplicamos la STFT
f, t, Zxx = stft(x_combined, fs=1.0, nperseg=128)

# Preparamos los datos para el gráfico 3D
T, F = np.meshgrid(t, f)
Z = np.abs(Zxx)

# Graficamos el espectrograma en 3D
fig = plt.figure(figsize=(14, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T, F, Z, cmap='viridis')

ax.set_title('Espectrograma 3D de la Señal Combinada')
ax.set_xlabel('Tiempo [s]')
ax.set_ylabel('Frecuencia [Hz]')
ax.set_zlabel('Amplitud')
plt.show()
