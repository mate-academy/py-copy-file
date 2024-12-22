def copy_file(command: str) -> None:
    splitted = command.split(" ")
    cm = splitted[0]
    initial_file_name = splitted[1]
    new_file_name = splitted[2]
    if initial_file_name == new_file_name:
        return None
    elif cm != "cp":
        return None
    with (open(initial_file_name, "r") as file_in,
          open(new_file_name, "w") as file_out):
        initial = file_in.readlines()
        for line in initial:
            file_out.write(line)
