def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Error: Command format is incorrect.")
        return
    name_to_copy, new_name = parts[1], parts[2]
    if name_to_copy == new_name:
        return
    with open(name_to_copy, "r") as file_in, open(new_name, "w") as file_out:
        file_out.write(file_in.read())
