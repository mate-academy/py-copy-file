def copy_file(command: str) -> None:
    if not command.startswith("cp "):
        return
    read_from, write_to = command[3:].split(" ")
    if read_from == write_to:
        return

    with open(read_from, "r") as file_in, open(write_to, "w") as file_out:
        file_out.write(file_in.read())
