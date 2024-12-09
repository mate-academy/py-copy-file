def copy_file(command: str) -> None:
    if isinstance(command, str) and command.split(" ")[0] == "cp":
        file_name = command.split(" ")[1]
        destination_file = command.split(" ")[2]
        if file_name == destination_file:
            return None
        with (open(file_name, "r") as fro,
              open(destination_file_file, "w") as dest):
            dest.write(fro.read())
