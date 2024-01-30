
from scipy.stats import norm 

x=np.arange(0,30,0.1)
T= 15+10*norm.pdf(x, 15, 5)
plt.plot(x, T ,c='darkred') 
plt.plot(x[:-1], np.diff(T)/np.diff(x) ,c='darkblue') 
plt.plot(x,0*np.ones(len(x)),c='k',linestyle='--')
plt.ylabel("$T(x)$")
plt.xlabel("$x$")
plt.show() 
