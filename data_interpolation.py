import csv
import math
import numpy as np

# Paths defined:
input = "data_new/dynamic_pressure_field_original.csv"
output = "data_new/dynamic_pressure_field_numerically_processed_final.csv"

# Step 1: Read the original CSV file
data = []
sorted_data = []

with open(input, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        x = float(row[1])
        y = float(row[2])
        z = float(row[3])
        pressure = float(row[4])

        x = x + 0.25
        y = y + 0.25

        x = np.format_float_positional(x, precision=3)
        y = np.format_float_positional(y, precision=3)
        z = np.format_float_positional(z, precision=3)

        row_data = [x, y, z, pressure]
        data.append(row_data)

data = np.array(data)
sort_indices = np.lexsort((data[:, 2], data[:, 1], data[:, 0]))
sorted_data = data[sort_indices]

# Step 2: Create empty lists for new values
new_data = []
new_sorted_data = []

# Step 3: Generate new x, y, z values
step_size = 0.01
max_value = 0.5
for x in range(0, int(max_value/step_size)):
    for y in range(0, int(max_value/step_size)):
        for z in range(0, int(max_value/step_size)):
            new_x = x * step_size
            new_y = y * step_size
            new_z = z * step_size

            new_row_data = [new_x, new_y, new_z]
            new_data.append(new_row_data)

new_data = np.array(new_data)
new_sort_indices = np.lexsort((new_data[:, 2], new_data[:, 1], new_data[:, 0]))
new_sorted_data = new_data[new_sort_indices]
pressure = np.array([sorted_data[:, 3]])
pressure = np.transpose(pressure)
new_sorted_data = np.concatenate((new_sorted_data, pressure), axis=1)
#new_sorted_data = np.append(new_sorted_data, pressure, axis=1)

header = ['x', 'y', 'z', 'dynamic pressure']

with open(output, 'w', newline='') as output_file:
    writer = csv.writer(output_file)

    writer.writerow(header)
    writer.writerows(new_sorted_data)

