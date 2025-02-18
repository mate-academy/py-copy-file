def copy_file(command: str) -> None:
    input_line = command.split(" ")
    if len(input_line) != 3 or input_line[0] != "cp":
        print("Wrong command")
        return

    in_file_name, out_file_name = input_line[1:]
    if in_file_name == out_file_name:
        return

    with open(in_file_name, "r") as in_f, open(out_file_name, "w") as out_f:
        out_f.write(in_f.read())
