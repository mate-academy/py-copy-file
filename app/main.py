def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) == 3 and command_parts[0] == "cp":
        if command_parts[1] != command_parts[2]:
            with (open(command_parts[1], "r") as source_file,
                  open(command_parts[2], "w") as destination_file):
                for line in source_file:
                    destination_file.write(line)
