import csv
import matplotlib.pyplot as plt
import numpy as np

# specify the path to your CSV file
csv_path = 'thrust_force-rfile.csv'

#
n=[]
force=[]
flow_time=[]

# read in the CSV file and extract the x, y, z, and pressure values
with open(csv_path, 'r') as f:
    reader = csv.reader(f,delimiter=' ')
    for row in reader:
        n.append(float(row[0]))
        force.append(float(row[1]))
        flow_time.append(float(row[2]))

force_converged=force[1000:]
average_force=np.format_float_positional(np.mean(force_converged),precision=4)
print("Converged thrust force="+str(average_force)+" [N]")

fig=plt.figure()
plt.plot(flow_time,force)
plt.title("Thrust force during the simulation\n Converged thrust force="+str(average_force)+" [N]")
plt.xlabel("Flow time [s]")
plt.ylabel("Thrust force [N]")
plt.show()