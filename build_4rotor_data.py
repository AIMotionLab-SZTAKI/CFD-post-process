import csv
import numpy as np

# Input data:
input = "data/dynamic_pressure_field.csv"
output = "data/dynamic_pressure_field_processed_4rotor.csv"

# Displacement constants:
l_real = 0.0884
l_x1 = 0.074
l_x2 = 0.091
l_y= 0.087
l=0.09
d = 0.25

# Calculate the origo and the intervallum of the different domains:
x1_O = d - l
y1_O = d - l
x1_lim = [0, d]
y1_lim = [0, d]

x2_O = d + l
y2_O = d - l
x2_lim = [d, 2*d]
y2_lim = [0, d]

x3_O = d + l
y3_O = d + l
x3_lim = [d, 2*d]
y3_lim = [d, 2*d]

x4_O = d - l
y4_O = d + l
x4_lim = [0, d]
y4_lim = [d, 2*d]

# Open input CSV file and output CSV file
with open(input, 'r') as input_file, open(output, 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write header line to output CSV file
    writer.writerow(next(reader))

    data=[]
    sorted_data=[]


    # Iterate through each row in the input CSV file
    for row in reader:
        node = float(row[0])
        x = float(row[1])
        y = float(row[2])
        z = float(row[3])
        pressure = float(row[4])

        x = float(np.format_float_positional(x,precision=3))
        y = float(np.format_float_positional(y,precision=3))
        z = float(np.format_float_positional(z,precision=3))

        x1 = x + x1_O
        y1 = y + y1_O
        z1 = z
        node1 = node
        pressure1 = pressure

        x2 = x + x2_O
        y2 = y + y2_O
        z2 = z
        node2 = node
        pressure2 = pressure

        x3 = x + x3_O
        y3 = y + y3_O
        z3 = z
        node3 = node
        pressure3 = pressure

        x4 = x + x4_O
        y4 = y + y4_O
        z4 = z
        node4 = node
        pressure4 = pressure

        if x1 >= x1_lim[0] and x1 <= x1_lim[1] and y1 >= y1_lim[0] and y1 <= y1_lim[1]:
            row_data1 = [node1, x1, y1, z1, pressure1]
            data.append(row_data1)

        if x2 >= x2_lim[0] and x2 <= x2_lim[1] and y2 >= y2_lim[0] and y2 <= y2_lim[1]:
            row_data2 = [node2, x2, y2, z2, pressure2]
            data.append(row_data2)

        if x3 >= x3_lim[0] and x3 <= x3_lim[1] and y3 >= y3_lim[0] and y3 <= y3_lim[1]:
            row_data3 = [node3, x3, y3, z3, pressure3]
            data.append(row_data3)

        if x4 >= x4_lim[0] and x4 <= x4_lim[1] and y4 >= y4_lim[0] and y4 <= y4_lim[1]:
            row_data4 = [node4, x4, y4, z4, pressure4]
            data.append(row_data4)


    data=np.array(data)
    sort_indices = np.lexsort((data[:, 1], data[:, 2], data[:, 3]))
    sorted_data = data[sort_indices]

    writer.writerows(sorted_data)


