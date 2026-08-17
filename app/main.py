def copy_file(command: str) -> None:
    result = command.split(" ")

    if len(result) != 3:
        return

    if result[0] != "cp":
        return

    source_file = result[1]
    destination_file = result[2]

    try:
        with open(source_file, "r") as file1:
            content = file1.read()
    except FileNotFoundError:
        return

    with open(destination_file, "w") as file2:
        file2.write(content)
