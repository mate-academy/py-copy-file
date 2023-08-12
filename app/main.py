def copy_file(command: str) -> None:
    args = command.split(" ")
    if len(args) == 3:
        com, file_copy, new_file = args
        if com == "cp" and file_copy != new_file:
            with (open(file_copy, "r") as file_in,
                    open(new_file, "w") as file_out):
                file_out.write(file_in.read())
