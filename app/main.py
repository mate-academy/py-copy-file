def copy_file(command: str) -> None:
    cmd, source, destination = command.split()
    if len(cmd) == 3:
        if cmd == "cp" and (source != destination):
            with (open(source, "r") as file_in,
                  open(destination, "w") as file_out):
                file_out.write(file_in.read())
