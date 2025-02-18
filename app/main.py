def copy_file(command: str) -> None:
    separate = command.split()
    if len(separate) != 3:
        raise ValueError("Incorrect command line.")
    old_file = separate[1]
    new_file = separate[2]
    if separate[0] == "cp" and old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            for each_line in file_in:
                file_out.write(each_line)
