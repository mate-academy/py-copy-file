def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        source_file_name, target_file_name = parts[1], parts[2]
    else:
        return
    if source_file_name == target_file_name:
        return

    try:
        with open(source_file_name, "r") as file_in, open(target_file_name,
                                                          "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
