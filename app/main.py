def copy_file(command: str) -> None:
    if len(command) == 0:
        return
    if len(command.split()) < 3:
        return
    if command.split()[0] != "cp":
        return

    file_name = command.split()[1]
    new_file_name = command.split()[2]

    if file_name == new_file_name:
        return
    source_content = ""

    try:
        with open(file_name, "r") as source_file:
            source_content = source_file.read()
    except Exception:
        print("No file")
    else:
        with open(new_file_name, "w") as new_file:
            new_file.write(source_content)
