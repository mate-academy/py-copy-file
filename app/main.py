def copy_file(commands_str: str) -> None:
    commands_list, file_out, file_in = commands_str.split()
    if (len(commands_list) == 3 and commands_list[0] == "cp"
            and file_out != file_in):
        with open(file_out, "r") as file_out, open(file_in, "w") as file_in:
            file_in.write(file_out.read())
