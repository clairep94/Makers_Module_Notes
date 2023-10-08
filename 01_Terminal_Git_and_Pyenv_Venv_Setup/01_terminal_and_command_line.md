# COMMAND LINE:

## NAVIGATION:

`; pwd` print working directory

`; ls` list

`; cd` change directory

`; cd ..` go up one directory. first . is the current location

`; cd ./` folderName go to folder within current directory

`; ls -A` show hidden files

`; ls -l` list long format

`; ls -lA` or `;ls - Al` hidden files list long format


## DIRECTORY:

`mkdir newFolder newFolder2` make directory --> spaces indicate separate directories, this will make two folders.

`rmdir` newFolder removed empty directory

`rm -r` newFolder  remove both the folder and the items inside. rm command takes two params:

    `-r` is a switch and tells the remove command to recursively remove all files within a directory
    
    `newFolder` is the location


## FILE MANIPULATION:

`touch newFile.txt` make a new file -- don't need to specify file type, but you can. If no extension, then it is an empty file with no file type.

`cp someFile newFile` copies file -- someFile is the file to copy, newFile is the copied file's name

`mv newFile ../newFile` moves file, in this case to the parent directory.

`mv newFile ./Folder/newFile` moves file to Folder

`mv newFile newNameFile` renames file
    first param: name and location of file. No need to include if in the wd
    second param: name and location of file after moving

`echo "string" > textFile.txt` writes text to a file. Use the same rules as python (\n, ''' ''')



## ZIP FILE:

Make sure you're in the working directory containing the file to be zipped. You must see the file in `ls`, not be inside it.


`; zip -r chapter_1_drills.zip drills`