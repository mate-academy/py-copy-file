def copy_file(command: str) -> None:
    parth_of_file = command.split(" ")
    if parth_of_file[0] == "cp" and len(parth_of_file) == 3:
        if parth_of_file[1] != parth_of_file[2]:
            try:
                with (open(parth_of_file[1], "r") as file_in,
                      open(parth_of_file[2], "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                pass
