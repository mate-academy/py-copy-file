def copy_file(command: str) -> None:
    cmd_parts = command.split()
    if not (len(cmd_parts) == 3 and cmd_parts[0] == "cp"):
        return

    file_in_name = cmd_parts[1]
    file_out_name = cmd_parts[2]

    if file_in_name == file_out_name:
        return

    with open(file_in_name) as file_in, open(file_out_name, "w") as file_out:
        file_out.write(file_in.read())
