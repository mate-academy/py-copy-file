def copy_file(command: str) -> None:
    commands = command.split()
    source_file = commands[1]
    destination_file = commands[2]

    if source_file != destination_file and commands[0] == "cp":
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
