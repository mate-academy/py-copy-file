def copy_file(command: str) -> None:
    try:
        comm, file_name, new_file_name = command.split()
    except ValueError:
        return

    if comm != "cp":
        return

    if file_name != new_file_name:
        try:
            with (open(file_name, "r") as file,
                  open(new_file_name, "w") as new_file):
                new_file.write(file.read())
        except FileNotFoundError:
            return
