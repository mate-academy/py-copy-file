def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError
    file_to_copy_name, new_file_name = parts[1], parts[2]
    if file_to_copy_name != new_file_name:
         with open(file_to_copy_name, "r") as file_in, open(new_file_name, "w") as file_out:
            for line in file_in:
                file_out.write(line)
