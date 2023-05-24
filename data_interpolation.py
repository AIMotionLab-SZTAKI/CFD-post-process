import csv
import math
import numpy as np

# Paths defined:
input = "data_new/dynamic_pressure_field_original.csv"
output = "data_new/dynamic_pressure_field_numerically_processed.csv"

# Step 1: Read the original CSV file
x_values = []
y_values = []
z_values = []
pressure_values = []

with open(input, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        x_values.append(float(row[1]))
        y_values.append(float(row[2]))
        z_values.append(float(row[3]))
        pressure_values.append(float(row[4]))

# Step 2: Create empty lists for new values
new_x_values = []
new_y_values = []
new_z_values = []
new_pressure_values = []

# Step 3: Generate new x, y, z values
step_size = 0.1
max_value = 0.5
for x in range(0, int(max_value/step_size)):
    for y in range(0, int(max_value/step_size)):
        for z in range(0, int(max_value/step_size)):
            new_x_values.append(x * step_size)
            new_y_values.append(y * step_size)
            new_z_values.append(z * step_size)

# Step 4-7: Find closest values and assign pressure
for i in range(len(new_x_values)):
    closest_distance = float('inf')
    closest_index = None
    print(f"Value i:{i}")

    for j in range(len(x_values)):
        distance = math.sqrt(
            (new_x_values[i] - x_values[j]) ** 2 +
            (new_y_values[i] - y_values[j]) ** 2 +
            (new_z_values[i] - z_values[j]) ** 2
        )

        if distance < closest_distance:
            closest_distance = distance
            closest_index = j

    new_pressure_values.append(pressure_values[closest_index])

# Step 8: Print or process the new x, y, z, and pressure values
# for k in range(len(new_x_values)):
#     print(f'x: {new_x_values[k]}, y: {new_y_values[k]}, z: {new_z_values[k]}, pressure: {new_pressure_values[k]}')

# Step 9: Write out the new .csv file
new_x_values = np.array(new_x_values)
new_y_values = np.array(new_y_values)
new_z_values = np.array(new_z_values)
new_pressure_values = np.array(new_pressure_values)

data = np.array([new_x_values, new_y_values, new_z_values, new_pressure_values])
data = np.transpose(data)
header = ['x', 'y', 'z', 'dynamic pressure']

with open(output, 'w', newline='') as output_file:
    writer = csv.writer(output_file)

    writer.writerow(header)
    writer.writerows(data)

