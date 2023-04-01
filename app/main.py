def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        new_file = command.split()
        if command[0] == "cp" and new_file[1] != new_file[2]:
            with (open(new_file[1], "r") as file_in,
                  open(new_file[2], "w") as file_out):
                file_out.write(file_in.read())
