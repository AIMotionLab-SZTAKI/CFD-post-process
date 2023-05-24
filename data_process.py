import csv
import numpy as np

# Input data:
input = "data_original/dynamic_pressure_field.csv"
output = "data_final/dynamic_pressure_field_processed_round.csv"

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
        node = float(row[0])
        x = float(row[1])
        y = float(row[2])
        z = float(row[3])
        pressure = float(row[4])

        x = x + 0.25
        y = y + 0.25

        # x = np.format_float_positional(x, precision=3)
        # y = np.format_float_positional(y, precision=3)
        # z = np.format_float_positional(z, precision=3)

        x = round(x, 3)
        y = round(y, 3)
        z = round(z, 3)

        row_data=[node,x,y,z,pressure]
        data.append(row_data)
        #writer.writerow([node,x,y,z,pressure])

    data = np.array(data)
    sort_indices = np.lexsort((data[:, 1], data[:, 2], data[:, 3]))
    sorted_data = data[sort_indices]


    writer.writerows(sorted_data)


