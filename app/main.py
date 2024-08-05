def copy_file(command: str) -> None:
    if command.startswith("cp "):
        read_from, write_to = command[3:].split()
        if read_from != write_to:
            with (open(read_from, "r") as file_in,
                  open(write_to, "w") as file_out):
                file_out.write(file_in.read())
