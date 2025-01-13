import pandas as pd

# based and adapted from https://github.com/RobertoIA/Hertzsprung-Russell/blob/master/Hertzsprung-Russell.ipynb

# Données pour les étoiles
stars = {
    'Sun': {'ci': 0.656, 'absmag': 4.83, 'color': 'yellow'},
    'Rigel': {'ci': -0.03, 'absmag': -6.69, 'color': 'purple'},
    'Betelgeuse': {'ci': 1.86, 'absmag': -5.3, 'color': 'red'},
    'Aldebaran': {'ci': 1.54, 'absmag': -0.63, 'color': 'orange'},
    'Sirius': {'ci': -0.01, 'absmag': 1.43, 'color': 'blue'}
}

download="False"
if download=="True":
    !curl -O http://www.astronexus.com/downloads/catalogs/hygdata_v41.csv.gz
    !ls -l | grep hyg
df = pd.read_csv('hygdata_v41.csv.gz')[['absmag', 'ci']]
df.dropna(inplace=True) # drops 1882 rows

def bv2rgb(bv):
    t = (5000 / (bv + 1.84783)) + (5000 / (bv + .673913))
    x, y = 0, 0
    
    if 1667 <= t <= 4000:
        x = .17991 - (2.66124e8 / t**3) - (234358 / t**2) + (877.696 / t)
    elif 4000 < t:
        x = .24039 - (3.02585e9 / t**3) + (2.10704e6 / t**2) + (222.635 / t)
        
    if 1667 <= t <= 2222:
        y = (-1.1063814 * x**3) - (1.34811020 * x**2) + 2.18555832 * x - .20219683
    elif 2222 < t <= 4000:
        y = (-.9549476 * x**3) - (1.37418593 * x**2) + 2.09137015 * x - .16748867
    elif 4000 < t:
        y = (3.0817580 * x**3) - (5.87338670 * x**2) + 3.75112997 * x - .37001483
        
    X = 0 if y == 0 else x / y
    Z = 0 if y == 0 else (1 - x - y) / y
    
    r, g, b = np.dot([X, 1., Z],
        [[3.2406, -.9689, .0557], [-1.5372, 1.8758, -.204], [-.4986, .0415, 1.057]])
    
    R = np.clip(12.92 * r if (r <= 0.0031308) else 1.4 * (r**2 - .285714), 0, 1)
    G = np.clip(12.92 * g if (g <= 0.0031308) else 1.4 * (g**2 - .285714), 0, 1)
    B = np.clip(12.92 * b if (b <= 0.0031308) else 1.4 * (b**2 - .285714), 0, 1)
    
    return [R, G, B, np.random.ranf()]

color = df['ci'].apply(bv2rgb)


# Tracer le diagramme HR
fig = plt.figure(
    figsize=(10, 12),
    facecolor='black',
    dpi=100)
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

ax.scatter(
    df['ci'],
    df['absmag'],
    marker='.',
    s=[5] * len(df),
    facecolors=color,
    linewidth=0)

# Ajouter les étoiles spécifiques
for star, data in stars.items():
    ax.scatter(
        data['ci'], data['absmag'],
        color=data['color'],
        edgecolor='white',
        s=100,  # Taille du point pour les étoiles
        label=star)

# Configurer les limites et les ticks des axes
ax.set_xlim(-.5, 2.5)
ax.set_xticks(np.linspace(0, 2, 3, endpoint=True))
ax.set_ylim(18, -16)
ax.set_yticks(np.linspace(20, -10, 3, endpoint=True))
ax.tick_params(top=False, right=False, direction='out', colors='white')

# ax.annotate(
#     'main sequence (V)', xy=(.6, 6.5), xycoords='data',
#     fontsize='small', color='white',
#     xytext=(-40, -30), textcoords='offset points',
#     arrowprops=dict(
#         arrowstyle="->",
#         connectionstyle="arc3,rad=-.2",
#         color='white'))
# ax.annotate(
#     'giants (II-IV)', xy=(1.8, -1), xycoords='data',
#     fontsize='small', color='white',
#     xytext=(30, 7), textcoords='offset points',
#     arrowprops=dict(
#         arrowstyle="->",
#         connectionstyle="arc3,rad=.2",
#         color='white'))
# ax.annotate(
#     'supergiants (I)', xy=(.5, -14), xycoords='data',
#     fontsize='small', color='white')
# ax.annotate(
#     'white dwarfs (VII)', xy=(0, 16), xycoords='data',
#     fontsize='small', color='white')

# Ajouter une légende pour les étoiles
legend = ax.legend(loc='upper left', fontsize='small', facecolor='black', edgecolor='white')
for text in legend.get_texts():
    text.set_color('white')  # Couleur blanche pour le texte de la légende

# Afficher le diagramme
plt.savefig("../images/Hertzsprung-Russell.png", facecolor='black', edgecolor='white', dpi=600)
plt.show()
