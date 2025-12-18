import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# --------------------------------
# Microstates energies
# --------------------------------
N_states = 10000
E_i = np.linspace(0, 10, N_states)

# Auxiliary beta scan (not final physical input but needed to explore the parameter space)
beta_scan = np.linspace(0.2, 3.0, 200)

mean_energy = []
entropy = []
distributions = []

# --------------------------------
# Canonical construction
# --------------------------------
# We use here all the formula of the lectures
for beta in beta_scan:
    Z = np.sum(np.exp(-beta * E_i))
    p_i = np.exp(-beta * E_i) / Z

    mean_energy.append(np.sum(p_i * E_i))
    entropy.append(-np.sum(p_i * np.log(p_i)))
    distributions.append(p_i)

mean_energy = np.array(mean_energy)
entropy = np.array(entropy)
distributions = np.array(distributions)

# --------------------------------
# Sort by <E> (needed for derivative)
# --------------------------------
idx = np.argsort(mean_energy)
mean_energy = mean_energy[idx]
entropy = entropy[idx]
distributions = distributions[idx]
beta_scan = beta_scan[idx]

# --------------------------------
# Derive beta from entropy
# --------------------------------
# for each curve, beta = 1/T = dS/d<E>

beta_derived = np.gradient(entropy, mean_energy)

# --------------------------------
# Colormap based on entropy
# --------------------------------
norm = colors.Normalize(vmin=entropy.min(), vmax=entropy.max())
cmap = cm.coolwarm

plt.figure(figsize=(7, 5))

# Select a subset of curves for readability
indices = np.linspace(0, len(mean_energy)-1, 6, dtype=int)

for i in indices:
    plt.plot(
        E_i,
        distributions[i],
        color=cmap(norm(entropy[i])),
        label=rf"$T={1/beta_derived[i]:.2f},\ \langle E\rangle={mean_energy[i]:.2f}$"
    )

# Colorbar
sm = cm.ScalarMappable(norm=norm, cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm)
cbar.set_label(r"Entropy $S(\langle E\rangle)$")

plt.xlabel(r"Microstate energy $E_i$")
plt.ylabel(r"Probability $p_i$")
plt.legend()
plt.tight_layout()
plt.semilogx()
plt.savefig("../images/canonical_boltzmann_beta_derived.png", dpi=300)
plt.show()
