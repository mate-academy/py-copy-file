def copy_file(command: str) -> None:
    try:
        command_in, file_in, new_file = command.split()
    except ValueError:
        return

    if file_in == new_file or command_in != "cd":
        return

    with (open(file_in, "r") as file_in,
          open(new_file, "w") as new_file):
        new_file.write(file_in.read())
