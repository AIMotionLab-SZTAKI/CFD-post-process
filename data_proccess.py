import csv
import numpy as np

# Input data:
input = "dynamic_pressure_field.csv"
output = "dynamic_pressure_field_processed.csv"

# Open input CSV file and output CSV file
with open(input, 'r') as input_file, open(output, 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)

    # Write header line to output CSV file
    writer.writerow(next(reader))

    nodes = []
    x_vals = []
    y_vals = []
    z_vals = []
    pressure_vals = []


    # Iterate through each row in the input CSV file
    for row in reader:
        node = float(row[0])
        x = float(row[1])
        y = float(row[2])
        z = float(row[3])
        pressure = float(row[4])

        x = x + 0.25
        y = y + 0.25

        x = np.format_float_positional(x,precision=2)
        y = np.format_float_positional(y,precision=2)
        z = np.format_float_positional(z,precision=2)



        writer.writerow([node, x, y, z, pressure])


