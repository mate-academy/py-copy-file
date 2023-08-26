import shutil
import os

def copy_file(source_file, target_file):
    if source_file == target_file:
        return  # Do nothing

    # Check if the source file exists
    if not os.path.isfile(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    # Copy the source file to the target file
    shutil.copyfile(source_file, target_file)

# Test cases
copy_file("D:/All_For_Programming/Projects/py-copy-file/app/file.txt", "D:/All_For_Programming/Projects/py-copy-file/app/new_file.txt")
