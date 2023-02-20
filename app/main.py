def copy_file(command: str) -> None:
    com = command.split()[0]
    file_name = command.split()[1]
    copy_name = command.split()[2]
    if file_name != copy_name and com == "cp":
        with open(file_name, "r") as f_in, open(copy_name, "w") as f_out:
            f_in_lines = [line for line in f_in.readlines()]
            f_out.write(str(f_in_lines))
