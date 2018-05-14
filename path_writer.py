import os
import csv
import numpy as np


def on_click():
    path = []

    for root, dirs, files in os.walk(os.path.abspath(home)):
        for file in files:
            path.append(os.path.join(root, file))

    path = np.array(path)
    print(path)

    with open(csvloc, 'w') as myfile:
        for singlefile in path:
            myfile.write(singlefile+'\n')

#GUI Start

from tkinter import *
root.title()

#GUI Line 1 "home folder path: [user inpt]"
l1 = Label(root, text="home folder path:")
l1.pack()
home_folder = StringVar()
home = Entry(root, textvariable = home_folder)
home_folder.set(" ")
home.pack()

#GUI Line 2 "csv location: [user inpt]"
l2 = Label(root, text="csv location:")
l2.pack()
csv_loc = StringVar()
csvloc = Entry(root, textvariable = csv_loc)
csv_loc.set(" ")
csvloc.pack()

#GUI Line 3 "OK Button", click to execute mainloop
Button(root, text="OK", command = on_click).pack()

path = []

root.mainloop()

#GUI End

