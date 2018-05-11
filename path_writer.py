import os
import csv
import numpy as np

path = []

for root, dirs, files in os.walk(os.path.abspath("...")):
    for file in files:
        path.append(os.path.join(root, file))

path = np.array(path)
print(path)

with open(".../.csv", 'w') as myfile:
    for singlefile in path:
        myfile.write(singlefile+'\n')
