# import libraries
import numpy as np
from scipy.integrate import odeint

# the vector valued function to
# describe the velocity field
def vfunc(x,t):
    omega=2*np.pi # 1/s
    v_z=0.2 # m/s
    return np.array([omega*x[1],-omega*x[0],v_z])

# define initial point
x0=np.array([1,0,0])

# define the time instances
# at which the point is recorded
ts=np.linspace(0,10,1000)

# solve the differential equation
# describing the motion of the point
# get a list of points
xs=odeint(vfunc,x0,ts)

# create a 3-D plot of the
# calculated point trajectory
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator)

# initialize the figure and set axes to 3D
fig=plt.figure(figsize=(6,5))
ax=plt.axes(projection='3d')

# plot the trajectory and the starting point
ax.plot3D(xs[:,0],xs[:,1],xs[:,2],color='blue')
ax.scatter(xs[0,0],xs[0,1],xs[0,2],color='red',marker='o',s=20)

# tune and save the figure into a file
ax.set_xlabel(r'$x\,(m)$')
ax.set_ylabel(r'$y\,(m)$')
ax.set_zlabel(r'$z\,(m)$')
ax.grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
ax.xaxis.set_major_locator(MultipleLocator(0.25))
ax.yaxis.set_major_locator(MultipleLocator(0.25))
ax.zaxis.set_major_locator(MultipleLocator(0.25))
fig.tight_layout()
fig.savefig('../figs/example-fig-flowmap-with-odeint.svg',
            bbox_inches='tight',pad_inches=0.3)
plt.close(fig)
