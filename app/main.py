def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format")

    with open(parts[1], "r") as file_in, open(parts[2], "w") as file_out:
        if file_in == file_out:
            return
    input_data = file_in.read()
    file_out.write(input_data)
