
def copy_file_from_command_cp(command: str) -> None:
    command_parsed = command.split(" ")
    source_file_name = command_parsed[1]
    destination_file_name = command_parsed[2]

    if source_file_name == destination_file_name:
        print(f"File wasn't copied: source file '{source_file_name}' "
              f"has the same name as the destination file.")
    else:
        with open(source_file_name, "r") as source_file, \
             open(destination_file_name, "w") as destination_file:

            file_in_data = source_file.readlines()
            destination_file.writelines(file_in_data)
