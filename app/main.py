def copy_file(command: str) -> None:
    names_list = command.split(" ")
    if names_list[1] != names_list[2]:
        with (open(names_list[1], "r") as file_in,
              open(names_list[2], "w") as file_out):
            file_out.write(file_in.read())
