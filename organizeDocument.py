#! python3

# organizes your PDf documents base on whether the filename has a keyword you are looking for
# usage: run command - python3 organizeDocument.py '{filetype}' '{keyword}' '{working directory}' '{destination folder}'

import shutil, os, sys

# 1. store the keywords, working directory, and destination directory in variables
if len(sys.argv) == 5:
    movedfiles = 0
    filetype = sys.argv[1]
    keyword = sys.argv[2]
    if os.path.isdir(sys.argv[3]):
        workingDir = sys.argv[3]
    else:
        print(f"Working directory given {sys.argv[3]} is not valid.")
        sys.exit(1)
    if os.path.isdir(sys.argv[4]):
        destDir = sys.argv[4]
        textfile = os.path.join(destDir, 'organizeDocument.txt')
        txtDocument = open(textfile, 'a+')
    else:
        print(f"Destination directory given {sys.argv[3]} is not valid.")
        sys.exit(1)
else:
    print("Lacking input arguments.")
    sys.exit(1)

# 2. find all files in which the keyword is in the filename
for foldername, subfolders, filenames in os.walk(workingDir):

    # check if the folder is the destination, then don't scan
    if foldername == destDir:
        continue

    for filename in filenames:
        if filename.endswith(filetype):
            if keyword in filename:
                currDir = os.path.join(foldername, filename)
                destinationDir = os.path.join(destDir, filename)
                # 3. move the files to the destination folder
                print('----------------')
                print(f'Moving "{filename}"...')
                print(f'from "{currDir}"')
                print(f'to "{destinationDir}"')
                print('----------------')
                txtDocument.write('----------------'+ '\n')
                txtDocument.write(f'Moving "{filename}"...'+ '\n')
                txtDocument.write(f'from "{currDir}"'+ '\n')
                txtDocument.write(f'to "{destinationDir}"'+ '\n')
                txtDocument.write('----------------'+ '\n')
                shutil.move(currDir, destinationDir)
                movedfiles += 1

print("Completed")
print(f"Moved {movedfiles} files.")
txtDocument.write("Completed" + '\n')
txtDocument.write(f"Moved {movedfiles} files." + '\n')
txtDocument.close()