import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Constants
k_B = 1.380649e-23  # Boltzmann constant (J/K)
m = 4.65e-26        # Mass of particle (kg), e.g., N2 molecule

# Maxwell-Boltzmann distribution function
def maxwell_boltzmann(v, T):
    return 4 * np.pi * (m / (2 * np.pi * k_B * T))**1.5 * v**2 * np.exp(-m * v**2 / (2 * k_B * T))

# Speed array
v = np.linspace(0, 2000, 1000)  # m/s

# Temperatures in Kelvin (more curves)
temperatures = [50, 100, 200, 300, 400, 600, 800]

# Colormap from red (hot) to blue (cold)
cmap = cm.get_cmap('coolwarm')  # red to blue
colors = [cmap(i / (len(temperatures)-1)) for i in range(len(temperatures))]

# Plot curves
plt.figure(figsize=(7, 5))
for T, color in zip(temperatures, colors):
    f_v = maxwell_boltzmann(v, T)
    plt.plot(v, f_v, color=color, label=f'T = {T} K')

plt.xlabel(r'$v$ (m/s)')
plt.ylabel(r'$\rho(v)$')
plt.legend()
plt.tight_layout()
plt.savefig("../images/Maxwell_Boltzmann.png", dpi=300)
plt.show()
