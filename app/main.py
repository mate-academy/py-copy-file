def copy_file(command: str) -> None:
    new_line = command.split()
    if len(new_line) == 3:
        if new_line[0] == "cp" and new_line[1] != new_line[2]:
            try:
                with (
                    open(new_line[1], "r") as file_in,
                    open(new_line[2], "w") as file_out
                ):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                pass
