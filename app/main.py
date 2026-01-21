def copy_file(command: str) -> None:
    string = command.split()
    if len(string) == 3:
        if string[1] != string[2] and string[0] == "cp":
            with (
                open(string[1], "r") as file_in,
                open(string[2], "w") as file_out
            ):
                file_out.write(file_in.read())
