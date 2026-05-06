def copy_file(command: str) -> None:
    spl_str = command.split()
    if len(spl_str) == 3 and spl_str[0] == "cp":
        if spl_str[1] != spl_str[2]:
            try:
                with (
                    open(spl_str[1], "r") as file_in,
                    open(spl_str[2], "w") as file_out
                ):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                pass
