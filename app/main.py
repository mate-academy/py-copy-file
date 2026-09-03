def copy_file(command: str) -> None:
    result = command.split()
    if len(result) < 3:
        return
    if result[0] != "cp":
        return
    if result[1] == result[2]:
        return
    try:
        with open(result[1], "r") as file_in, open(result[2], "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
