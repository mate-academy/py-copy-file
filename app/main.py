def copy_file(command: str) -> None:
    try:
        cp_command, origin_file_name, new_file_name = command.split()
    except ValueError:
        return

    if origin_file_name == new_file_name:
        return
    elif cp_command != "cp":
        return

    with open(origin_file_name, "r") as file_in, \
        open(new_file_name, "w") \
            as file_out:
        content = file_in.read()
        file_out.write(content)
