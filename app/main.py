def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format")
        return

    file_name = parts[1]
    new_file_name = parts[2]

    if file_name == new_file_name:
        print("Source and destination files have the same name")
        return

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        text = file_in.read()
        file_out.write(text)
