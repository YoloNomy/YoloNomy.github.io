# Plot energy and force of gravity

#WEIGHT ##########################

# x,z coordinates as a grid

x = np.linspace(0, 10, 10)
z = np.linspace(0, 10, 10)
xx, zz = np.meshgrid(x, z)


m=10 # mass arbitrary unit
g=9.81 # gravitational acceleration

# compute the potential energy V

V= m*g*zz

# and its gradient

dY, dX = np.gradient(V)


# plot V and P on top of it

plt.contourf(xx, zz, V,cmap='plasma')
plt.xlabel("x")
plt.ylabel("z")
plt.colorbar(label='V(z)')
plt.quiver(x, z, -1*dX, -1*dY, color='white')
plt.show()

#GRAVITY ##########################


x = np.linspace(-10, 10, 20)
y = np.linspace(-10, 10, 20)
xx, yy = np.meshgrid(x, y)

r= np.sqrt(xx**2+yy**2)

Vg= -1/r**2

#take the log to avoid gigantic arrows

dY, dX = np.gradient(np.log10(-Vg))

plt.contourf(xx, yy, Vg,cmap='plasma_r')
plt.xlabel("x")
plt.ylabel("y")
plt.colorbar(label='V(x,y)')
plt.quiver(x, y, dX, dY, color='white')
plt.show()
