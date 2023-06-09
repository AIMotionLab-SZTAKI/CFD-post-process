import csv
import numpy as np

# Input data:
input = "data_new/dynamic_pressure_field_numerically_processed_final.csv"
output = "data_new/dynamic_pressure_field_numerically_processed_final_4rotor.csv"

# Displacement constants:
l_real = 0.0884
l_x1 = 0.074
l_x2 = 0.091
l_y = 0.087
l = 0.085
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

mirror = False
separate = False # if True the flows does not modify each other

# how many decimals to round
precision = 3

# Open input CSV file and output CSV file
with open(input, 'r') as input_file, open(output, 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write header line to output CSV file
    writer.writerow(next(reader))

    data = []
    sorted_data = []

    # Iterate through each row in the input CSV file
    for row in reader:
        x = float(row[0])
        y = float(row[1])
        z = float(row[2])
        pressure = float(row[3])

        # x = float(np.format_float_positional(x,precision=precision1))
        # y = float(np.format_float_positional(y,precision=precision1))
        # z = float(np.format_float_positional(z,precision=precision1))

        # x = round(x, precision)
        # y = round(y, precision)
        # z = round(z, precision)

        # x = np.around(x, decimals=precision)
        # y = np.around(y, decimals=precision)
        # z = np.around(z, decimals=precision)

        x1 = x + x1_O
        y1 = y + y1_O
        z1 = z
        x1 = float(np.format_float_positional(x1,precision=precision))
        y1 = float(np.format_float_positional(y1,precision=precision))
        z1 = float(np.format_float_positional(z1,precision=precision))
        pressure1 = pressure

        x2 = x + x2_O
        y2 = y + y2_O
        z2 = z
        x2 = float(np.format_float_positional(x2,precision=precision))
        y2 = float(np.format_float_positional(y2,precision=precision))
        z2 = float(np.format_float_positional(z2,precision=precision))
        pressure2 = pressure

        x3 = x + x3_O
        y3 = y + y3_O
        z3 = z
        x3 = float(np.format_float_positional(x3,precision=precision))
        y3 = float(np.format_float_positional(y3,precision=precision))
        z3 = float(np.format_float_positional(z3,precision=precision))
        pressure3 = pressure

        x4 = x + x4_O
        y4 = y + y4_O
        z4 = z
        x4 = float(np.format_float_positional(x4,precision=precision))
        y4 = float(np.format_float_positional(y4,precision=precision))
        z4 = float(np.format_float_positional(z4,precision=precision))
        pressure4 = pressure


        if separate==True:
            if x1 >= x1_lim[0] and x1 <= x1_lim[1] and y1 >= y1_lim[0] and y1 <= y1_lim[1]:
                x1 = float(np.format_float_positional(x1, precision=precision))
                y1 = float(np.format_float_positional(y1, precision=precision))
                z1 = float(np.format_float_positional(z1, precision=precision))
                row_data1 = [x1, y1, z1, pressure1]
                data.append(row_data1)

            if x2 >= x2_lim[0] and x2 <= x2_lim[1] and y2 >= y2_lim[0] and y2 <= y2_lim[1]:
                x2 = float(np.format_float_positional(x2, precision=precision))
                y2 = float(np.format_float_positional(y2, precision=precision))
                z2 = float(np.format_float_positional(z2, precision=precision))
                row_data2 = [x2, y2, z2, pressure2]
                data.append(row_data2)

            if x3 >= x3_lim[0] and x3 <= x3_lim[1] and y3 >= y3_lim[0] and y3 <= y3_lim[1]:
                x3 = float(np.format_float_positional(x3, precision=precision))
                y3 = float(np.format_float_positional(y3, precision=precision))
                z3 = float(np.format_float_positional(z3, precision=precision))
                row_data3 = [x3, y3, z3, pressure3]
                data.append(row_data3)

            if x4 >= x4_lim[0] and x4 <= x4_lim[1] and y4 >= y4_lim[0] and y4 <= y4_lim[1]:
                x4 = float(np.format_float_positional(x4, precision=precision))
                y4 = float(np.format_float_positional(y4, precision=precision))
                z4 = float(np.format_float_positional(z4, precision=precision))
                row_data4 = [x4, y4, z4, pressure4]
                data.append(row_data4)


        else:
            tollerance = True
            tol = 0.005
            if tollerance == False:
                if x1 >= x1_lim[0] and x1 <= x1_O + d and y1 >= y1_lim[0]  and y1 <= y1_O + d:
                    # x1 = float(np.format_float_positional(x1, precision=precision))
                    # y1 = float(np.format_float_positional(y1, precision=precision))
                    # z1 = float(np.format_float_positional(z1, precision=precision))
                    # x1 = float(round(x1, precision))
                    # y1 = float(round(y1, precision))
                    # z1 = float(round(z1, precision))
                    row_data1 = [x1, y1, z1, pressure1]
                    data.append(row_data1)

                if x2 >= x2_O - d and x2 <= x2_lim[1] and y2 >= y2_lim[0] and y2 <= y2_O + d:
                    # x2 = float(np.format_float_positional(x2, precision=precision))
                    # y2 = float(np.format_float_positional(y2, precision=precision))
                    # z2 = float(np.format_float_positional(z2, precision=precision))
                    # x2 = float(round(x2, precision))
                    # y2 = float(round(y2, precision))
                    # z2 = float(round(z2, precision))
                    row_data2 = [x2, y2, z2, pressure2]
                    data.append(row_data2)

                if x3 >= x3_O - d and x3 <= x3_lim[1] and y3 >= y3_O - d and y3 <= y3_lim[1]:
                    # x3 = float(np.format_float_positional(x3, precision=precision))
                    # y3 = float(np.format_float_positional(y3, precision=precision))
                    # z3 = float(np.format_float_positional(z3, precision=precision))
                    # x3 = float(round(x3, precision))
                    # y3 = float(round(y3, precision))
                    # z3 = float(round(z3, precision))
                    row_data3 = [x3, y3, z3, pressure3]
                    data.append(row_data3)

                if x4 >= x4_lim[0] and x4 <= x4_O + d and y4 >= y4_O - d and y4 <= y4_lim[1]:
                    # x4 = float(np.format_float_positional(x4, precision=precision))
                    # y4 = float(np.format_float_positional(y4, precision=precision))
                    # z4 = float(np.format_float_positional(z4, precision=precision))
                    # x4 = float(round(x4, precision))
                    # y4 = float(round(y4, precision))
                    # z4 = float(round(z4, precision))
                    row_data4 = [x4, y4, z4, pressure4]
                    data.append(row_data4)
            else:
                if x1 >= x1_lim[0]-tol and x1 <= x1_O + d  and y1 >= y1_lim[0]-tol and y1 <= y1_O + d:
                    x1 = float(np.format_float_positional(x1, precision=precision))
                    y1 = float(np.format_float_positional(y1, precision=precision))
                    z1 = float(np.format_float_positional(z1, precision=precision))
                    row_data1 = [x1, y1, z1, pressure1]
                    data.append(row_data1)

                if x2 >= x2_O - d and x2 <= x2_lim[1]+tol and y2 >= y2_lim[0]-tol and y2 <= y2_O + d:
                    x2 = float(np.format_float_positional(x2, precision=precision))
                    y2 = float(np.format_float_positional(y2, precision=precision))
                    z2 = float(np.format_float_positional(z2, precision=precision))
                    row_data2 = [x2, y2, z2, pressure2]
                    data.append(row_data2)

                if x3 >= x3_O - d and x3 <= x3_lim[1]+tol and y3 >= y3_O - d and y3 <= y3_lim[1]+tol:
                    x3 = float(np.format_float_positional(x3, precision=precision))
                    y3 = float(np.format_float_positional(y3, precision=precision))
                    z3 = float(np.format_float_positional(z3, precision=precision))
                    row_data3 = [x3, y3, z3, pressure3]
                    data.append(row_data3)

                if x4 >= x4_lim[0]-tol and x4 <= x4_O + d and y4 >= y4_O - d and y4 <= y4_lim[1]+tol:
                    x4 = float(np.format_float_positional(x4, precision=precision))
                    y4 = float(np.format_float_positional(y4, precision=precision))
                    z4 = float(np.format_float_positional(z4, precision=precision))
                    row_data4 = [x4, y4, z4, pressure4]
                    data.append(row_data4)

    if separate == False:
        data = np.array(data)
        xyz_nodes = np.column_stack((data[:, 0:3]))
        pressure = data[:, 3]

        # Sort the data by x, y, and z
        sorted_data = data[np.lexsort((data[:, 2], data[:, 1], data[:, 0]))]

        # Find the unique (x, y, z) values
        unique_xyz, indices = np.unique(sorted_data[:, 0:3], axis=0, return_index=True)

        # Create a new array to store the aggregated data
        aggregated_data = np.zeros((unique_xyz.shape[0], 4))

        # Aggregate the pressure values for each unique (x, y, z) value
        for i, (x, y, z) in enumerate(unique_xyz):
            rows_with_xyz = sorted_data[(sorted_data[:, 0] == x) & (sorted_data[:, 1] == y) & (sorted_data[:, 2] == z)]
            pressure_sum = rows_with_xyz[:, 3].sum()
            aggregated_data[i] = [x, y, z, pressure_sum]
            print(i)
        data = aggregated_data

    data = np.array(data)
    sort_indices = np.lexsort((data[:, 0], data[:, 1], data[:, 2]))
    sorted_data = data[sort_indices]

    writer.writerows(sorted_data)


