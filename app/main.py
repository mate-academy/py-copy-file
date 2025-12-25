def copy_file(command: str) -> None:
    splitted_command = command.split(" ")
    linux_command = splitted_command[0]
    file_name = ""
    file_to_copy_name = ""
    if len(splitted_command) == 3:
        file_name = splitted_command[1]
        file_to_copy_name = splitted_command[2]
    if (
        file_name
        and file_to_copy_name
        and file_name != file_to_copy_name
        and linux_command == "cp"
    ):
        try:
            with open(file_name, "r") as file_in, \
                    open(file_to_copy_name, "w") as file_out:
                file_out.write(file_in.read())
        except FileNotFoundError:
            pass
