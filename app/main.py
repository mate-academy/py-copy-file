def copy_file(command: str) -> None:
    parts = command.split()
    cp = parts[0]
    old_file = parts[1]
    new_file = parts[2]

    if len(parts) != 3 or cp != "cp":
        raise ValueError("Invalid command format.")

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        if file_in == file_out:
            return
        input_data = file_in.read()
        file_out.write(input_data)
