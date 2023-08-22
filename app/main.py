def copy_file(command: str) -> None:
    splitted_command = command.split()

    if splitted_command[0] != "cp":
        return

    source_file = splitted_command[1]
    destination_file = splitted_command[2]

    if source_file != destination_file:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out,
        ):
            for line in file_in.readlines():
                file_out.write(line)
