def copy_file(command: str) -> None:
    try:
        command, current_file_name, new_file_name = command.split()
    except ValueError:
        print("Command must have 3 arguments")
        return
    if current_file_name == new_file_name or command != "cp":
        return
    with (open(current_file_name, "r") as current_file,
          open(new_file_name, "w") as new_file):
        new_file.write(current_file.read())
