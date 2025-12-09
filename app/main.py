def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) < 3:
        print("You must specify a command and two files, \
        for example: cp source.txt dest.txt")
        return

    cmd, file_in, file_out = parts[0], parts[1], parts[2]

    if cmd != "cp":
        print(f"Invalid command: {cmd}")
        return

    if file_in == file_out:
        print("The files are the same, no copying required.")
        return

    try:
        with open(file_in, "r") as file_in, open(file_out, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"{file_in} was not found.")
