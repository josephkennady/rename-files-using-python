# rename-files-using-python


This script is written in Python and is used to add a prefix to the file names in a specific folder. It makes use of the os and os.path modules in Python.

To use this script, you will need to first specify the path to the folder where the files are located. You can do this by changing the value of the folder_path variable to the desired path.

You can also specify the prefix that you want to add to the file names by changing the value of the prefix variable.

The script uses a for loop to iterate through all the files in the specified folder. Inside the loop, the script checks if the file name already starts with the prefix. If it does not, it creates a new file name by concatenating the prefix and the original file name. Finally, it uses the os.rename() function to rename the file with the new name.

Please note that this script only adds prefix to file name and not change the file content. If you want to do something with the file content, you need to use file related operations like read, write etc.

You can run the script by using any python interpreter, like python3.

Please make sure that you have correct permission to access the folder and files before running the script

Please also note that the script will change the file name permanently, so you should use it with caution and make sure that you have a backup of the files before running it.
