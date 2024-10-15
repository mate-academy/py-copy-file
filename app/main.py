def copy_file(command: str) -> None:
    copy_command, source_file, destination_file = command.split(" ")

    if copy_command == "cp":
        if source_file == destination_file:
            return

        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            for line in file_in:
                file_out.write(line)
