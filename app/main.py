def copy_file(command: str) -> None:
    command_line, original_file, new_file = command.split(" ")
    if command_line == "cp":
        if original_file != new_file:
            with (open(original_file) as file_in,
                  open(new_file, "w") as file_out):
                file_out.write(file_in.read())
