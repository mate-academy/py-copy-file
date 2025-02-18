def copy_file(command: str) -> None:
    try:
        if len(command.split()) == 3:
            cp_command, origin_file_name, new_file_name = command.split()
    except ValueError:
        return f"Error encountered. {ValueError}"

    if origin_file_name == new_file_name:
        return
    elif cp_command != "cp":
        return

    try:
        with open(origin_file_name, "r") as file_in, \
            open(new_file_name, "w") \
                as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return f"Error occured. File was not found in said directory.\n \
            {FileNotFoundError}"
