def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) == 3:
        command_name, file, file_copy = parts
        if file != file_copy and command_name == "cd":
            with (open(file, "r") as file_in,
                  open(file_copy, "w") as file_out):
                file_out.write(file_in.read())
