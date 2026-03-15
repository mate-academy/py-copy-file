def copy_file(command: str) -> None:
    parts = command.split()
    if not (len(parts) == 3 and parts[0] == "cp"):
        return
    file_name = parts[1]
    new_file_name = parts[2]
    if file_name == new_file_name:
        return
    try:
        with open(file_name, "r") as file_in:
            with open(new_file_name, "w") as file_out:
                content = file_in.read()
                file_out.write(content)
    except FileNotFoundError:
        return
