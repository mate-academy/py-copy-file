def copy_file(command: str) -> None:
    names = command.split(" ")
    first_file = names[1]
    copys_file = names[2]
    if len(names) == 3 and names[0] == "cd" and not first_file == copys_file:
        with (open(first_file, "r") as file_in,
              open(copys_file, "w") as file_out):
            file_out.write(file_in.read())
