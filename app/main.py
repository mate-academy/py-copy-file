def copy_file(command: str) -> None:
    in_file_name, out_file_name = command.split(" ")[1:]
    if in_file_name == out_file_name:
        return

    with open(in_file_name, "r") as in_f, open(out_file_name, "w") as out_f:
        out_f.write(in_f.read())
