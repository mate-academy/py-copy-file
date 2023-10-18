def copy_file(command_str: str) -> None:
    command = command_str.split(" ")
    if command[0] == "cp" and command[1] != command[2]:
        with open(command[1]) as file_out, open(command[2], "w") as file_in:
            file_in.write(file_out.read())
