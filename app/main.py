def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) == 3:
        cmd, source, destination = split_command
        if cmd == "cp" and source != destination:
            with open(source, "r") as file_in, open(destination, "w") as file_out:
                file_out.write(file_in.read())
