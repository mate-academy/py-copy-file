def copy_file(command: str) -> None:
    files_names = command.split(" ")
    if files_names[1] != files_names[2]:
        with open(files_names[1], "r") as file_to_copy, \
                open(files_names[2], "w") as new_file:
            file_content = file_to_copy.readlines()
            new_file.write("".join(file_content))

