def copy_file(command: str) -> None:
    command_elements = command.split()
    if len(command_elements) == 3 and command_elements[0] == "cp":
        f_1, f_2 = command_elements[1], command_elements[2]
        if f_1 != f_2:
            with open(f_1, "r") as file_in, open(f_2, "w") as file_out:
                file_out.write(file_in.read())
