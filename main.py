import numpy as np
import matplotlib.pyplot as plt


def solveFD(nx, ny, f, size):
    # Solve Poisson equation using finite difference method
    for it in range(size):
        un = u.copy()
        for i in range(1, nx - 1):
            for j in range(1, ny - 1):
                u[i, j] = (dx**2 * dy**2 * f[i, j] + dy**2 * (un[i - 1, j] + un[i + 1, j]) + dx**2 * (un[i, j - 1] + un[i, j + 1])) / (2 * (dx**2 + dy**2))
    return u


## COMPUTATIONAL DOMAIN DEFINITION
nx, ny = 100, 100  # number of points in x and y directions
dx = 1.0 / (nx - 1)  # grid spacing in the x direction
dy = 1.0 / (ny - 1)  # grid spacing in the y direction

# Create grid
x = np.linspace(0, 1, nx)
y = np.linspace(0, 1, ny)
X, Y = np.meshgrid(x, y)

# Define source term
f = np.sin(np.pi * X) * np.sin(np.pi * Y)

# Define size
size = 100


# Initialize solution array
u = np.zeros((nx, ny))

# Define boundary conditions
u[0, :] = 0.0  # u = 0 at x = 0
u[-1, :] = 0.0  # u = 0 at x = 1
u[:, 0] = 0.0  # u = 0 at y = 0
u[:, -1] = 0.0  # u = 0 at y = 1

# Solve Poisson equation using finite difference method
u = solveFD(nx, ny, f, size)




# Plot solution
F = plt.gcf()
Size = F.get_size_inches()
F.set_size_inches(Size[0]*1.5, Size[1]*1.5, forward=True) 

ax = F.add_subplot(111, projection='3d')
ax.set_facecolor('white')
ax.set_facecolor('white')  # Set face color to white
ax.xaxis.pane.fill = False  # Remove background color from x-axis plane
ax.yaxis.pane.fill = False  # Remove background color from y-axis plane
ax.zaxis.pane.fill = False  # Remove background color from z-axis plane
ax.grid(False)  # Remove grid lines
ax.zaxis.line.set_visible(False) # Hide the z-axis
ax.w_zaxis.line.set_color('none')  # Remove z-axis line by setting color 
for spine in ax.spines.values():
    spine.set_color('none')  # Remove box by setting color to 'none'

# Create the surface plot
surf = ax.plot_surface(X, Y, u, cmap='bwr', alpha=0.8)

# Set contour levels
contour_min = np.min(u)
contour_max = np.max(u)
contour_levels = np.linspace(contour_min, contour_max, 11)

contour = ax.contour(X, Y, u, zdir='z', offset=contour_min, cmap='bwr', linestyles="solid", levels = contour_levels)

# Colorbar properties
cbar = F.colorbar(surf)
cbar_ticks = np.linspace(contour_min, contour_max, 5)
cbar.set_ticks(cbar_ticks)
cbar.set_ticklabels([f'{tick:.2f}' for tick in cbar_ticks])
cbar.set_label('u', rotation=90, labelpad=15)
cbar.ax.tick_params(labelsize=18)  # Set font size for ticks
cbar.set_ticklabels([f'{tick:.2f}' for tick in cbar_ticks])

ax.set_xlabel('x', fontsize=20,fontname = "Times New Roman", fontweight="normal")
ax.set_ylabel('y', fontsize=20,fontname = "Times New Roman", fontweight="normal")
cbar.set_label('u', rotation=270, labelpad=15, fontdict={'family': 'Times New Roman', 'size': 20})  # Set font type and size for label

ax.zaxis.set_ticks([])  # Remove z-axis ticks

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300

plt.show()