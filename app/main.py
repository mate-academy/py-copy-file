def copy_file(files_name: str):
    file1 = files_name.split()[1]
    file2 = files_name.split()[2]
    if file1 != file2:
        with open(file1, 'r') as file:
            with open(file2, 'w') as new_file:
                new_file.write(file.read())
