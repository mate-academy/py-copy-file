def copy_file(command: str) -> None:
    parse_str = command.split()
    if parse_str[1] != parse_str[2] and parse_str[0] == "cp":
        with open(parse_str[1], "r") as f_in, open(parse_str[2], "w") as f_out:
            f_out.write(f_in.read())
