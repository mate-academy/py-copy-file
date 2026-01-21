def copy_file(command: str) -> None:
    args = command.split()
    if len(args) == 3 and args[0] == "cp" and args[1] != args[2]:
        with open(args[1], "r") as file_in, open(args[2], "w") as file_out:
            file_out.write(file_in.read())
