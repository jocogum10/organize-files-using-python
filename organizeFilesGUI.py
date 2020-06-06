#! python3

# organizes your PDf documents base on whether the filename has a keyword you are looking for
# usage: run command - python3 organizeFiles.py

import tkinter
from tkinter import ttk
from tkinter import filedialog
import shutil, os, sys
from datetime import datetime

# define the functions
def moveByFiletype(filetype, workingFolder,destinationFolder):
    movedfiles = 0
    if os.path.isdir(workingFolder) and os.path.isdir(destinationFolder):
        txtfile = os.path.join(destinationFolder, 'list_of_files.txt')
        listOfFiles = open(txtfile, 'a+')
        listOfFiles.write(f'\nMoving By Filetype: {filetype}\n')
        listOfFiles.write(f'\n{datetime.utcnow()}\n')

        # start moving files
        for foldername, subfolder, filenames in os.walk(workingFolder):
            # skip the destination folder if walked
            if foldername == destinationFolder:
                continue
            # check for the filetypes
            for filename in filenames:
                if filename.endswith(filetype):
                    # move the file to the destination folder
                    currDir = os.path.join(foldername,filename)
                    destinationDir = os.path.join(destinationFolder, filename)
                    shutil.move(currDir, destinationDir)
                    movedfiles += 1
                    print(f"Moving {filename}...")
                    listOfFiles.write(currDir + '\n')

        print('Completed...')
        listOfFiles.write(f"Completed.\nMoved {movedfiles} files.")
        listOfFiles.close()
    else:
        print('There was an error moving files by filetype')
        sys.exit(1)
        
def moveByKeyword(keyword, workingFolder,destinationFolder):
    movedfiles = 0
    if os.path.isdir(workingFolder) and os.path.isdir(destinationFolder):
        txtfile = os.path.join(destinationFolder, 'list_of_files.txt')
        listOfFiles = open(txtfile, 'a+')
        listOfFiles.write(f'\nMoving By Keyword: {keyword}\n')
        listOfFiles.write(f'\n{datetime.utcnow()}\n')

        # start moving files
        for foldername, subfolder, filenames in os.walk(workingFolder):
            # skip the destination folder if walked
            if foldername == destinationFolder:
                continue
            # check for the filetypes
            for filename in filenames:
                if keyword in filename:
                    # move the file to the destination folder
                    currDir = os.path.join(foldername,filename)
                    destinationDir = os.path.join(destinationFolder, filename)
                    shutil.move(currDir, destinationDir)
                    movedfiles += 1
                    print(f"Moving {filename}...")
                    listOfFiles.write(currDir + '\n')

        print('Completed...')
        listOfFiles.write(f"Completed.\nMoved {movedfiles} files.")
        listOfFiles.close()
    else:
        print('There was an error moving files by filetype')
        sys.exit(1)

# define the askdirectory function
def askWorkingDirectory():
    wrkingDir = filedialog.askdirectory(initialdir=".")
    if os.path.isdir(wrkingDir):
        workingFolderEntry.insert(0,wrkingDir)
def askDestinationDirectory():
    destDir = filedialog.askdirectory(initialdir=".")
    if os.path.isdir(destDir):
        destinationFolderEntry.insert(0,destDir)


# make the GUI
root = tkinter.Tk()

# layout
# column 0
tkinter.Label(root, text="Keyword", width=25).grid(row=0, column=0)
tkinter.Label(root, text="Filetype", width=25).grid(row=1, column=0)
tkinter.Label(root, text="Working folder", width=25).grid(row=2, column=0)
tkinter.Label(root, text="Destination folder", width=25).grid(row=3, column=0)
#column 1
keywordEntry = tkinter.Entry(root, width=50)
filetypeEntry = ttk.Combobox(root, values=['.pdf', '.txt', '.epub'])
filetypeEntry.current(1)
workingFolderEntry = tkinter.Entry(root, width=50)
destinationFolderEntry = tkinter.Entry(root, width=50)
keywordEntry.grid(row=0,column=1)
filetypeEntry.grid(row=1,column=1, sticky="nsew")
workingFolderEntry.grid(row=2,column=1)
destinationFolderEntry.grid(row=3,column=1)
# column 2
workingFolderDialog = tkinter.Button(root,text="Select the working directory", command=lambda:askWorkingDirectory())
destinationFolderDialog = tkinter.Button(root,text="Select the destination directory", command=lambda:askDestinationDirectory())
workingFolderDialog.grid(row=2,column=2,sticky="nsew")
destinationFolderDialog.grid(row=3,column=2,sticky="nsew")

# options for the commands
moveByKeywordButton = tkinter.Button(root,text="Move Files by Keyword", command=(lambda:moveByKeyword(keyword=keywordEntry.get(), workingFolder=workingFolderEntry.get(),destinationFolder=destinationFolderEntry.get())))
moveByFiletypeButton = tkinter.Button(root,text="Move Files by Filetype", command=(lambda:moveByFiletype(filetype=filetypeEntry.get(), workingFolder=workingFolderEntry.get(),destinationFolder=destinationFolderEntry.get())))
moveByKeywordButton.grid(row=0,column=2, sticky="nsew")
moveByFiletypeButton.grid(row=1,column=2, sticky="nsew")

if __name__ == '__main__':
    root.mainloop()

