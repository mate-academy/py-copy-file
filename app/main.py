def copy_file(command: str) -> None:
    if (
            command.split()[0] == "cp"
            and command.split()[1] != command.split()[2]
    ):
        command_parts = command.split()
        if len(command_parts) == 3:
            source_file, target_file = command_parts[1], command_parts[2]
            with (open(source_file, "r") as file,
                  open(target_file, "w") as new_file):
                new_file.write(file.read())
