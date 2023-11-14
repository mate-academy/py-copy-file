def copy_file(command: str) -> None | str:
    file_names = command.split()

    if len(file_names) != 3 or file_names[1] == file_names[2]:
        return "invalid format"

    old_file, new_file = file_names[1], file_names[2]

    # Copy the file content from source to destination
    with open(old_file, "r") as file_to_copy, open(new_file, "w") as new_file:
        file_content = file_to_copy.readlines()
        new_file.write("".join(file_content))
