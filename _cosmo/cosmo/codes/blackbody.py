import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
import scipy.constants as constants
import scipy.special as ss

def blackbody(T, nu):
    """
    blackbody function in term of frequency
    :param T: temperature in Kelvin
    :param nu: frequency in Hertz. 
    """
    A = 2*constants.h*nu**3/constants.c**2
    x = constants.h*nu/constants.k/T
    intensity = A/(np.exp(x) - 1)
    return intensity

def wien(T):
    """
    Derive nu_max associated to a given temperature T using Wien's displacement law.
    :param T: temperature in Kelvin
    """
    a=3+ss.lambertw(-3*np.exp(-3))
    b=a.real*constants.k/constants.h
    return b*T

# frequency
nu = np.linspace(1e13, 3e15, 1000)  

# list of surface temperatures for some stars:
star_Ts = {
    "Proxima Centauri": 3050,
    "Betelgeuse": 3500,
    "Aldebaran": 4300,
    "Sun": 5778,
    "Sirius A": 9940,
    "Rigel": 12000,
}

# plot figure
plt.figure(figsize=(10, 6))
norm = Normalize(vmin=min(star_Ts.values()), vmax=max(star_Ts.values()))
cmap = plt.cm.rainbow.reversed()
sm = ScalarMappable(cmap=cmap, norm=norm)
sm.set_array([])

for star, T in star_Ts.items():
    I = blackbody(T, nu)
    nu_max = wien(T)
    color = cmap(norm(T))
    
    plt.plot(nu / 1e12, I, label=f"{star} (T = {T} K)", color=color)
    plt.axvline(nu_max / 1e12, color=color, linestyle="--", alpha=0.7,
                label=r"$\nu_{\rm max}=%s \, THz$"%(int(nu_max / 1e12)))

plt.xlabel(r"$\nu$ [THz]",fontsize=12)
plt.ylabel(r"$B_\nu\,$ [W·sr⁻¹·Hz⁻¹·m⁻²]",fontsize=12)
plt.legend(fontsize=12)
cbar = plt.colorbar(sm, ax=plt.gca(), orientation='vertical')
cbar.set_label('Surface temperature [K]',fontsize=12)
plt.tight_layout()
plt.savefig("../images/blackbody.png",dpi=600)
plt.show()

