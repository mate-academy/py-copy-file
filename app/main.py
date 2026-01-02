def copy_file(command: str) -> None:
    str_split = command.split(" ")
    if len(str_split) != 3:
        return

    action, source, target = str_split
    if action != "cp":
        return
    if source == target:
        return

    try:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
