def copy_file(command: str) -> None:
    if not command:
        return
    if len(command.split()) != 3:
        return
    if command.split()[0] != "cp":
        return
    data_file_in = command.split()[1]
    data_file_out = command.split()[2]
    if data_file_in == data_file_out:
        return
    if not data_file_in:
        return
    else:
        try:
            with (
                open(data_file_in, "r") as file_in,
                open(data_file_out, "w") as file_out,
            ):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            return
