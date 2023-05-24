import csv
import matplotlib.pyplot as plt
import numpy as np

# specify the path to your CSV file
#csv_path = 'data_new/dynamic_pressure_field_numerically_processed_4rotor.csv'
csv_path = 'data_final/dynamic_pressure_field_processed_round.csv'
# specify the z plane you want to plot
z_plane = 0.0
x_plane = 0.25

# initialize empty lists to store x, y, z, and pressure values
x_vals = []
y_vals = []
z_vals = []
pressure_vals = []

# read in the CSV file and extract the x, y, z, and pressure values
with open(csv_path, 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    for row in reader:
        x_vals.append(float(row[1]))
        y_vals.append(float(row[2]))
        z_vals.append(float(row[3]))
        pressure_vals.append(float(row[4]))

# convert the x, y, z, and pressure lists to numpy arrays
x_arr = np.array(x_vals)
y_arr = np.array(y_vals)
z_arr = np.array(z_vals)
pressure_arr = np.array(pressure_vals)

# check if the desired z plane is in the z array
if z_plane not in z_arr:
    # if not, find the closest z value
    closest_z = z_arr[np.argmin(np.abs(z_arr - z_plane))]
    print(f"Desired z plane value {z_plane} not found in CSV file. Using closest z plane value {closest_z}")
    z_plane = closest_z

# check if the desired x plane is in the x array
if x_plane not in x_arr:
    # if not, find the closest x value
    closest_x = x_arr[np.argmin(np.abs(x_arr - x_plane))]
    print(f"Desired x plane value {x_plane} not found in CSV file. Using closest x plane value {closest_x}")
    x_plane = closest_x


# create a 2D meshgrid from the x and y arrays
x_mesh_z, y_mesh_z = np.meshgrid(np.unique(x_arr), np.unique(y_arr))

# create a 2D meshgrid from the z and y arrays
z_mesh_x, y_mesh_x = np.meshgrid(np.unique(z_arr), np.unique(y_arr))

# create a 2D array of pressure values corresponding to each x-y pair in the z meshgrid
pressure_mesh_z = np.zeros_like(x_mesh_z)
for i, x_val in enumerate(np.unique(x_arr)):
    for j, y_val in enumerate(np.unique(y_arr)):
        z_index = np.where((x_arr == x_val) & (y_arr == y_val) & (z_arr == z_plane))[0]
        if len(z_index) > 0:
            pressure_mesh_z[j, i] = pressure_arr[z_index[0]]

# create a 2D array of pressure values corresponding to each z-y pair in the x meshgrid
pressure_mesh_x = np.zeros_like(z_mesh_x)
for k, z_val in enumerate(np.unique(z_arr)):
    for l, y_val in enumerate(np.unique(y_arr)):
        x_index = np.where((z_arr == z_val) & (y_arr == y_val) & (x_arr == x_plane))[0]
        if len(x_index) > 0:
            pressure_mesh_x[l, k] = pressure_arr[x_index[0]]


# create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# plot the pressure heatmap for the z plane on the first subplot
im1 = axs[0].pcolormesh(x_mesh_z, y_mesh_z, pressure_mesh_z, cmap='jet')
axs[0].set_xlabel('x [m]')
axs[0].set_ylabel('y [m]')
axs[0].set_title(f'Pressure on z={z_plane} [m]')
fig.colorbar(im1, ax=axs[0], label='Pressure [Pa]')

# plot the pressure heatmap for the x plane on the second subplot
im2 = axs[1].pcolormesh(y_mesh_x, z_mesh_x, pressure_mesh_x, cmap='jet')
#im2 = axs[1].scatter(y_mesh_x, z_mesh_x, c=pressure_mesh_x, cmap='jet')
axs[1].set_xlabel('y [m]')
axs[1].set_ylabel('z [m]')
axs[1].set_title(f'Pressure on x={x_plane} [m]')
fig.colorbar(im2, ax=axs[1], label='Pressure [Pa]')

# set aspect ratio to equal for both subplots
axs[0].set_aspect('equal', 'box')
axs[1].set_aspect('equal', 'box')

# adjust the layout of the subplots to prevent overlap
fig.tight_layout()

# display the plot
plt.show()
