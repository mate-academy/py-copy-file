def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) == 3 and command_parts[0] == "cp":
        command_type, source_file, copied_file = command_parts
        if source_file != copied_file:
            with (open(source_file, "r") as file_in,
                  open(copied_file, "w") as file_out):
                file_out.write(file_in.read())
