def copy_file(command: str) -> None:
    file_name_to_copy = command.split(" ")[1]
    new_file_name = command.split(" ")[2]

    if file_name_to_copy == new_file_name:
        return

    with open(file_name_to_copy) as file_to_copy,\
         open(new_file_name, "w") as new_file:
        new_file.writelines(file_to_copy.readlines())
