import numpy as np
import matplotlib.pyplot as plt

# Grid
x = np.linspace(-3, 3, 400)
y = np.linspace(-3, 3, 400)
X, Y = np.meshgrid(x, y)

# Function
Z = 3 * X**2 + Y**2

# Figure
plt.figure()

# Contours with colormap (increasing values)
contours = plt.contour(
    X, Y, Z,
    levels=20,
    cmap='viridis',
    linestyles='dashed'
)

# Colorbar
plt.colorbar(contours, label=r'$f(x,y)=3x^2+y^2$')

# Constraint x + 2y = 3
y_line = (3 - x) / 2
plt.plot(x, y_line, color='red', linewidth=2, label=r'$x+2y=3$')

# Axes lines
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

#adding the solution we found analytically:
plt.scatter(3/13, 18/13, color='orange', marker='*', zorder=5,s=100)

# Formatting
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')
plt.legend()
plt.tight_layout()
plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.savefig('../images/exercice_lagrange_mult.png', dpi=300)
plt.show()
