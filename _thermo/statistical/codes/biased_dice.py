import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# array of microstates
i = np.arange(1, 7)

# observed mean
i_bar = 4.5


def f(lambda_1):
    #function to solve as f=0 in order to find lambda_1
    exp = np.exp(lambda_1 * i)
    p = exp / np.sum(exp)
    return np.sum(i * p) - i_bar

lambda_1 = brentq(f, 0.0, 1.0)
print(f(lambda_1)) #should give zero!
print(lambda_1)

# Compute probabilities
exp = np.exp(lambda_1 * i)
p = exp / np.sum(exp)

print("lambda_1 =", lambda_1)
print("mean =", np.sum(i * p))

# Plot
plt.figure()
plt.scatter(i, p)
plt.xlabel(r"$i$ (dice number)")
plt.ylabel(r"Probability $p_i$")
plt.title(r"$\langle i\rangle $=%s, $\lambda_1$ = %s"%(i_bar,np.round(lambda_1,4)))
#plt.legend()
plt.tight_layout()
plt.savefig("../images/biased_dice.png", dpi=300)
plt.show()
