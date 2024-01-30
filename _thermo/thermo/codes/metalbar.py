
from scipy.stats import norm 
import numpy as np 
import matplotlib.pyplot as plt

x=np.arange(0,30,0.1) #x axis
T= 10*norm.pdf(x, 15, 5) # put any function of $x$ you want here!
Q= np.diff(T)/np.diff(x) # computing numerically the derivative

# plotting figures

plt.plot(x, T ,c='darkred') #T(x)
plt.plot(x[:-1], Q ,c='darkblue') #Q(x)
plt.plot(x,0*np.ones(len(x)),c='k',linestyle='--') # a bar labelling the zero
plt.ylabel("$d T(x)/dx$")
plt.xlabel("$x$")
plt.show() 
