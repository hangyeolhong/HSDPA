import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
f = open("report.2010-11-23_1541CET_tram_ljabru_to_jernbanetorget.txt", 'r')
# 456개

timestamp = []
throughput = []

while True:
    line = f.readline()
    if not line: break
    s = int(line.split()[1])/1000   # ms to sec
    timestamp.append(s)
    elapsed_s = float(line.split()[5])/1000 # ms to sec
    mb = float(line.split()[4]) / 1000000 # byte to Mbyte
    c = mb / elapsed_s    # Mbps
    throughput.append(c)

    # print(timestamp, ", ", throughput)
plt.plot(timestamp,throughput)
plt.xlabel('timestamp (s)')
plt.ylabel('throughput (Mbps)')
plt.show()
f.close()

# df = pd.read_csv("./training.csv", sep=',')
# print(df.head())