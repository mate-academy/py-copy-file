def copy_file(command: str) -> None:
    act, first_file, second_file = command.split()
    if act == "cp":
        if first_file[1] != second_file[2]:
            with (open(first_file, "r") as file_in,
                  open(second_file, "w") as file_out):
                file_out.write(file_in.read())
