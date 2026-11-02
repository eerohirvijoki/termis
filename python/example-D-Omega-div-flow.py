import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.ticker import (AutoMinorLocator,MultipleLocator)
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
    "text.latex.preamble": r"""
        \usepackage{amsmath} 
        \usepackage{amssymb}
        \usepackage{bm}  % Bold math symbols
    """
})


def mix_colors(color1, color2, fraction):
    """
    Mix two colors: fraction of color1, (1-fraction) of color2
    color1 and color2 can be color names or RGB tuples
    """
    c1 = np.array(mcolors.to_rgb(color1))
    c2 = np.array(mcolors.to_rgb(color2))
    return tuple(fraction * c1 + (1 - fraction) * c2)

# Define the colors
mydarkblue  = mix_colors('blue', 'black', 0.8)   # 80% blue + 20% black
mydarkred   = mix_colors('red', 'black', 0.9)    # 90% red + 10% black
mydarkgreen = mix_colors('green', 'black', 0.4)  # 40% green + 60% black
mydarkorange= mix_colors('red', 'yellow', 0.4)   # 40% red + 60% yellow

u_const=0.0

# --- Flow integrator ---
def propagate(points, velocity_func, dt=0.01, steps=50):
    trajectory = [points.copy()]
    for _ in range(steps):
        v = velocity_func(points)
        points = points + v * dt
        trajectory.append(points.copy())
    return np.array(trajectory)

# --- Velocity fields ---
def strain_flow(points):
    x, y = points[:,0], points[:,1]
    u = x+u_const
    v = -y
    return np.stack([u, v], axis=1)

def rotation_flow(points):
    x, y = points[:,0], points[:,1]
    u = -y+u_const
    v = x
    return np.stack([u, v], axis=1)

def expansion_flow(points):
    x, y = points[:,0], points[:,1]
    u = 0.7*x+u_const
    v = 0.7*y
    return np.stack([u, v], axis=1)

def combined_flow(points):
    return strain_flow(points) + rotation_flow(points) + expansion_flow(points)

# --- Nonuniform rotation ---
def nonuniform_rotation(points, omega=1):
    """
    Nonuniform rotation: angular velocity depends on distance from origin
    u = -omega(y) * y, v = omega(x) * x
    Here we use: omega = k * r
    """
    x, y = points[:,0], points[:,1]
    r = np.sqrt(x**2 + y**2)
    u = -omega * y/(r)+x**2
    v = omega * x/(r)+y**2
    return np.stack([u, v], axis=1)

flows = [strain_flow, rotation_flow, expansion_flow, combined_flow, nonuniform_rotation]
titles = [r'$\bm{u}_D$', r'$\bm{u}_\Omega$', r'$\bm{u}_\text{div}$', r'$\bm{u}_D+\bm{u}_\Omega+\bm{u}_\text{div}$','']

# --- Rectangle mesh (same number of lines, more points along each line) ---
x_min, x_max = -0.5,0.5
y_min, y_max = -0.5,0.5
nx_lines, ny_lines = 6, 6  # number of horizontal/vertical lines
points_per_line = 100       # more points per line for smoothness

x_lines = np.linspace(x_min, x_max, nx_lines)
y_lines = np.linspace(y_min, y_max, ny_lines)
x_dense = np.linspace(x_min, x_max, points_per_line)
y_dense = np.linspace(y_min, y_max, points_per_line)

# Horizontal lines
mesh_xlines = []
for yi in y_lines:
    mesh_xlines.append(np.stack([x_dense, np.full_like(x_dense, yi)], axis=1))

mesh_ylines = []
# Vertical lines
for xi in x_lines:
    mesh_ylines.append(np.stack([np.full_like(y_dense, xi), y_dense], axis=1))

# Rotate points and shift the points
all_xpoints = np.vstack(mesh_xlines)
all_ypoints = np.vstack(mesh_ylines)
th=2*np.pi*45/360
R=np.array([[np.cos(th),-np.sin(th)],[np.sin(th),np.cos(th)]])
all_xpoints=(R.dot(all_xpoints.transpose())).transpose()#+np.array([0.5,0])
all_ypoints=(R.dot(all_ypoints.transpose())).transpose()#+np.array([0.5,0])


# --- Propagate and plot ---
#plt.figure(figsize=(25,5))

fig1,ax1=plt.subplots(1,3,figsize=(6,2),constrained_layout=True)
fig2,ax2=plt.subplots(figsize=(2,2))
fig3,ax3=plt.subplots(figsize=(2,2))
ax1=ax1.flatten()
ax2 = np.atleast_1d(ax2)
ax3 = np.atleast_1d(ax3)
all_axes=np.concatenate([ax1,ax2,ax3])

for i, flow in enumerate(flows):
    traj_x = propagate(all_xpoints.copy(), flow)
    final_points_x = traj_x[-1]
    traj_y= propagate(all_ypoints.copy(), flow)
    final_points_y = traj_y[-1]

    # Plot original mesh
    start = 0
    for line in mesh_xlines:
        n = line.shape[0]
        all_axes[i].plot(all_xpoints[start:start+n,0], all_xpoints[start:start+n,1], color=mydarkorange, linestyle='-', alpha=0.2)
        start += n

    start = 0
    for line in mesh_ylines:
        n = line.shape[0]
        all_axes[i].plot(all_ypoints[start:start+n,0], all_ypoints[start:start+n,1], color=mydarkblue, linestyle='-', alpha=0.2)
        start += n

    # Plot deformed mesh
    start = 0
    for line in mesh_xlines:
        n = line.shape[0]
        all_axes[i].plot(final_points_x[start:start+n,0], final_points_x[start:start+n,1], color=mydarkorange, linestyle='-', alpha=0.9)
        start += n
    start = 0
    for line in mesh_ylines:
        n = line.shape[0]
        all_axes[i].plot(final_points_y[start:start+n,0], final_points_y[start:start+n,1], color=mydarkblue, linestyle='-', alpha=0.8)
        start += n

    all_axes[i].axis('equal')
    all_axes[i].set_xlabel(r'$x/L_0$')
    if i == 0 or i==3 or i==4:
        all_axes[i].set_ylabel(r'$y/L_0$')
    all_axes[i].set_xlim([x_min*3,x_max*3])
    all_axes[i].set_ylim([y_min*3,y_max*3])
    all_axes[i].set_title(titles[i])
    all_axes[i].xaxis.set_minor_locator(AutoMinorLocator(4))
    all_axes[i].yaxis.set_minor_locator(AutoMinorLocator(4))
    all_axes[i].grid(which='major',color='#CCCCCC',linestyle='-',linewidth=0.3)
    all_axes[i].grid(which='minor',color='#CCCCCC',linestyle=':',linewidth=0.1)
    #all_axes[i].yaxis.set_major_locator(MultipleLocator(10))
    #all_axes[i].xaxis.set_major_locator(MultipleLocator(0.002))
    all_axes[i].set_title(titles[i])
    #plt.grid(True)

fig1.savefig('../figs/example-fig-D-Omega-div-flow-individually.svg',bbox_inches='tight')
fig2.savefig('../figs/example-fig-D-Omega-div-flow-combined.svg',bbox_inches='tight')
fig3.savefig('../figs/example-fig-D-Omega-div-flow-complicated.svg',bbox_inches='tight')

plt.close(fig1)
plt.close(fig2)
plt.close(fig3)
