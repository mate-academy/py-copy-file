def copy_file(command: str) -> None:
    command_name, file_in, file_out, *_ = command.split()
    if ("cp" in command_name
            or file_in != file_out
            or len(command_name) != 3):
        return
    with (open(f"{file_in}", "r") as file,
          open(f"{file_out}", "w") as new_file):
        new_file.write(file.read())
