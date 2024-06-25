def copy_file(commands_str: str) -> None:
    commands_list = commands_str.split()
    file_out = commands_list[1]
    file_in = commands_list[2]
    with open(file_out, "r") as file_out:
        with open(file_in, "w") as file_in:
            file_in.write(file_out.read())
