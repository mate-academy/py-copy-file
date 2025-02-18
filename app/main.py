def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "cp":
        file_r = command_parts[1]
        file_w = command_parts[2]
        if file_r != file_w:
            with open(file_r, "r") as file_in, open(file_w, "w") as file_out:
                file_out.write(file_in.read())
