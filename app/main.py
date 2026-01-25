def copy_file(command: str) -> None:
    if not command:
        return

    parts = command.split()

    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return

    data_file_in = parts[1]
    data_file_out = parts[2]

    if data_file_in == data_file_out:
        return

    try:
        with (
            open(data_file_in, "r") as file_in,
            open(data_file_out, "w") as file_out,
        ):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
