def copy_file(command: str) -> None:
    separate = command.split()
    old_file = separate[1]
    new_file = separate[2]
    if len(separate) == 3 and separate[0] == "cp" and old_file != new_file:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            for each_line in file_in:
                file_out.write(each_line)
    else:
        raise ValueError("Incorrect command line.")
