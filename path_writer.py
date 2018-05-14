import os
import csv

# write file path into a csv file
def on_click():
    path = []
    
    homedir = str(home.get()) # get content from home and convert it to string
    
    csvlocdir = str(csvloc.get()) # get content from home and convert it to string
    
    
    for root, dirs, files in os.walk(os.path.abspath(homedir)):
        for file in files:
            path.append(os.path.join(root, file))

    with open(csvlocdir, 'w') as myfile:
        for singlefile in path:
            myfile.write(singlefile+'\n')
# path writer end
            
  
#GUI Start

from tkinter import *


root = Tk()
root.title()

#GUI Line 1 : Prompt for home folder
l1 = Label(root, text="Home folder path:")
l1.pack()

#GUI Line 2 : Receiving home folder as a string
home_folder = StringVar()
home = Entry(root, textvariable = home_folder)
home_folder.set(" ")
home.pack()

#GUI Line 3 Prompt for csv location
l2 = Label(root, text="csv filename with full path:")
l2.pack()

#GUI Line 4 Receiving csv location as a string
csv_loc = StringVar()
csvloc = Entry(root, textvariable = csv_loc)
csv_loc.set(" ")
csvloc.pack()

#GUI Line 5 "OK Button", click to execute mainloop
Button(root, text="OK", command = on_click).pack()

root.mainloop()

#GUI End
