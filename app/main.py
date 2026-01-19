def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3:
        if command_parts[0] == "cp":
            if command_parts[1] != command_parts[2]:
                with open(command_parts[1], "r") as f1, open(command_parts[2], "w") as f2:
                    f2.write(f1.read())
