import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

# microstates
i = np.arange(1, 7)

# constraints
i_bar = 4.5
var_target = 0.5
i2_bar = i_bar**2 + var_target


def equations(lambdas):
    lambda_1, lambda_2 = lambdas
    exp = np.exp(lambda_1 * i + lambda_2 * i**2)
    p = exp / np.sum(exp)

    eq1 = np.sum(i * p) - i_bar
    eq2 = np.sum(i**2 * p) - i2_bar
    return [eq1, eq2]


# initial guess
init = [0.0, 0.0]

sol = root(equations, init)

lambda_1, lambda_2 = sol.x

print("Convergence:", sol.success)
print("lambda_1 =", lambda_1)
print("lambda_2 =", lambda_2)

# probabilities
exp = np.exp(lambda_1 * i + lambda_2 * i**2)
p = exp / np.sum(exp)

print("mean =", np.sum(i * p))
print("variance =", np.sum((i - i_bar)**2 * p))

# plot
plt.figure()
plt.scatter(i, p)
plt.xlabel(r"$i$")
plt.ylabel(r"$p_i$")
plt.title(
    r"$\langle i\rangle = %.2f,\ \mathrm{Var}(i)=%.2f$"
    "\n"
    r"$\lambda_1=%.3f,\ \lambda_2=%.3f$"
    % (i_bar, var_target, lambda_1, lambda_2)
)
plt.savefig("../images/biased_dice_var.png", dpi=300)
plt.tight_layout()
plt.show()
