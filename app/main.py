def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Error")

    com, f_name, s_name = parts

    if f_name != s_name:
        with open(f_name, "r") as first, open(s_name, "w") as second:
            for line in first:
                second.write(line)
