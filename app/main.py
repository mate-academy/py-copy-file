def copy_file(command: str) -> None:
    if command.startswith("cp "):
        command_parts = command.split()
        if len(command_parts) == 3:
            try:
                with (open(command_parts[1], "r") as file_in,
                      open(command_parts[2], "w") as file_out):
                    if command_parts[1] != command_parts[2]:
                        file_out.write(file_in.read())
            except FileNotFoundError:
                print("No such file or directory.")
