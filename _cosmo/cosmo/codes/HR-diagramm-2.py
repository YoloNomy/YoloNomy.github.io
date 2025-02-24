import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
import matplotlib.patheffects as path_effects
from matplotlib.patches import Ellipse

stars = {
    'Sun': {'ci': 0.656, 'absmag': 4.83, 'color': 'yellow'},
    'Rigel': {'ci': -0.03, 'absmag': -6.69, 'color': 'purple'},
    'Betelgeuse': {'ci': 1.86, 'absmag': -5.3, 'color': 'red'},
    'Aldebaran': {'ci': 1.54, 'absmag': -0.63, 'color': 'orange'},
    'Sirius': {'ci': -0.01, 'absmag': 1.43, 'color': 'blue'}
}

spectral_types = {
    'O': {'color': '#9bb0ff', 'range': (-0.4, -0.2)},
    'B': {'color': '#aabfff', 'range': (-0.2, 0)},
    'A': {'color': '#cad7ff', 'range': (0, 0.3)},
    'F': {'color': '#f8f7ff', 'range': (0.3, 0.6)},
    'G': {'color': '#fff4e8', 'range': (0.6, 0.8)},
    'K': {'color': '#ffd2a1', 'range': (0.8, 1.4)},
    'M': {'color': '#ffcc6f', 'range': (1.4, 2.5)}
}

zones = {
    "0: Hypergiants": {"center": (0.75, -12), "width": 2, "height": 2, "angle": 0},
    "I: Supergiants": {"center": (0.75, -7), "width": 2, "height": 3, "angle": 0},
    "II: Bright Giants": {"center": (0.75, -4), "width": 2, "height": 2.5, "angle": 0},
    "III: Giants": {"center": (1.40, -0.5), "width": 1.5, "height": 4, "angle": 0},
    "IV: Subgiants": {"center": (1.25, 3), "width": 0.5, "height": 1.5, "angle": -10},
    "V: Main Sequence": {"center": (0.75, 5), "width": 1.0, "height": 15, "angle": -8},
    "VI: Subdwarfs": {"center": (-0.1, 7), "width": 0.6, "height": 2, "angle": 0},
    "VII: White Dwarfs": {"center": (-0.1, 13), "width": 2, "height": 2, "angle": -40},
}

download="False"
if download=="True":
    !curl -O http://www.astronexus.com/downloads/catalogs/hygdata_v41.csv.gz
    !ls -l | grep hyg
df = pd.read_csv('hygdata_v41.csv.gz')[['absmag', 'ci']]
df.dropna(inplace=True)

# Tracer le diagramme HR (inchangé)
fig = plt.figure(
    figsize=(10, 12),
    facecolor='black',
    dpi=72)
ax = fig.add_axes([.1, .1, .85, .8])

ax.set_facecolor('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_color('white')
ax.spines['bottom'].set_color('white')

ax.set_title('Hertzsprung-Russell Diagram', color='white', fontsize=18)
ax.title.set_position([.5, 1.03])
ax.set_xlabel('Color Index (B-V)', color='white')
ax.set_ylabel('Absolute Magnitude (M)', color='white')

# Ajouter les bandes de couleurs pour les types spectraux
for s_type, s_data in spectral_types.items():
    rect = Rectangle((s_data['range'][0], -15), s_data['range'][1] - s_data['range'][0], 33,
                     linewidth=0, edgecolor='none', facecolor=s_data['color'], alpha=0.7)
    ax.add_patch(rect)
    ax.text((s_data['range'][0] + s_data['range'][1]) / 2, -14, s_type, color='white', fontsize=12, ha='center')

ax.scatter(
    df['ci'],
    df['absmag'],
    marker='.',
    s=[5] * len(df),
    facecolors='white',
    linewidth=0)

for label, props in zones.items():
    ellipse = Ellipse(xy=props["center"], width=props["width"], height=props["height"],
                      angle=props["angle"], edgecolor='red', facecolor='red', alpha=0.5,
                      linestyle='dashed', linewidth=1.5)
    ax.add_patch(ellipse)
    ax.text(props["center"][0], props["center"][1], label, ha='center', va='center', color='white', fontsize=10)

for star, data in stars.items():
    ax.scatter(
        data['ci'], data['absmag'],
        color=data['color'],
        edgecolor='white',
        s=100,
        label=star)

ax.set_xlim(-.4, 2.)
ax.set_xticks(np.linspace(0, 2, 3, endpoint=True))
ax.set_ylim(18, -16)
ax.set_yticks(np.linspace(20, -10, 3, endpoint=True))
ax.tick_params(top=False, right=False, direction='out', colors='white')

plt.tight_layout()
plt.savefig("../images/Hertzsprung-Russell-2.png", facecolor='black', edgecolor='white', dpi=600)
plt.show()
