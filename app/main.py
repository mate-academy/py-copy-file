def copy_file(command: str) -> None:
    command_name, file_in, file_out, *_ = command.split()
    if command_name == "cp" and file_in != file_out:
        return
    with (open(f"{file_in}", "r") as file,
          open(f"{file_out}", "w") as new_file):
        new_file.write(file.read())
