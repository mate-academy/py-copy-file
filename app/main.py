def copy_file(command: str) -> None:
    com, f_name, s_name = command.split(" ")

    if f_name != s_name:
        with open(f_name, "r") as first, open(s_name, "w") as second:
            for line in first:
                second.write(line)
